### FHIR Profiles

This Implementation Guide defines the following FHIR profiles to represent the nursing process:

#### Assessment Phase

**ONCNursingAssessment**
- Base profile for all nursing observations and assessments
- Mandates a nurse performer and nursing category
- Supports both CodeableConcept and Quantity values

**ONCBradenScaleAssessment**
- Specialized profile for Braden Scale pressure injury risk assessment
- Includes six required components: sensory perception, moisture, activity, mobility, nutrition, and friction/shear
- Uses LOINC code 9017-7 for the total score

#### Diagnosis Phase

**ONCNursingProblem**
- Based on FHIR Condition resource
- Represents a clinical judgment about a human response to a health condition
- Uses ICNP and SNOMED CT codes from the Nursing Problem ValueSet

#### Planning Phase

**ONCPatientGoal**
- Based on FHIR Goal resource
- Represents desired patient outcomes
- Must reference at least one ONCNursingProblem

#### Intervention Phase

**ONCNursingIntervention**
- Based on FHIR Procedure resource
- Represents actions performed by nurses
- Uses ICNP and SNOMED CT codes from the Nursing Intervention ValueSet
- Can reference goals as the reason for the intervention

#### Evaluation Phase

**ONCGoalEvaluation**
- Specialized observation for evaluating goal progress
- Must reference the goal(s) being evaluated
- Uses codes indicating achievement status

#### Care Plan

**ONCNursingCarePlan**
- Based on FHIR CarePlan resource
- Orchestrates the entire nursing process
- Links problems, goals, and interventions into a cohesive care plan