library ONC_NEWS2_Logic version '1.0.0'

using FHIR version '4.0.1'

include FHIRHelpers version '4.0.1'

// =============================================================================
// ONC NEWS2 Logic (Super-Gold Edition)
// National Early Warning Score 2 Auto-Calculation with Scale 2 Logic
// =============================================================================

codesystem "LOINC": 'http://loinc.org'
codesystem "SNOMED": 'http://snomed.info/sct'
codesystem "ONCObservationCodes": 'https://opennursingcoreig.com/CodeSystem/onc-observation-codes'

// -----------------------------------------------------------------------------
// CODES & TERMINOLOGY
// -----------------------------------------------------------------------------

// Vitals Codes
code "RespRateCode": '9279-1' from "LOINC"
code "O2SatCode": '59408-5' from "LOINC" // SpO2
code "InspiredOxygenCode": '3151-8' from "LOINC" // Inhaled oxygen flow rate
code "BPPanelCode": '85354-9' from "LOINC" // BP Panel
code "SystolicBPComponent": '8480-6' from "LOINC" // Systolic component
code "HeartRateCode": '8867-4' from "LOINC"
code "BodyTempCode": '8310-5' from "LOINC"
code "ACVPUCode": '1104441000000107' from "SNOMED" // ACVPU Scale

// Air / Oxygen Values (from InspiredOxygenValueSet)
code "BreathingRoomAir": '722742002' from "SNOMED"
code "PatientOnOxygen": '371825009' from "SNOMED"

// Consciousness Values (from ACVPUValueSet)
code "MentallyAlert": '248234008' from "SNOMED"

// Conditions for Scale 2 (Hypercapnic Respiratory Failure)
code "COPD": '13645005' from "SNOMED"
code "Hypercapnia": '389087006' from "SNOMED"

context Patient

// =============================================================================
// 1. Respiration Rate
// =============================================================================
define "Most Recent Respiration Rate":
    Last([Observation: "RespRateCode"] O
        where O.status = 'final'
        sort by effective.as(dateTime))

define "Respiration Rate Score":
    case
        when "Most Recent Respiration Rate".value.as(Quantity).value <= 8 then 3
        when "Most Recent Respiration Rate".value.as(Quantity).value between 9 and 11 then 1
        when "Most Recent Respiration Rate".value.as(Quantity).value between 12 and 20 then 0
        when "Most Recent Respiration Rate".value.as(Quantity).value between 21 and 24 then 2
        when "Most Recent Respiration Rate".value.as(Quantity).value >= 25 then 3
        else null
    end

// =============================================================================
// 2. Air or Oxygen (Used in SpO2 Logic)
// =============================================================================
define "Most Recent Inspired Oxygen":
    Last([Observation: "InspiredOxygenCode"] O
        where O.status = 'final'
        sort by effective.as(dateTime))

define "Is On Oxygen":
    // Check if value is CodeableConcept 'PatientOnOxygen' OR quantity > 0
    ("Most Recent Inspired Oxygen".value.as(CodeableConcept) ~ "PatientOnOxygen")
    or
    ("Most Recent Inspired Oxygen".value.as(Quantity).value > 0)

define "Air Oxygen Score":
    if "Is On Oxygen" then 2 else 0

// =============================================================================
// 3. Oxygen Saturation (SpO2) - Dual Scale Logic
// =============================================================================
define "Most Recent SpO2":
    Last([Observation: "O2SatCode"] O
        where O.status = 'final'
        sort by effective.as(dateTime))

// SCALE 1 (Default)
define "SpO2 Score Scale 1":
    case
        when "Most Recent SpO2".value.as(Quantity).value <= 91 then 3
        when "Most Recent SpO2".value.as(Quantity).value between 92 and 93 then 2
        when "Most Recent SpO2".value.as(Quantity).value between 94 and 95 then 1
        when "Most Recent SpO2".value.as(Quantity).value >= 96 then 0
        else null
    end

