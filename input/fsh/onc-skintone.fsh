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

Profile: ONCMonkSkinToneObservation
Parent: Observation
Id: onc-monk-skintone-observation
Title: "ONC Monk Skin Tone Observation"
Description: "Observation for Monk Skin Tone (MST) to support equity in assessment interpretation, providing better representation for darker skin tones than Fitzpatrick."
* code = ONCObservationCodes#mst-score "Monk Skin Tone Scale Score"
* code MS
* value[x] only CodeableConcept
* valueCodeableConcept 1..1 MS
