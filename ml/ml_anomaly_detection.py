"""
Phase 3.3: Anomaly Detection Module
Time-series analysis for vital signs anomaly detection
Auto-calibrating thresholds and critical deviation alerts
"""

import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any
import warnings

import numpy as np
import pandas as pd
from scipy import stats
from scipy.signal import savgol_filter
import json

from core.safe_logging import mask_identifier

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

warnings.filterwarnings('ignore')


class VitalSignsAnomalyDetector:
    """Detect anomalies in vital signs using statistical methods"""
    
    # Normal vital sign ranges (conservative)
    NORMAL_RANGES = {
        'heart_rate': {'min': 50, 'max': 110, 'units': 'bpm'},
        'blood_pressure_sys': {'min': 90, 'max': 140, 'units': 'mmHg'},
        'blood_pressure_dia': {'min': 50, 'max': 90, 'units': 'mmHg'},
        'respiratory_rate': {'min': 12, 'max': 25, 'units': 'breaths/min'},
        'temperature': {'min': 36.0, 'max': 38.5, 'units': '°C'},
        'oxygen_saturation': {'min': 92, 'max': 100, 'units': '%'},
        'glucose': {'min': 70, 'max': 180, 'units': 'mg/dL'}
    }
    
    def __init__(self):
        self.anomaly_history = []
        self.calibration_data = {}
        self.alert_history = []
    
    def simple_threshold_detection(self, vitals: Dict) -> List[Dict]:
        """Detect anomalies using simple threshold method"""
        anomalies = []
        
        for vital_name, value in vitals.items():
            if vital_name not in self.NORMAL_RANGES:
                continue
            
            ranges = self.NORMAL_RANGES[vital_name]
            
            if value < ranges['min']:
                anomalies.append({
                    'vital': vital_name,
                    'value': value,
                    'normal_range': f"{ranges['min']}-{ranges['max']}",
                    'type': 'low',
                    'severity': self._calculate_severity(vital_name, value, ranges, 'low'),
                    'method': 'threshold'
                })
            elif value > ranges['max']:
                anomalies.append({
                    'vital': vital_name,
                    'value': value,
                    'normal_range': f"{ranges['min']}-{ranges['max']}",
                    'type': 'high',
                    'severity': self._calculate_severity(vital_name, value, ranges, 'high'),
                    'method': 'threshold'
                })
        
        return anomalies
    
    def z_score_detection(self, vital_timeseries: pd.DataFrame, window: int = 20) -> Dict:
        """Detect anomalies using Z-score method on time series"""
        anomalies_by_vital = {}
        
        for column in vital_timeseries.columns:
            data = vital_timeseries[column].values
            
            # Calculate rolling mean and std
            rolling_mean = pd.Series(data).rolling(window=window, center=True).mean().values
            rolling_std = pd.Series(data).rolling(window=window, center=True).std().values
            
            # Calculate Z-scores
            z_scores = np.abs((data - rolling_mean) / (rolling_std + 1e-8))
            
            # Detect anomalies (Z-score > 3)
            anomaly_indices = np.where(z_scores > 3)[0]
            
            anomalies = []
            for idx in anomaly_indices:
                anomalies.append({
                    'index': int(idx),
                    'timestamp': vital_timeseries.index[idx] if hasattr(vital_timeseries.index, 'tolist') else idx,
                    'value': float(data[idx]),
                    'expected': float(rolling_mean[idx]),
                    'deviation': float(z_scores[idx]),
                    'severity': 'high' if z_scores[idx] > 4 else 'medium'
                })
            
            if anomalies:
                anomalies_by_vital[column] = anomalies
        
        return anomalies_by_vital
    
    def isolation_forest_detection(self, vitals_df: pd.DataFrame) -> List[Dict]:
        """Detect anomalies using Isolation Forest approach (simplified)"""
        anomalies = []
        
        # For each vital sign, calculate isolation scores
        for column in vitals_df.columns:
            data = vitals_df[column].values
            
            # Simplified anomaly score: deviation from median
            median = np.median(data)
            mad = np.median(np.abs(data - median))
            
            # Modified Z-score
            if mad != 0:
                mod_z_scores = 0.6745 * (data - median) / mad
            else:
                mod_z_scores = np.zeros_like(data)
            
            # High anomaly score indicates outlier
            anomaly_scores = np.abs(mod_z_scores)
            
            # Flag anomalies with high scores
            threshold = 3.5
            anomaly_indices = np.where(anomaly_scores > threshold)[0]
            
            for idx in anomaly_indices:
                anomalies.append({
                    'vital': column,
                    'index': int(idx),
                    'value': float(data[idx]),
                    'median': float(median),
                    'anomaly_score': float(anomaly_scores[idx]),
                    'severity': 'critical' if anomaly_scores[idx] > 5 else 'high'
                })
        
        return sorted(anomalies, key=lambda x: x['anomaly_score'], reverse=True)
    
    def detect_rapid_changes(self, vital_timeseries: pd.DataFrame, window: int = 3) -> List[Dict]:
        """Detect rapid changes in vital signs"""
        anomalies = []
        
        for column in vital_timeseries.columns:
            data = vital_timeseries[column].values
            
            # Calculate rate of change
            diffs = np.diff(data)
            
            # Calculate rolling std of changes
            rolling_std_diffs = pd.Series(diffs).rolling(window=window).std().values
            
            # Detect rapid changes (2+ std of typical changes)
            threshold_indices = np.where(np.abs(diffs) > 2 * np.nanstd(rolling_std_diffs))[0]
            
            for idx in threshold_indices:
                if idx + 1 < len(data):
                    anomalies.append({
                        'vital': column,
                        'index': int(idx),
                        'rate_of_change': float(diffs[idx]),
                        'previous_value': float(data[idx]),
                        'current_value': float(data[idx + 1]),
                        'severity': 'high' if abs(diffs[idx]) > 3 * np.nanstd(rolling_std_diffs) else 'medium'
                    })
        
        return anomalies
    
    def _calculate_severity(self, vital_name: str, value: float, ranges: Dict, direction: str) -> str:
        """Calculate severity of anomaly"""
        if direction == 'low':
            deviation_percent = (ranges['min'] - value) / ranges['min'] * 100
        else:
            deviation_percent = (value - ranges['max']) / ranges['max'] * 100
        
        if deviation_percent > 50:
            return 'critical'
        elif deviation_percent > 30:
            return 'high'
        elif deviation_percent > 15:
            return 'medium'
        else:
            return 'low'


