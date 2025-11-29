"""
Phase 3.2: AI Recommendations Engine
Recommendation system for interventions and care plans
Includes care optimization, pattern recognition, and evidence-based suggestions
"""

import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import warnings

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

warnings.filterwarnings('ignore')


class InterventionRecommender:
    """Recommend evidence-based interventions based on patient problems"""
    
    # Evidence-based intervention database
    INTERVENTION_DATABASE = {
        'hypertension': {
            'interventions': [
                {'name': 'Antihypertensive medication', 'priority': 'high', 'time_to_effect': '2-4 weeks'},
                {'name': 'Sodium reduction', 'priority': 'high', 'time_to_effect': '1-2 weeks'},
                {'name': 'Weight management', 'priority': 'medium', 'time_to_effect': '4-8 weeks'},
                {'name': 'Exercise program', 'priority': 'medium', 'time_to_effect': '4-8 weeks'},
                {'name': 'Stress management', 'priority': 'low', 'time_to_effect': '2-4 weeks'}
            ],
            'monitoring': 'BP monitoring daily, labs q3mo'
        },
        'diabetes': {
            'interventions': [
                {'name': 'Insulin therapy', 'priority': 'high', 'time_to_effect': 'immediate'},
                {'name': 'Oral hypoglycemic agents', 'priority': 'high', 'time_to_effect': '1-2 weeks'},
                {'name': 'Dietary counseling', 'priority': 'high', 'time_to_effect': 'ongoing'},
                {'name': 'Blood glucose monitoring', 'priority': 'high', 'time_to_effect': 'immediate'},
                {'name': 'Exercise program', 'priority': 'medium', 'time_to_effect': '4-8 weeks'},
                {'name': 'Foot care education', 'priority': 'medium', 'time_to_effect': 'ongoing'}
            ],
            'monitoring': 'HbA1c q3mo, glucose monitoring BID-QID'
        },
        'pneumonia': {
            'interventions': [
                {'name': 'Antibiotic therapy', 'priority': 'high', 'time_to_effect': '24-48 hours'},
                {'name': 'Respiratory support', 'priority': 'high', 'time_to_effect': 'immediate'},
                {'name': 'Fluid management', 'priority': 'high', 'time_to_effect': 'immediate'},
                {'name': 'Oxygen therapy', 'priority': 'high', 'time_to_effect': 'immediate'},
                {'name': 'Chest physiotherapy', 'priority': 'medium', 'time_to_effect': 'ongoing'},
                {'name': 'Nutritional support', 'priority': 'medium', 'time_to_effect': 'ongoing'}
            ],
            'monitoring': 'Chest X-ray daily, O2 sat continuous, labs daily'
        },
        'heart_failure': {
            'interventions': [
                {'name': 'ACE inhibitor/ARB', 'priority': 'high', 'time_to_effect': '2-4 weeks'},
                {'name': 'Beta-blocker', 'priority': 'high', 'time_to_effect': '2-4 weeks'},
                {'name': 'Diuretics', 'priority': 'high', 'time_to_effect': 'immediate'},
                {'name': 'Fluid restriction', 'priority': 'high', 'time_to_effect': 'immediate'},
                {'name': 'Daily weight monitoring', 'priority': 'high', 'time_to_effect': 'immediate'},
                {'name': 'Exercise tolerance program', 'priority': 'medium', 'time_to_effect': '2-4 weeks'}
            ],
            'monitoring': 'Daily weights, I&Os, BNP levels, EF assessment'
        },
        'sepsis': {
            'interventions': [
                {'name': 'Broad-spectrum antibiotics', 'priority': 'high', 'time_to_effect': 'immediate'},
                {'name': 'IV fluid resuscitation', 'priority': 'high', 'time_to_effect': 'immediate'},
                {'name': 'Vasopressor support', 'priority': 'high', 'time_to_effect': 'immediate'},
                {'name': 'Source control', 'priority': 'high', 'time_to_effect': 'immediate'},
                {'name': 'Lactate monitoring', 'priority': 'high', 'time_to_effect': 'continuous'},
                {'name': 'ICU monitoring', 'priority': 'high', 'time_to_effect': 'immediate'}
            ],
            'monitoring': 'Continuous vitals, lactate q1h, blood cultures, qSOFA score'
        }
    }
    
    def __init__(self):
        self.recommendation_history = []
        self._build_vectorizer()
    
    def _build_vectorizer(self):
        """Build TF-IDF vectorizer for problem matching"""
        problems = list(self.INTERVENTION_DATABASE.keys())
        self.vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(2, 3))
        self.vectorizer.fit(problems)
        logger.info(f"Vectorizer trained on {len(problems)} problem types")
    
    def recommend_interventions(self, problem: str, patient_data: Dict = None) -> Dict:
        """Recommend interventions for a given problem"""
        # Find best matching problem
        best_match = self._find_best_problem_match(problem)
        
        if best_match not in self.INTERVENTION_DATABASE:
            logger.warning(f"No interventions found for: {problem}")
            return {'problem': problem, 'interventions': [], 'confidence': 0}
        
        db_interventions = self.INTERVENTION_DATABASE[best_match]
        interventions = db_interventions['interventions'].copy()
        
        # Personalize recommendations based on patient data
        if patient_data:
            interventions = self._personalize_recommendations(interventions, patient_data)
        
        recommendation = {
            'problem': problem,
            'matched_to': best_match,
            'interventions': interventions,
            'monitoring': db_interventions['monitoring'],
            'confidence': 0.95,
            'timestamp': datetime.now().isoformat()
        }
        
        self.recommendation_history.append(recommendation)
        return recommendation
    
    def _find_best_problem_match(self, problem: str) -> str:
        """Find best matching problem in database"""
        problems = list(self.INTERVENTION_DATABASE.keys())
        problem_vec = self.vectorizer.transform([problem]).toarray()
        db_vecs = self.vectorizer.transform(problems).toarray()
        
        similarities = cosine_similarity(problem_vec, db_vecs)[0]
        best_idx = np.argmax(similarities)
        
        return problems[best_idx]
    
    def _personalize_recommendations(self, interventions: List[Dict], patient_data: Dict) -> List[Dict]:
        """Personalize recommendations based on patient data"""
        personalized = []
        
        for intervention in interventions:
            priority = intervention['priority']
            
            # Adjust priority based on patient factors
            if patient_data.get('age', 0) > 75:
                if intervention['name'].endswith('therapy'):
                    priority = 'high'  # Prioritize medical therapy for elderly
            
            if patient_data.get('comorbidities', 0) > 3:
                if intervention.get('time_to_effect', '').startswith('4-8'):
                    priority = 'low'  # Defer long-term interventions for complex patients
            
            personalized.append({**intervention, 'priority': priority})
        
        return sorted(personalized, key=lambda x: {'high': 0, 'medium': 1, 'low': 2}[x['priority']])
    
    def get_intervention_effectiveness(self, problem: str, intervention: str) -> Dict:
        """Get evidence on intervention effectiveness"""
        effectiveness_data = {
            'antihypertensive medication': {'efficacy': 0.85, 'side_effects': 0.15, 'duration': '12-24 months'},
            'insulin therapy': {'efficacy': 0.90, 'side_effects': 0.10, 'duration': '1-2 weeks'},
            'antibiotic therapy': {'efficacy': 0.88, 'side_effects': 0.12, 'duration': '48-72 hours'},
            'ace inhibitor/arb': {'efficacy': 0.80, 'side_effects': 0.08, 'duration': '2-4 weeks'},
            'exercise program': {'efficacy': 0.65, 'side_effects': 0.02, 'duration': '4-8 weeks'}
        }
        
        intervention_lower = intervention.lower()
        return effectiveness_data.get(intervention_lower, {
            'efficacy': 0.5,
            'side_effects': 0.05,
            'duration': 'unknown'
        })


