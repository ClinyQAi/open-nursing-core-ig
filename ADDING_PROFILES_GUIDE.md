# Adding Clinical Profiles to the Open Nursing Core IG

## What I Just Created

I've added a new FSH file with three clinical assessment profiles:
- **NEWS2 Score** (National Early Warning Score 2)
- **Pain Assessment** (Numeric Rating Scale 0-10)
- **Wound Assessment** (Pressure ulcer staging and dimensions)

**File Location**: `input/fsh/onc-clinical-assessments.fsh`

## How to Build and Publish the IG

### Step 1: Install SUSHI (if not already installed)
```bash
npm install -g fsh-sushi
```

### Step 2: Build the Implementation Guide
Navigate to the `open-nursing-core-ig` directory and run:

```bash
cd c:\Users\g0226\OneDrive\Desktop\fhir-git\open-nursing-core-ig

# Download the HL7 FHIR IG Publisher (if needed)
./_updatePublisher.sh  # or .bat on Windows

# Run SUSHI to compile FSH files
sushi .

# Build the full IG
./_genonce.sh  # or .bat on Windows
```

### Step 3: Review the Output
After building, the IG will be in the `output/` directory. Open `output/index.html` in a browser to preview.

### Step 4: Commit and Push to GitHub
```bash
git add input/fsh/onc-clinical-assessments.fsh
git commit -m "feat: Add NEWS2, Pain Assessment, and Wound Assessment profiles"
git push
```

### Step 5: GitHub Pages will Auto-Publish
If you have GitHub Actions set up, the IG will automatically rebuild and publish to:
https://clinyqai.github.io/open-nursing-core-ig/

## What Gets Generated

The SUSHI/IG Publisher will create:
- **StructureDefinitions**: Formal FHIR profile definitions
- **ValueSets**: Code systems for wound stages and pain codes
- **HTML Documentation**: Human-readable pages for each profile
- **JSON/XML**: Machine-readable profile files

## Linking the Validator to the IG

Once the IG is published, you can update the validator's README to reference the official profiles:

```markdown
This validator enforces the profiles defined in the [Open Nursing Core IG](https://clinyqai.github.io/open-nursing-core-ig/):
- [NEWS2 Score](https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition-onc-news2-score.html)
- [Pain Assessment](https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition-onc-pain-assessment.html)
- [Wound Assessment](https://clinyqai.github.io/open-nursing-core-ig/StructureDefinition-onc-wound-assessment.html)
```

## Next Steps

1. **Build the IG** to verify the FSH compiles correctly
2. **Review the generated profiles** in the output
3. **Push to GitHub** to trigger auto-publishing
4. **Update the validator** to reference the official IG URLs instead of placeholder URLs