class AdaptiveThresholdCalibration:
    """Auto-calibrate thresholds based on patient history"""
    
    def __init__(self, history_window_days: int = 14):
        self.history_window_days = history_window_days
        self.patient_baselines = {}
        self.calibration_history = []
    
    def calibrate_thresholds(self, patient_id: str, vital_timeseries: pd.DataFrame) -> Dict:
        """Calculate personalized thresholds based on patient history"""
        
        baselines = {}
        
        for column in vital_timeseries.columns:
            data = vital_timeseries[column].values
            
            # Calculate percentiles instead of simple min/max
            baseline = {
                'p5': float(np.percentile(data, 5)),
                'p25': float(np.percentile(data, 25)),
                'p50': float(np.percentile(data, 50)),  # Median
                'p75': float(np.percentile(data, 75)),
                'p95': float(np.percentile(data, 95)),
                'mean': float(np.mean(data)),
                'std': float(np.std(data)),
                'min': float(np.min(data)),
                'max': float(np.max(data))
            }
            
            # Define thresholds as mean ± 2*std
            baseline['lower_alert'] = baseline['mean'] - 2 * baseline['std']
            baseline['upper_alert'] = baseline['mean'] + 2 * baseline['std']
            
            # Critical thresholds: mean ± 3*std
            baseline['lower_critical'] = baseline['mean'] - 3 * baseline['std']
            baseline['upper_critical'] = baseline['mean'] + 3 * baseline['std']
            
            baselines[column] = baseline
        
        calibration = {
            'patient_id': patient_id,
            'calibrated_at': datetime.now().isoformat(),
            'baselines': baselines,
            'history_days': self.history_window_days
        }
        
        self.patient_baselines[patient_id] = baselines
        self.calibration_history.append(calibration)
        
        logger.info(f"Thresholds calibrated for patient {mask_identifier(patient_id, 'pat')}")
        return calibration
    
    def get_patient_thresholds(self, patient_id: str) -> Dict:
        """Get calibrated thresholds for a patient"""
        if patient_id in self.patient_baselines:
            return self.patient_baselines[patient_id]
        else:
            logger.warning(f"No calibrated thresholds for patient {mask_identifier(patient_id, 'pat')}")
            return {}
    
    def update_thresholds(self, patient_id: str, vital_name: str, new_value: float):
        """Update thresholds incrementally with new data"""
        if patient_id not in self.patient_baselines:
            return
        
        baseline = self.patient_baselines[patient_id].get(vital_name, {})
        
        if not baseline:
            return
        
        # Exponential moving average update
        alpha = 0.1  # Learning rate
        
        baseline['mean'] = alpha * new_value + (1 - alpha) * baseline.get('mean', new_value)
        baseline['lower_alert'] = baseline['mean'] - 2 * baseline.get('std', 1)
        baseline['upper_alert'] = baseline['mean'] + 2 * baseline.get('std', 1)


