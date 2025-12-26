# NHS NEWS2 Alignment Strategy

## Overview
The NHS CareConnect NEWS2 profiles are the **official NHS standard** for NEWS2 documentation. We should align with their approach while maintaining our unified "Open Nursing Core" philosophy.

## NHS CareConnect NEWS2 Structure

### Core Profiles
1. **`CareConnect-NEWS2-Observation-1`** - Overall NEWS2 score (0-20)
   - **SNOMED Code**: `1104051000000101` (National Early Warning Score 2)
   - **LOINC Code**: `88330-6` (National Early Warning Score [NEWS])
   - Status: Fixed to `#final`
   - Contains optional sub-scores

2. **`CareConnect-Subscore-Observation-1`** - Individual parameter scores
   - One per observation (respiration, oxygen, temperature, etc.)
   - References the related observation via `Observation.related`

3. **Supporting Observation Profiles**:
   - `CareConnect-HeartRate-Observation-1` (Pulse rate)
   - `CareConnect-BloodPressure-Observation-1` (Systolic BP)
   - `CareConnect-BodyTemperature-Observation-1`
   - `CareConnect-OxygenSaturation-Observation-1`
   - `CareConnect-InspiredOxygen-Observation-1`
   - `CareConnect-ACVPU-Observation-1` (Consciousness level)

### Message Design Flexibility
NHS allows 3 levels of detail:
1. **Full**: NEWS2 score + sub-scores + observations (recommended)
2. **Medium**: NEWS2 score + observations only
3. **Minimal**: NEWS2 score only

## 🎯 Recommended Alignment Strategy

### Option A: **Pragmatic Hybrid** (RECOMMENDED)
**Keep your current simple profile for the validator, but document NHS compatibility**

**Pros:**
- ✅ Validator stays simple and focused
- ✅ Easier for "Citizen Developers" to understand
- ✅ Still compatible with NHS if you add mapping documentation
- ✅ Can evolve to full NHS compatibility later

**Implementation:**
1. Keep `ONCNEWS2Score` as-is (simple total score validation)
2. Add a **compatibility note** in the profile description
3. Create an **optional extension profile** `ONCNEWS2ScoreExtended` that includes sub-scores
4. Document how to map between ONC and NHS CareConnect

**FSH Example:**
```fsh
Profile: ONCNEWS2Score
Parent: ONCNursingAssessment
Id: onc-news2-score
Title: "NEWS2 Score (Simple)"
Description: "National Early Warning Score 2 total score (0-20). Compatible with NHS CareConnect-NEWS2-Observation-1. For full sub-score detail, see ONCNEWS2ScoreExtended."
* code from NEWS2CodeValueSet (required)
* valueQuantity.value obeys news2-range

ValueSet: NEWS2CodeValueSet
* http://loinc.org#88330-6 "National Early Warning Score [NEWS]"
* http://snomed.info/sct#1104051000000101 "National Early Warning Score 2"
```

### Option B: **Full NHS Alignment**
**Replicate the entire NHS CareConnect structure**

**Pros:**
- ✅ 100% NHS compatible
- ✅ Supports full clinical detail
- ✅ Future-proof for NHS integration

**Cons:**
- ❌ Much more complex
- ❌ Requires 7+ profiles instead of 1
- ❌ Harder for beginners

### Option C: **Minimal Change**
**Just add the SNOMED code to your existing profile**

**Pros:**
- ✅ Easiest
- ✅ Minimal disruption

**Cons:**
- ❌ Not fully NHS compatible
- ❌ Misses the sub-score structure

## 💡 My Recommendation: **Option A (Pragmatic Hybrid)**

### Immediate Actions:
1. ✅ Add SNOMED code `1104051000000101` to your NEWS2 profile
2. ✅ Update description to mention NHS CareConnect compatibility
3. ✅ Keep the simple structure for now
4. 📝 Document the mapping in a "Compatibility Guide"

### Future Enhancement (Phase 2):
1. Create `ONCNEWS2ScoreExtended` profile with sub-scores
2. Add the 6 supporting observation profiles
3. Provide examples showing both simple and extended usage

## Implementation Plan

### Step 1: Update Current NEWS2 Profile
```fsh
Profile: ONCNEWS2Score
Parent: ONCNursingAssessment
Id: onc-news2-score
Title: "NEWS2 Score"
Description: "National Early Warning Score 2 (NEWS2) for detecting clinical deterioration. Compatible with NHS CareConnect-NEWS2-Observation-1 (minimal mode). Supports total score validation (0-20)."
* status = #final
* status MS
* code from NEWS2CodeValueSet (required)  // Now includes both LOINC and SNOMED
* code MS
* value[x] only Quantity
* valueQuantity 1..1 MS
* valueQuantity.value obeys news2-range
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"

ValueSet: NEWS2CodeValueSet
Id: news2-code-vs
Title: "NEWS2 Code Value Set"
Description: "LOINC and SNOMED codes for NEWS2"
* http://loinc.org#88330-6 "National Early Warning Score [NEWS]"
* http://snomed.info/sct#1104051000000101 "National Early Warning Score 2 (observable entity)"
```

### Step 2: Create Compatibility Documentation
Add a page to your IG explaining:
- How ONC-IG relates to NHS CareConnect
- Mapping table between the two
- When to use simple vs. extended profiles

### Step 3: Validator Update
Update the validator to accept EITHER:
- LOINC `88330-6` (current)
- SNOMED `1104051000000101` (NHS standard)

## Key Differences to Note

| Aspect | ONC-IG (Current) | NHS CareConnect | Recommendation |
|--------|------------------|-----------------|----------------|
| **Code System** | LOINC only | SNOMED preferred | Support both |
| **Structure** | Simple (total only) | Complex (with sub-scores) | Start simple, extend later |
| **Status** | Any final status | Fixed to `#final` | Keep flexible |
| **Components** | None | 6 sub-scores | Optional extension |

## Benefits of This Approach

1. **Backward Compatible**: Existing validator code still works
2. **NHS Compatible**: Can accept NHS-formatted data
3. **Scalable**: Easy to add extended profile later
4. **Educational**: Simple version teaches the concept, extended shows real-world complexity
5. **Pragmatic**: Balances standards compliance with usability

## Next Steps

Would you like me to:
- **A)** Implement Option A (add SNOMED code, keep simple structure)
- **B)** Implement Option B (full NHS alignment with all sub-scores)
- **C)** Just document the differences without changing code yet
