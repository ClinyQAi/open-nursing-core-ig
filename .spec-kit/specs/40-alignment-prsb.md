# Spec 40: PRSB Alignment Matrix

## Status
- [x] Specify
- [ ] Plan
- [ ] Tasks
- [ ] Implement

## Clinical Context
The **Professional Record Standards Body (PRSB)** published the **Nursing Care Needs Standard v1.0** in February 2024. This is the UK's official logical model for structured nursing documentation.

To gain credibility and NHS adoption, the ONC-IG must demonstrate formal alignment with PRSB requirements.

## The Problem
- ONC-IG exists as an independent initiative
- No formal mapping to PRSB logical model
- NHS Trusts hesitant to adopt without PRSB alignment
- Potential duplicate effort with UK Core

## The Solution
Create a formal **Conformance Matrix** mapping every PRSB requirement to an ONC-IG profile, with gap analysis and remediation plan.

---

## PRSB Nursing Care Needs Standard - Domains

### 1. Eating and Drinking
| PRSB Element | ONC-IG Profile | Status |
|--------------|----------------|--------|
| Nutritional screening | ONCMUSTScore | ✅ Covered |
| Oral intake assessment | ONCOralIntakeAssessment | ⚠️ Gap |
| Swallowing assessment | ONCSwallowingAssessment | ⚠️ Gap |
| Dietary requirements | ONCDietaryRequirements | ⚠️ Gap |
| Assistance required | ONCCarePlan.activity | ✅ Covered |

### 2. Mobility
| PRSB Element | ONC-IG Profile | Status |
|--------------|----------------|--------|
| Mobility assessment | ONCMobility | ⚠️ Gap |
| Falls risk | ONCMorseFallScale | ✅ Covered |
| Moving and handling needs | ONCCarePlan.activity | ✅ Covered |
| Mobility aids | ONCDeviceUse | ⚠️ Gap |

### 3. Elimination
| PRSB Element | ONC-IG Profile | Status |
|--------------|----------------|--------|
| Continence status | ONCContinenceAssessment | ⚠️ Gap |
| Bladder function | ONCBladderAssessment | ⚠️ Gap |
| Bowel function | ONCBowelAssessment | ⚠️ Gap |
| Catheter care | ONCCatheterCare | ⚠️ Gap |

### 4. Personal Hygiene
| PRSB Element | ONC-IG Profile | Status |
|--------------|----------------|--------|
| Hygiene needs | ONCHygieneAssessment | ⚠️ Gap |
| Oral care | ONCOralCareAssessment | ⚠️ Gap |
| Bathing assistance | ONCCarePlan.activity | ✅ Covered |

### 5. Skin Integrity
| PRSB Element | ONC-IG Profile | Status |
|--------------|----------------|--------|
| Pressure ulcer risk | ONCBradenScale, ONCWaterlowScore | ✅ Covered |
| Skin assessment | ONCWoundAssessment | ✅ Covered |
| Skin tone context | ONCEquitySkinTone | ✅ **Superior** |
| Wound care plan | ONCCarePlan | ✅ Covered |

### 6. Medication Self-Management
| PRSB Element | ONC-IG Profile | Status |
|--------------|----------------|--------|
| Medication ability | ONCMedicationAbility | ⚠️ Gap |
| Self-admin assessment | ONCMedicationSelfAdmin | ⚠️ Gap |
| Compliance factors | ONCCarePlan | ✅ Covered |

---

## Gap Analysis Summary

| Domain | PRSB Elements | ONC-IG Covered | Gap Count |
|--------|---------------|----------------|-----------|
| Eating/Drinking | 5 | 2 | 3 |
| Mobility | 4 | 2 | 2 |
| Elimination | 4 | 0 | 4 |
| Personal Hygiene | 3 | 1 | 2 |
| Skin Integrity | 4 | 4 | 0 |
| Medication | 3 | 1 | 2 |
| **TOTAL** | **23** | **10** | **13** |

### Coverage: 43% → Target: 100%

---

## Remediation Plan

### Priority 1: Elimination Domain (High Clinical Impact)
```yaml
New Profiles Required:
  - ONCContinenceAssessment
  - ONCBladderAssessment  
  - ONCBowelAssessment
  - ONCCatheterCare

Timeline: Q1 2026
Dependencies: SNOMED CT UK Clinical Extension codes
```

### Priority 2: Eating/Drinking Domain
```yaml
New Profiles Required:
  - ONCOralIntakeAssessment
  - ONCSwallowingAssessment
  - ONCDietaryRequirements

Timeline: Q1 2026
Dependencies: Align with BDA (British Dietetic Association) standards
```

### Priority 3: Mobility Domain
```yaml
New Profiles Required:
  - ONCMobility
  - ONCDeviceUse (for mobility aids)

Timeline: Q2 2026
Dependencies: Align with CSP (Chartered Society of Physiotherapy)
```

---

## UK Core Mapping

| ONC-IG Profile | UK Core Base Profile | Extension Required |
|----------------|----------------------|-------------------|
| ONCBradenScale | UKCore-Observation | No |
| ONCNursingGoal | UKCore-Goal | No |
| ONCCarePlan | UKCore-CarePlan | ONC-equity-context |
| ONCEquitySkinTone | UKCore-Observation | ONC-mandatory-invariant |

---

## Formal Endorsement Strategy

### Step 1: PRSB Submission
- Submit ONC-IG to PRSB as "candidate implementation"
- Request formal review against Nursing Care Needs Standard
- Address any conformance gaps raised

### Step 2: Royal College Engagement
- Present to RCN (Royal College of Nursing) Digital Nursing Forum
- Request clinical endorsement
- Incorporate feedback into v1.1

### Step 3: NHS Digital Review
- Submit to UK Core governance for inclusion consideration
- Propose equity extensions as UK Core additions
- Align versioning with NHS release cycles

---

## Success Metrics
- [ ] 100% PRSB elements have ONC-IG coverage
- [ ] Formal PRSB alignment statement obtained
- [ ] UK Core compatibility verified
- [ ] At least 2 NHS Trusts agree to pilot

---

## References
- PRSB: Nursing Care Needs Standard v1.0 (February 2024)
- NHS Digital: FHIR UK Core Implementation Guide
- RCN: Digital Nursing Strategy
