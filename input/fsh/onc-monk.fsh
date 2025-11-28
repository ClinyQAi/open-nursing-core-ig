// 1. Define the Monk Scale CodeSystem
CodeSystem: ONCMonkScale
Id: onc-monk-scale
Title: "Monk Skin Tone Scale"
Description: "The Monk Skin Tone (MST) Scale is a 10-shade scale designed to represent a broader range of skin tones for AI and equity applications."
* ^url = "https://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-monk-scale"
* ^caseSensitive = true
* #MST-01 "Monk Scale 01" "Lightest skin tone"
* #MST-02 "Monk Scale 02"
* #MST-03 "Monk Scale 03"
* #MST-04 "Monk Scale 04"
* #MST-05 "Monk Scale 05" "Medium skin tone"
* #MST-06 "Monk Scale 06"
* #MST-07 "Monk Scale 07"
* #MST-08 "Monk Scale 08"
* #MST-09 "Monk Scale 09"
* #MST-10 "Monk Scale 10" "Darkest skin tone"

// 2. Define the ValueSet (All codes from the system)
ValueSet: ONCMonkScaleVS
Id: onc-monk-scale-vs
Title: "Monk Skin Tone Scale Value Set"
Description: "Codes representing the 10-point Monk Skin Tone Scale."
* include codes from system ONCMonkScale

// 3. Define the Observation Profile
Profile: ONCMonkSkinToneObservation
Parent: Observation
Id: onc-monk-skintone-observation
Title: "Monk Skin Tone Observation"
Description: "An observation of visual skin tone using the Monk Skin Tone (MST) scale. This is distinct from UV-reactivity scales (like Fitzpatrick) and is used primarily for equity, representation, and AI fairness applications."
* code = http://clinyqai.github.io/open-nursing-core-ig/CodeSystem/onc-observation-codes#mst-score
* subject 1..1
* subject only Reference(Patient)
* value[x] only CodeableConcept
* valueCodeableConcept from ONCMonkScaleVS (required)
* valueCodeableConcept ^short = "The selected Monk Scale tone (MST-01 to MST-10)"
