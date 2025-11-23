Profile: ONCSkinToneObservation
Parent: Observation
Id: onc-skintone-observation
Title: "ONC Skin Tone Observation"
Description: "Observation for Fitzpatrick Skin Type to support equity in assessment interpretation."
* code = http://loinc.org#66472-2 "Fitzpatrick skin type"
* code MS
* value[x] only CodeableConcept
* valueCodeableConcept from SkinToneVS (required)
* valueCodeableConcept 1..1 MS

ValueSet: SkinToneVS
Id: skintone-vs
Title: "Fitzpatrick Skin Tone Value Set"
Description: "Values for Fitzpatrick Skin Type I-VI using standard SNOMED CT codes."
* http://snomed.info/sct#403153005 "Fitzpatrick skin type I"
* http://snomed.info/sct#403154004 "Fitzpatrick skin type II"
* http://snomed.info/sct#403155003 "Fitzpatrick skin type III"
* http://snomed.info/sct#403156002 "Fitzpatrick skin type IV"
* http://snomed.info/sct#403157006 "Fitzpatrick skin type V"
* http://snomed.info/sct#403158001 "Fitzpatrick skin type VI"