class CriticalDeviationAlertSystem:
    """Generate alerts for critical deviations"""
    
    ALERT_THRESHOLDS = {
        'heart_rate': {'critical_low': 40, 'critical_high': 130, 'critical_change': 40},
        'blood_pressure_sys': {'critical_low': 80, 'critical_high': 180, 'critical_change': 50},
        'blood_pressure_dia': {'critical_low': 40, 'critical_high': 120, 'critical_change': 40},
        'respiratory_rate': {'critical_low': 8, 'critical_high': 35, 'critical_change': 15},
        'temperature': {'critical_low': 35.0, 'critical_high': 39.5, 'critical_change': 2.0},
        'oxygen_saturation': {'critical_low': 85, 'critical_high': 100, 'critical_change': 10},
        'glucose': {'critical_low': 50, 'critical_high': 400, 'critical_change': 100}
    }
    
    def __init__(self):
        self.active_alerts = {}
        self.alert_log = []
    
    def evaluate_critical_deviation(self, patient_id: str, vital_name: str, 
                                   current_value: float, previous_value: Optional[float] = None) -> Optional[Dict]:
        """Evaluate if current value is critically deviated"""
        
        if vital_name not in self.ALERT_THRESHOLDS:
            return None
        
        thresholds = self.ALERT_THRESHOLDS[vital_name]
        alert = None
        
        # Check absolute thresholds
        if current_value <= thresholds['critical_low']:
            alert = {
                'type': 'critical_low',
                'vital': vital_name,
                'value': current_value,
                'threshold': thresholds['critical_low'],
                'severity': 'critical'
            }
        elif current_value >= thresholds['critical_high']:
            alert = {
                'type': 'critical_high',
                'vital': vital_name,
                'value': current_value,
                'threshold': thresholds['critical_high'],
                'severity': 'critical'
            }
        
        # Check rate of change
        if previous_value is not None:
            change = abs(current_value - previous_value)
            if change > thresholds['critical_change']:
                alert = {
                    'type': 'rapid_change',
                    'vital': vital_name,
                    'value': current_value,
                    'previous_value': previous_value,
                    'change': change,
                    'threshold': thresholds['critical_change'],
                    'severity': 'high'
                }
        
        if alert:
            alert.update({
                'patient_id': patient_id,
                'timestamp': datetime.now().isoformat(),
                'acknowledged': False,
                'alert_id': f"{patient_id}_{vital_name}_{datetime.now().timestamp()}"
            })
            
            self.active_alerts[alert['alert_id']] = alert
            self.alert_log.append(alert)
            logger.warning(f"ALERT: {alert['type']} for {mask_identifier(patient_id, 'pat')} - {vital_name}={current_value}")
        
        return alert
    
    def acknowledge_alert(self, alert_id: str, notes: str = ""):
        """Acknowledge an alert"""
        if alert_id in self.active_alerts:
            self.active_alerts[alert_id]['acknowledged'] = True
            self.active_alerts[alert_id]['acknowledged_at'] = datetime.now().isoformat()
            self.active_alerts[alert_id]['acknowledgment_notes'] = notes
            logger.info(f"Alert {alert_id} acknowledged")
    
    def get_active_alerts(self, patient_id: str = None) -> List[Dict]:
        """Get all unacknowledged active alerts"""
        active = [a for a in self.active_alerts.values() if not a['acknowledged']]
        
        if patient_id:
            active = [a for a in active if a['patient_id'] == patient_id]
        
        return sorted(active, key=lambda x: x['timestamp'], reverse=True)
    
    def get_alert_summary(self) -> Dict:
        """Get summary of alerts"""
        all_alerts = self.alert_log
        
        return {
            'total_alerts': len(all_alerts),
            'active_alerts': len(self.get_active_alerts()),
            'by_type': self._count_by_field(all_alerts, 'type'),
            'by_severity': self._count_by_field(all_alerts, 'severity'),
            'by_vital': self._count_by_field(all_alerts, 'vital'),
            'last_24h': len([a for a in all_alerts if self._is_recent(a, 24)]),
            'last_7d': len([a for a in all_alerts if self._is_recent(a, 7 * 24)])
        }
    
    def _count_by_field(self, alerts: List[Dict], field: str) -> Dict:
        """Count alerts by field value"""
        counts = {}
        for alert in alerts:
            value = alert.get(field, 'unknown')
            counts[value] = counts.get(value, 0) + 1
        return counts
    
    def _is_recent(self, alert: Dict, hours_ago: int) -> bool:
        """Check if alert is recent"""
        alert_time = datetime.fromisoformat(alert['timestamp'])
        cutoff = datetime.now() - timedelta(hours=hours_ago)
        return alert_time > cutoff