// SCALE 2 (High Risk / Hypercapnic - Targeted 88-92%)
define "SpO2 Score Scale 2":
    case
        when "Most Recent SpO2".value.as(Quantity).value <= 83 then 3
        when "Most Recent SpO2".value.as(Quantity).value between 84 and 85 then 2
        when "Most Recent SpO2".value.as(Quantity).value between 86 and 87 then 1
        when "Most Recent SpO2".value.as(Quantity).value between 88 and 92 then 0 // Target Range
        when "Most Recent SpO2".value.as(Quantity).value between 93 and 94 then 1
        when "Most Recent SpO2".value.as(Quantity).value between 95 and 96 then 2
        when "Most Recent SpO2".value.as(Quantity).value >= 97 then 
            if "Is On Oxygen" then 3 else 0 // Only unsafe if on O2
        else null
    end

// Logic to determine if Scale 2 applies (COPD/Hypercapnia Diagnosis)
define "Has Hypercapnic Risk":
    exists([Condition: "COPD"]) or exists([Condition: "Hypercapnia"])

define "Selected SpO2 Score":
    if "Has Hypercapnic Risk" then "SpO2 Score Scale 2" else "SpO2 Score Scale 1"

// =============================================================================
// 4. Systolic Blood Pressure (Extraction Logic)
// =============================================================================
define "Most Recent BP Panel":
    Last([Observation: "BPPanelCode"] O
        where O.status = 'final'
        sort by effective.as(dateTime))

define "Systolic BP Value":
    // Extract component where code matches SystolicBPComponent
    singleton from (
        "Most Recent BP Panel".component C
        where C.code ~ "SystolicBPComponent"
        return C.value.as(Quantity).value
    )

define "SBP Score":
    case
        when "Systolic BP Value" <= 90 then 3
        when "Systolic BP Value" between 91 and 100 then 2
        when "Systolic BP Value" between 101 and 110 then 1
        when "Systolic BP Value" between 111 and 219 then 0
        when "Systolic BP Value" >= 220 then 3
        else null
    end

// =============================================================================
// 5. Pulse (Heart Rate)
// =============================================================================
define "Most Recent Pulse":
    Last([Observation: "HeartRateCode"] O
        where O.status = 'final'
        sort by effective.as(dateTime))

define "Pulse Score":
    case
        when "Most Recent Pulse".value.as(Quantity).value <= 40 then 3
        when "Most Recent Pulse".value.as(Quantity).value between 41 and 50 then 1
        when "Most Recent Pulse".value.as(Quantity).value between 51 and 90 then 0
        when "Most Recent Pulse".value.as(Quantity).value between 91 and 110 then 1
        when "Most Recent Pulse".value.as(Quantity).value between 111 and 130 then 2
        when "Most Recent Pulse".value.as(Quantity).value >= 131 then 3
        else null
    end

// =============================================================================
// 6. Consciousness (ACVPU)
// =============================================================================
define "Most Recent Consciousness":
    Last([Observation: "ACVPUCode"] O
        where O.status = 'final'
        sort by effective.as(dateTime))

define "Consciousness Score":
    if "Most Recent Consciousness".value.as(CodeableConcept) ~ "MentallyAlert" then 0
    else 3 // Any other state (Confusion, Voice, Pain, Unresponsive) is Scored 3

// =============================================================================
// 7. Temperature
// =============================================================================
define "Most Recent Temp":
    Last([Observation: "BodyTempCode"] O
        where O.status = 'final'
        sort by effective.as(dateTime))

define "Temp Score":
    case
        when "Most Recent Temp".value.as(Quantity).value <= 35.0 then 3
        when "Most Recent Temp".value.as(Quantity).value between 35.1 and 36.0 then 1
        when "Most Recent Temp".value.as(Quantity).value between 36.1 and 38.0 then 0
        when "Most Recent Temp".value.as(Quantity).value between 38.1 and 39.0 then 1
        when "Most Recent Temp".value.as(Quantity).value >= 39.1 then 2
        else null
    end

// =============================================================================
// Total Score & Risk Category
// =============================================================================
define "NEWS2 Total Score":
    Coalesce("Respiration Rate Score", 0)
    + Coalesce("Selected SpO2 Score", 0)
    + Coalesce("Air Oxygen Score", 0)
    + Coalesce("SBP Score", 0)
    + Coalesce("Pulse Score", 0)
    + Coalesce("Consciousness Score", 0)
    + Coalesce("Temp Score", 0)

define "Clinical Risk Category":
    case
        when "NEWS2 Total Score" >= 7 then 'High'
        when "NEWS2 Total Score" >= 5 then 'Medium'
        when "NEWS2 Total Score" >= 1 then 'Low'
        else 'Low'
    end
