"""
Phase 3.1: Predictive Analytics Module
Machine Learning pipeline for patient outcome prediction
Includes readmission risk, deterioration prediction, and model monitoring
"""

import logging
import pickle
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any
import warnings

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import (
    classification_report, confusion_matrix, roc_auc_score, roc_curve,
    precision_recall_curve, f1_score, accuracy_score
)
from joblib import dump, load
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

warnings.filterwarnings('ignore')


class PredictiveModel:
    """Base class for predictive models"""
    
    def __init__(self, model_name: str, model_type: str = 'random_forest'):
        self.model_name = model_name
        self.model_type = model_type
        self.model = None
        self.scaler = StandardScaler()
        self.label_encoders = {}
        self.feature_names = None
        self.training_history = {
            'created': datetime.now().isoformat(),
            'last_trained': None,
            'accuracy': None,
            'roc_auc': None,
            'f1_score': None,
            'samples_trained': 0
        }
        
        self._initialize_model()
    
    def _initialize_model(self):
        """Initialize the underlying ML model"""
        if self.model_type == 'random_forest':
            self.model = RandomForestClassifier(
                n_estimators=100,
                max_depth=15,
                min_samples_split=10,
                min_samples_leaf=5,
                random_state=42,
                n_jobs=-1,
                class_weight='balanced'
            )
        elif self.model_type == 'gradient_boosting':
            self.model = GradientBoostingClassifier(
                n_estimators=100,
                learning_rate=0.1,
                max_depth=5,
                min_samples_split=10,
                min_samples_leaf=5,
                random_state=42,
                subsample=0.8
            )
        else:
            raise ValueError(f"Unknown model type: {self.model_type}")
        
        logger.info(f"Initialized {self.model_type} model: {self.model_name}")
    
    def preprocess_features(self, X: pd.DataFrame, fit: bool = False) -> np.ndarray:
        """Preprocess features: encode categorical, scale numerical"""
        X_processed = X.copy()
        
        # Encode categorical variables
        for col in X_processed.select_dtypes(include=['object']).columns:
            if fit:
                self.label_encoders[col] = LabelEncoder()
                X_processed[col] = self.label_encoders[col].fit_transform(X_processed[col].astype(str))
            else:
                if col in self.label_encoders:
                    X_processed[col] = self.label_encoders[col].transform(X_processed[col].astype(str))
        
        # Scale numerical features
        if fit:
            X_scaled = self.scaler.fit_transform(X_processed)
        else:
            X_scaled = self.scaler.transform(X_processed)
        
        return X_scaled
    
    def train(self, X: pd.DataFrame, y: pd.Series, test_size: float = 0.2, cv_folds: int = 5):
        """Train the predictive model with cross-validation"""
        logger.info(f"Training {self.model_name} on {len(X)} samples")
        
        # Preprocess features
        self.feature_names = X.columns.tolist()
        X_scaled = self.preprocess_features(X, fit=True)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=test_size, random_state=42, stratify=y
        )
        
        # Train model
        self.model.fit(X_train, y_train)
        
        # Cross-validation scoring
        skf = StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=42)
        cv_scores = cross_val_score(self.model, X_train, y_train, cv=skf, scoring='roc_auc')
        
        # Evaluate on test set
        y_pred = self.model.predict(X_test)
        y_pred_proba = self.model.predict_proba(X_test)[:, 1]
        
        accuracy = accuracy_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        f1 = f1_score(y_test, y_pred)
        
        # Update training history
        self.training_history.update({
            'last_trained': datetime.now().isoformat(),
            'accuracy': float(accuracy),
            'roc_auc': float(roc_auc),
            'f1_score': float(f1),
            'cv_mean': float(cv_scores.mean()),
            'cv_std': float(cv_scores.std()),
            'samples_trained': len(X_train),
            'test_samples': len(X_test)
        })
        
        logger.info(f"Model training complete - Accuracy: {accuracy:.3f}, ROC-AUC: {roc_auc:.3f}, F1: {f1:.3f}")
        logger.info(f"Cross-validation: {cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")
        
        return {
            'accuracy': accuracy,
            'roc_auc': roc_auc,
            'f1_score': f1,
            'cv_scores': cv_scores,
            'confusion_matrix': confusion_matrix(y_test, y_pred),
            'classification_report': classification_report(y_test, y_pred),
            'X_test': X_test,
            'y_test': y_test,
            'y_pred_proba': y_pred_proba
        }
    
    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """Make predictions on new data"""
        if self.model is None:
            raise ValueError("Model not trained yet")
        
        X_scaled = self.preprocess_features(X, fit=False)
        return self.model.predict(X_scaled)
    
    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        """Get prediction probabilities"""
        if self.model is None:
            raise ValueError("Model not trained yet")
        
        X_scaled = self.preprocess_features(X, fit=False)
        return self.model.predict_proba(X_scaled)
    
    def get_feature_importance(self) -> pd.DataFrame:
        """Get feature importance scores"""
        if not hasattr(self.model, 'feature_importances_'):
            raise ValueError("Model doesn't support feature importance")
        
        importance_df = pd.DataFrame({
            'feature': self.feature_names,
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        return importance_df
    
    def save(self, filepath: str):
        """Save model to disk"""
        model_data = {
            'model': self.model,
            'scaler': self.scaler,
            'label_encoders': self.label_encoders,
            'feature_names': self.feature_names,
            'training_history': self.training_history,
            'model_name': self.model_name,
            'model_type': self.model_type
        }
        dump(model_data, filepath)
        logger.info(f"Model saved to {filepath}")
    
    @classmethod
    def load(cls, filepath: str) -> 'PredictiveModel':
        """Load model from disk"""
        model_data = load(filepath)
        instance = cls(model_data['model_name'], model_data['model_type'])
        instance.model = model_data['model']
        instance.scaler = model_data['scaler']
        instance.label_encoders = model_data['label_encoders']
        instance.feature_names = model_data['feature_names']
        instance.training_history = model_data['training_history']
        logger.info(f"Model loaded from {filepath}")
        return instance


class PatientOutcomePredictor:
    """Predict readmission risk and patient deterioration"""
    
    def __init__(self):
        self.readmission_model = PredictiveModel(
            'readmission_risk', 'random_forest'
        )
        self.deterioration_model = PredictiveModel(
            'deterioration_risk', 'gradient_boosting'
        )
        self.monitoring_logs = []
    
    def train_readmission_model(self, df: pd.DataFrame, target_col: str = 'readmitted_30d') -> Dict:
        """Train model to predict 30-day readmission risk"""
        logger.info("Training readmission risk model...")
        
        # Feature engineering
        X, y = self._prepare_features_for_readmission(df, target_col)
        
        results = self.readmission_model.train(X, y)
        self._log_model_performance('readmission', results)
        
        return results
    
    def train_deterioration_model(self, df: pd.DataFrame, target_col: str = 'deteriorated') -> Dict:
        """Train model to predict patient deterioration"""
        logger.info("Training deterioration risk model...")
        
        # Feature engineering
        X, y = self._prepare_features_for_deterioration(df, target_col)
        
        results = self.deterioration_model.train(X, y)
        self._log_model_performance('deterioration', results)
        
        return results
    
    def _prepare_features_for_readmission(self, df: pd.DataFrame, target_col: str) -> Tuple[pd.DataFrame, pd.Series]:
        """Prepare features for readmission prediction"""
        # Select relevant features
        feature_cols = [
            'age', 'los', 'num_comorbidities', 'num_medications',
            'admission_type', 'discharge_type', 'previous_readmissions',
            'has_mental_health', 'has_substance_abuse', 'insurance_type'
        ]
        
        # Filter available columns
        available_cols = [col for col in feature_cols if col in df.columns]
        X = df[available_cols].copy()
        y = df[target_col].astype(int)
        
        # Handle missing values
        X = X.fillna(X.median(numeric_only=True))
        X = X.fillna('Unknown')
        
        logger.info(f"Readmission features: {available_cols}")
        return X, y
    
    def _prepare_features_for_deterioration(self, df: pd.DataFrame, target_col: str) -> Tuple[pd.DataFrame, pd.Series]:
        """Prepare features for deterioration prediction"""
        feature_cols = [
            'heart_rate', 'blood_pressure_sys', 'blood_pressure_dia',
            'respiratory_rate', 'temperature', 'oxygen_saturation',
            'glucose', 'age', 'severity_score', 'qsofa_score',
            'has_infection', 'has_sepsis', 'recent_lab_abnormality'
        ]
        
        available_cols = [col for col in feature_cols if col in df.columns]
        X = df[available_cols].copy()
        y = df[target_col].astype(int)
        
        # Handle missing values
        X = X.fillna(X.median(numeric_only=True))
        
        logger.info(f"Deterioration features: {available_cols}")
        return X, y
    
    def predict_readmission_risk(self, patient_data: pd.DataFrame) -> pd.DataFrame:
        """Predict readmission risk for patients"""
        probabilities = self.readmission_model.predict_proba(patient_data)
        
        results = pd.DataFrame({
            'patient_id': patient_data.index if hasattr(patient_data.index, 'name') else range(len(patient_data)),
            'risk_score': probabilities[:, 1],
            'risk_level': pd.cut(probabilities[:, 1], bins=[0, 0.3, 0.6, 1.0], labels=['Low', 'Medium', 'High']),
            'prediction_timestamp': datetime.now()
        })
        
        return results
    
    def predict_deterioration_risk(self, patient_data: pd.DataFrame) -> pd.DataFrame:
        """Predict deterioration risk for patients"""
        probabilities = self.deterioration_model.predict_proba(patient_data)
        
        results = pd.DataFrame({
            'patient_id': patient_data.index if hasattr(patient_data.index, 'name') else range(len(patient_data)),
            'risk_score': probabilities[:, 1],
            'risk_level': pd.cut(probabilities[:, 1], bins=[0, 0.3, 0.6, 1.0], labels=['Low', 'Medium', 'High']),
            'alert_required': probabilities[:, 1] > 0.7,
            'prediction_timestamp': datetime.now()
        })
        
        return results
    
    def _log_model_performance(self, model_type: str, results: Dict):
        """Log model performance metrics"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'model_type': model_type,
            'accuracy': results['accuracy'],
            'roc_auc': results['roc_auc'],
            'f1_score': results['f1_score']
        }
        self.monitoring_logs.append(log_entry)
        logger.info(f"Performance logged for {model_type}")
    
    def get_feature_importance(self, model_type: str = 'readmission') -> pd.DataFrame:
        """Get feature importance for interpretability"""
        if model_type == 'readmission':
            return self.readmission_model.get_feature_importance()
        elif model_type == 'deterioration':
            return self.deterioration_model.get_feature_importance()
        else:
            raise ValueError(f"Unknown model type: {model_type}")
    
    def save_models(self, readmission_path: str, deterioration_path: str):
        """Save both models to disk"""
        self.readmission_model.save(readmission_path)
        self.deterioration_model.save(deterioration_path)
        logger.info(f"Models saved: {readmission_path}, {deterioration_path}")
    
    @classmethod
    def load_models(cls, readmission_path: str, deterioration_path: str) -> 'PatientOutcomePredictor':
        """Load both models from disk"""
        instance = cls()
        instance.readmission_model = PredictiveModel.load(readmission_path)
        instance.deterioration_model = PredictiveModel.load(deterioration_path)
        logger.info(f"Models loaded: {readmission_path}, {deterioration_path}")
        return instance


class ModelEvaluator:
    """Comprehensive model evaluation and monitoring"""
    
    def __init__(self):
        self.evaluation_history = []
    
    def evaluate_model(self, model: PredictiveModel, X_test: np.ndarray, y_test: np.ndarray) -> Dict:
        """Comprehensive model evaluation"""
        y_pred = model.model.predict(X_test)
        y_pred_proba = model.model.predict_proba(X_test)[:, 1]
        
        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        f1 = f1_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)
        
        # Sensitivity and specificity
        tn, fp, fn, tp = cm.ravel()
        sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
        specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
        ppv = tp / (tp + fp) if (tp + fp) > 0 else 0
        npv = tn / (tn + fn) if (tn + fn) > 0 else 0
        
        evaluation = {
            'model_name': model.model_name,
            'timestamp': datetime.now().isoformat(),
            'accuracy': accuracy,
            'roc_auc': roc_auc,
            'f1_score': f1,
            'sensitivity': sensitivity,
            'specificity': specificity,
            'ppv': ppv,
            'npv': npv,
            'samples_tested': len(y_test)
        }
        
        self.evaluation_history.append(evaluation)
        return evaluation
    
    def get_model_drift(self) -> Optional[Dict]:
        """Detect model performance drift over time"""
        if len(self.evaluation_history) < 2:
            return None
        
        recent = self.evaluation_history[-1]
        previous = self.evaluation_history[-2]
        
        accuracy_drift = recent['accuracy'] - previous['accuracy']
        roc_auc_drift = recent['roc_auc'] - previous['roc_auc']
        
        return {
            'accuracy_drift': accuracy_drift,
            'roc_auc_drift': roc_auc_drift,
            'drifting': abs(accuracy_drift) > 0.05 or abs(roc_auc_drift) > 0.05,
            'drift_timestamp': datetime.now().isoformat()
        }
    
    def get_evaluation_summary(self) -> pd.DataFrame:
        """Get summary of all evaluations"""
        return pd.DataFrame(self.evaluation_history)


# Utility functions for integration with database
def create_sample_patient_data(n_samples: int = 1000) -> pd.DataFrame:
    """Create synthetic patient data for testing"""
    np.random.seed(42)
    
    data = {
        'age': np.random.randint(18, 95, n_samples),
        'los': np.random.randint(1, 30, n_samples),
        'num_comorbidities': np.random.randint(0, 8, n_samples),
        'num_medications': np.random.randint(0, 20, n_samples),
        'admission_type': np.random.choice(['Emergency', 'Planned', 'Transfer'], n_samples),
        'discharge_type': np.random.choice(['Home', 'Facility', 'Expired'], n_samples),
        'previous_readmissions': np.random.randint(0, 5, n_samples),
        'has_mental_health': np.random.choice([0, 1], n_samples),
        'has_substance_abuse': np.random.choice([0, 1], n_samples),
        'insurance_type': np.random.choice(['Medicare', 'Medicaid', 'Private'], n_samples),
        'readmitted_30d': np.random.choice([0, 1], n_samples, p=[0.75, 0.25]),
    }
    
    return pd.DataFrame(data)


def create_sample_vital_signs_data(n_samples: int = 500) -> pd.DataFrame:
    """Create synthetic vital signs data for deterioration prediction"""
    np.random.seed(42)
    
    data = {
        'heart_rate': np.random.normal(70, 15, n_samples),
        'blood_pressure_sys': np.random.normal(130, 20, n_samples),
        'blood_pressure_dia': np.random.normal(80, 12, n_samples),
        'respiratory_rate': np.random.normal(16, 3, n_samples),
        'temperature': np.random.normal(98.6, 1, n_samples),
        'oxygen_saturation': np.random.normal(95, 2, n_samples),
        'glucose': np.random.normal(110, 30, n_samples),
        'age': np.random.randint(18, 95, n_samples),
        'severity_score': np.random.randint(0, 10, n_samples),
        'qsofa_score': np.random.randint(0, 3, n_samples),
        'has_infection': np.random.choice([0, 1], n_samples),
        'has_sepsis': np.random.choice([0, 1], n_samples),
        'recent_lab_abnormality': np.random.choice([0, 1], n_samples),
        'deteriorated': np.random.choice([0, 1], n_samples, p=[0.85, 0.15]),
    }
    
    return pd.DataFrame(data)


if __name__ == '__main__':
    # Example usage
    logger.info("Initializing Predictive Analytics Module...")
    
    # Create sample data
    readmission_data = create_sample_patient_data(1000)
    vital_signs_data = create_sample_vital_signs_data(500)
    
    # Initialize predictor
    predictor = PatientOutcomePredictor()
    
    # Train models
    logger.info("Training models...")
    readmission_results = predictor.train_readmission_model(readmission_data)
    deterioration_results = predictor.train_deterioration_model(vital_signs_data)
    
    # Get feature importance
    logger.info("\nReadmission Risk - Top Features:")
    print(predictor.get_feature_importance('readmission').head(10))
    
    logger.info("\nDeterioration Risk - Top Features:")
    print(predictor.get_feature_importance('deterioration').head(10))
    
    # Make predictions on new data
    new_patients = readmission_data.head(10)
    predictions = predictor.predict_readmission_risk(new_patients)
    logger.info("\nSample Readmission Predictions:")
    print(predictions)
    
    logger.info("\nPhase 3.1: Predictive Analytics Module - Ready for deployment")