def create_sample_vital_timeseries(n_points: int = 100) -> pd.DataFrame:
    """Create sample vital signs time series"""
    np.random.seed(42)
    
    timestamps = pd.date_range(start='2025-01-01', periods=n_points, freq='15min')
    
    # Create somewhat realistic vital signs patterns
    heart_rate = np.random.normal(75, 8, n_points)
    blood_pressure_sys = np.random.normal(130, 12, n_points)
    blood_pressure_dia = np.random.normal(80, 8, n_points)
    respiratory_rate = np.random.normal(16, 2, n_points)
    temperature = np.random.normal(98.6, 0.5, n_points)
    oxygen_saturation = np.random.normal(97, 1.5, n_points)
    
    # Add some anomalies
    heart_rate[50] = 150  # Spike
    oxygen_saturation[75] = 85  # Dip
    temperature[25] = 100.5  # Fever
    
    df = pd.DataFrame({
        'heart_rate': heart_rate,
        'blood_pressure_sys': blood_pressure_sys,
        'blood_pressure_dia': blood_pressure_dia,
        'respiratory_rate': respiratory_rate,
        'temperature': temperature,
        'oxygen_saturation': oxygen_saturation
    }, index=timestamps)
    
    return df


if __name__ == '__main__':
    logger.info("Initializing Anomaly Detection Module...")
    
    # Create sample data
    vital_ts = create_sample_vital_timeseries(100)
    
    # Test simple threshold detection
    detector = VitalSignsAnomalyDetector()
    current_vitals = {
        'heart_rate': 95,
        'blood_pressure_sys': 120,
        'temperature': 98.6,
        'oxygen_saturation': 97
    }
    
    anomalies = detector.simple_threshold_detection(current_vitals)
    logger.info(f"Simple threshold anomalies: {len(anomalies)}")
    
    # Test Z-score detection
    z_anomalies = detector.z_score_detection(vital_ts, window=10)
    logger.info(f"Z-score anomalies: {len(z_anomalies)}")
    
    # Test threshold calibration
    calibrator = AdaptiveThresholdCalibration()
    calibration = calibrator.calibrate_thresholds('P12345', vital_ts)
    logger.info(f"Calibrated thresholds for patient P12345")
    
    # Test alert system
    alert_system = CriticalDeviationAlertSystem()
    alert = alert_system.evaluate_critical_deviation('P12345', 'oxygen_saturation', 82)
    if alert:
        logger.info(f"Critical alert generated: {alert['type']}")
    
    summary = alert_system.get_alert_summary()
    logger.info(f"Alert summary: {json.dumps(summary, indent=2)}")
    
    logger.info("\nPhase 3.3: Anomaly Detection - Ready for deployment")