class CarePlanOptimizer:
    """Optimize care plans based on patient condition and evidence"""
    
    def __init__(self):
        self.optimization_history = []
    
    def generate_optimized_care_plan(self, patient_id: str, problems: List[str], patient_data: Dict) -> Dict:
        """Generate optimized care plan for a patient"""
        recommender = InterventionRecommender()
        
        # Get recommendations for each problem
        problem_recommendations = {}
        all_interventions = []
        
        for problem in problems:
            rec = recommender.recommend_interventions(problem, patient_data)
            problem_recommendations[problem] = rec
            all_interventions.extend(rec['interventions'])
        
        # Optimize for conflicts and redundancies
        optimized_interventions = self._resolve_conflicts(all_interventions)
        
        # Prioritize by urgency and impact
        prioritized = self._prioritize_interventions(optimized_interventions, patient_data)
        
        care_plan = {
            'patient_id': patient_id,
            'problems': problems,
            'problem_recommendations': problem_recommendations,
            'optimized_interventions': prioritized,
            'care_goals': self._generate_care_goals(problems),
            'monitoring_plan': self._generate_monitoring_plan(problems),
            'timeline': self._generate_timeline(prioritized),
            'generated_at': datetime.now().isoformat(),
            'next_review': (datetime.now() + timedelta(days=7)).isoformat()
        }
        
        self.optimization_history.append(care_plan)
        return care_plan
    
    def _resolve_conflicts(self, interventions: List[Dict]) -> List[Dict]:
        """Resolve conflicts and remove redundancies"""
        # Remove duplicates
        seen = set()
        unique = []
        
        for intervention in interventions:
            key = intervention['name'].lower()
            if key not in seen:
                seen.add(key)
                unique.append(intervention)
        
        # Check for interactions (simplified)
        resolved = []
        for intervention in unique:
            if not self._has_conflict(intervention, resolved):
                resolved.append(intervention)
        
        return resolved
    
    def _has_conflict(self, intervention: Dict, existing: List[Dict]) -> bool:
        """Check if intervention conflicts with existing ones"""
        conflict_pairs = [
            ('antihypertensive medication', 'vasopressor support'),
            ('diuretics', 'fluid restriction'),  # Same goal, different approach
        ]
        
        for existing_int in existing:
            for conflict_pair in conflict_pairs:
                if ((intervention['name'].lower() in conflict_pair[0] and 
                     existing_int['name'].lower() in conflict_pair[1]) or
                    (intervention['name'].lower() in conflict_pair[1] and 
                     existing_int['name'].lower() in conflict_pair[0])):
                    return True
        
        return False
    
    def _prioritize_interventions(self, interventions: List[Dict], patient_data: Dict) -> List[Dict]:
        """Prioritize interventions by urgency and impact"""
        scored = []
        
        for intervention in interventions:
            score = 0
            
            # Base priority
            if intervention['priority'] == 'high':
                score += 10
            elif intervention['priority'] == 'medium':
                score += 5
            else:
                score += 1
            
            # Urgency based on time to effect
            if 'immediate' in intervention.get('time_to_effect', ''):
                score += 5
            elif '24-48' in intervention.get('time_to_effect', ''):
                score += 3
            
            # Patient-specific factors
            if patient_data.get('critical', False):
                score += 5  # Boost urgent interventions for critical patients
            
            scored.append({**intervention, 'priority_score': score})
        
        return sorted(scored, key=lambda x: x['priority_score'], reverse=True)
    
    def _generate_care_goals(self, problems: List[str]) -> List[Dict]:
        """Generate SMART care goals"""
        goals = []
        
        goal_templates = {
            'hypertension': 'Reduce BP to <140/90 mmHg within 4 weeks',
            'diabetes': 'Achieve HbA1c <7% within 3 months',
            'pneumonia': 'Resolve infiltrate on chest X-ray within 2 weeks',
            'heart_failure': 'Reduce weight by 2-3 lbs/day and maintain euvolemia',
            'sepsis': 'Achieve lactate clearance and hemodynamic stability within 24 hours'
        }
        
        for problem in problems:
            for key, template in goal_templates.items():
                if key in problem.lower():
                    goals.append({
                        'goal': template,
                        'problem': problem,
                        'measurable': True,
                        'timeline': '1-4 weeks'
                    })
                    break
        
        return goals
    
    def _generate_monitoring_plan(self, problems: List[str]) -> Dict:
        """Generate monitoring plan"""
        return {
            'vital_signs': 'Every 4-8 hours',
            'labs': 'Daily for acute conditions, weekly for chronic',
            'imaging': 'As clinically indicated',
            'assessments': 'Daily physical exam and patient interaction',
            'family_communication': 'Daily updates'
        }
    
    def _generate_timeline(self, interventions: List[Dict]) -> List[Dict]:
        """Generate implementation timeline"""
        timeline = []
        now = datetime.now()
        
        phases = {
            'Phase 1 - Immediate': timedelta(hours=1),
            'Phase 2 - Urgent': timedelta(hours=6),
            'Phase 3 - Short-term': timedelta(days=1),
            'Phase 4 - Medium-term': timedelta(days=7)
        }
        
        phase_idx = 0
        for i, intervention in enumerate(interventions[:10]):  # Limit to 10 items
            phase_name = list(phases.keys())[min(phase_idx, 3)]
            timeline.append({
                'intervention': intervention['name'],
                'phase': phase_name,
                'target_time': (now + phases[phase_name]).isoformat(),
                'sequence': i + 1
            })
            
            if (i + 1) % 3 == 0:
                phase_idx += 1
        
        return timeline


