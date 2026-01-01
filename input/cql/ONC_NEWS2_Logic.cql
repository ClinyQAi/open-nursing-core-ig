library ONC_NEWS2_Logic version '1.0.0'

using FHIR version '4.0.1'

include FHIRHelpers version '4.0.1'

// =============================================================================
// ONC NEWS2 Logic
// National Early Warning Score 2 Auto-Calculation
// =============================================================================

codesystem "LOINC": 'http://loinc.org'
codesystem "SNOMED": 'http://snomed.info/sct'

// Codes
code "RespRateCode": '9279-1' from "LOINC"
code "O2SatCode": '59408-5' from "LOINC"
code "AirOrOxygenCode": '722742002' from "SNOMED" // Breathing room air (finding)
code "SupplementalOxygenCode": '371825009' from "SNOMED" // Oxygen therapy (procedure)
code "SibpCode": '8480-6' from "LOINC"
code "HeartRateCode": '8867-4' from "LOINC"
code "BodyTempCode": '8310-5' from "LOINC"
code "ACVPUCode": '1104441000000107' from "SNOMED" // ACVPU Scale

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
// 2. Oxygen Saturation (SpO2) - Scale 1 (Default)
// =============================================================================
define "Most Recent SpO2":
  Last([Observation: "O2SatCode"] O
    where O.status = 'final'
    sort by effective.as(dateTime))

define "SpO2 Score Scale 1":
  case
    when "Most Recent SpO2".value.as(Quantity).value <= 91 then 3
    when "Most Recent SpO2".value.as(Quantity).value between 92 and 93 then 2
    when "Most Recent SpO2".value.as(Quantity).value between 94 and 95 then 1
    when "Most Recent SpO2".value.as(Quantity).value >= 96 then 0
    else null
  end

// =============================================================================
// 3. Air or Oxygen
// =============================================================================
// Need appropriate Observation code for Air/Oxygen status. 
// Assuming a custom observation or generic finding for now.
// For rigorous implementation, this requires a specific profile.

define "Air Oxygen Score":
  0 // Placeholder - defaulting to 0 for compilation safety in draft

// =============================================================================
// 4. Systolic Blood Pressure
// =============================================================================
define "Most Recent SBP":
  Last([Observation: "SibpCode"] O
    where O.status = 'final'
    sort by effective.as(dateTime))

define "SBP Score":
  case
    when "Most Recent SBP".value.as(Quantity).value <= 90 then 3
    when "Most Recent SBP".value.as(Quantity).value between 91 and 100 then 2
    when "Most Recent SBP".value.as(Quantity).value between 101 and 110 then 1
    when "Most Recent SBP".value.as(Quantity).value between 111 and 219 then 0
    when "Most Recent SBP".value.as(Quantity).value >= 220 then 3
    else null
  end

// =============================================================================
// 5. Pulse
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
define "Consciousness Score":
  0 // Placeholder

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
// Total Score
// =============================================================================
define "NEWS2 Total Score":
  Coalesce("Respiration Rate Score", 0)
  + Coalesce("SpO2 Score Scale 1", 0)
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