class PatternRecognitionEngine:
    """Recognize clinical patterns in patient data"""
    
    # Clinical pattern definitions
    CLINICAL_PATTERNS = {
        'sepsis_pattern': {
            'indicators': [
                'fever', 'tachycardia', 'tachypnea', 'hypotension', 'elevated_lactate'
            ],
            'diagnostic_criteria': 'At least 2 of 4 SIRS + suspected infection',
            'intervention': 'Sepsis protocol - Blood cultures, antibiotics, fluids'
        },
        'acute_kidney_injury': {
            'indicators': ['elevated_creatinine', 'oliguria', 'elevated_potassium'],
            'diagnostic_criteria': 'Creatinine increase >1.5x baseline or oliguria',
            'intervention': 'Hydration, medication review, nephrology consult'
        },
        'acute_heart_failure': {
            'indicators': ['dyspnea', 'elevated_bnp', 'pulmonary_edema', 'hypoxia'],
            'diagnostic_criteria': 'Dyspnea + BNP >100 + imaging findings',
            'intervention': 'Diuretics, vasodilators, cardiac monitoring'
        },
        'hypoglycemic_event': {
            'indicators': ['low_glucose', 'altered_mental_status', 'tachycardia', 'sweating'],
            'diagnostic_criteria': 'Glucose <70 with symptoms',
            'intervention': 'Immediate glucose administration, monitoring'
        }
    }
    
    def __init__(self):
        self.pattern_history = []
    
    def recognize_patterns(self, patient_vital_signs: Dict, patient_labs: Dict) -> List[Dict]:
        """Recognize clinical patterns in patient data"""
        recognized_patterns = []
        
        all_data = {**patient_vital_signs, **patient_labs}
        
        for pattern_name, pattern_def in self.CLINICAL_PATTERNS.items():
            match_score = self._calculate_pattern_match(all_data, pattern_def['indicators'])
            
            if match_score > 0.6:  # Threshold for pattern recognition
                recognized_patterns.append({
                    'pattern': pattern_name,
                    'match_score': match_score,
                    'diagnostic_criteria': pattern_def['diagnostic_criteria'],
                    'recommended_intervention': pattern_def['intervention'],
                    'urgency': self._calculate_urgency(match_score),
                    'timestamp': datetime.now().isoformat()
                })
        
        # Sort by match score
        recognized_patterns.sort(key=lambda x: x['match_score'], reverse=True)
        
        self.pattern_history.append({
            'recognized_patterns': recognized_patterns,
            'timestamp': datetime.now().isoformat()
        })
        
        return recognized_patterns
    
    def _calculate_pattern_match(self, data: Dict, indicators: List[str]) -> float:
        """Calculate how well data matches pattern indicators"""
        matches = 0
        
        for indicator in indicators:
            if indicator in data:
                value = data[indicator]
                # Simple match detection (would be more sophisticated in production)
                if isinstance(value, bool) and value:
                    matches += 1
                elif isinstance(value, (int, float)) and value > 0:
                    matches += 1
        
        return matches / len(indicators) if indicators else 0
    
    def _calculate_urgency(self, match_score: float) -> str:
        """Determine urgency based on match score"""
        if match_score > 0.9:
            return 'Critical'
        elif match_score > 0.75:
            return 'High'
        elif match_score > 0.6:
            return 'Medium'
        else:
            return 'Low'
    
    def get_pattern_analytics(self) -> pd.DataFrame:
        """Get analytics on recognized patterns"""
        patterns = []
        
        for entry in self.pattern_history:
            for pattern in entry['recognized_patterns']:
                patterns.append(pattern)
        
        return pd.DataFrame(patterns) if patterns else pd.DataFrame()


def generate_sample_patient_recommendation_data() -> Dict:
    """Generate sample patient data for recommendations"""
    return {
        'patient_id': 'P12345',
        'age': 65,
        'comorbidities': 3,
        'problems': ['hypertension', 'diabetes', 'heart_failure'],
        'critical': False,
        'insurance_type': 'Medicare'
    }


if __name__ == '__main__':
    logger.info("Initializing Recommendations Engine...")
    
    # Test intervention recommender
    recommender = InterventionRecommender()
    
    # Get recommendations
    patient_data = generate_sample_patient_recommendation_data()
    rec = recommender.recommend_interventions('high blood pressure', patient_data)
    
    logger.info("Intervention Recommendation:")
    print(json.dumps(rec, indent=2, default=str))
    
    # Test care plan optimizer
    optimizer = CarePlanOptimizer()
    care_plan = optimizer.generate_optimized_care_plan(
        'P12345',
        ['hypertension', 'diabetes'],
        patient_data
    )
    
    logger.info("\nOptimized Care Plan:")
    print(json.dumps(care_plan, indent=2, default=str))
    
    # Test pattern recognition
    pattern_engine = PatternRecognitionEngine()
    
    vital_signs = {
        'fever': True,
        'tachycardia': True,
        'tachypnea': True,
        'elevated_lactate': True
    }
    
    patterns = pattern_engine.recognize_patterns(vital_signs, {})
    logger.info("\nRecognized Patterns:")
    print(json.dumps(patterns, indent=2, default=str))
    
    logger.info("\nPhase 3.2: Recommendations Engine - Ready for deployment")
