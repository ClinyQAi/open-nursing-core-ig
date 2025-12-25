# Contributing to Open Nursing Core IG

Thank you for your interest in contributing to the Open Nursing Core FHIR Implementation Guide! This project is a nurse-led, open-source initiative to standardize nursing documentation using HL7 FHIR.

## 🎯 Ways to Contribute

### 1. Report Issues
- **Bug Reports**: If you find validation errors or issues with the profiles
- **Feature Requests**: Suggest new profiles, extensions, or terminology
- **Documentation**: Help improve documentation or fix typos

### 2. Submit Pull Requests
- **New Profiles**: Add FHIR profiles for nursing assessments
- **Terminology**: Expand ValueSets and CodeSystems
- **Examples**: Add example instances for testing

### 3. Clinical Review
- **Validate clinical accuracy** of nursing concepts
- **Review LOINC/SNOMED code selections**
- **Suggest improvements** based on nursing practice

---

## 🔧 Development Setup

### Prerequisites
```bash
# Install Node.js (https://nodejs.org/)
# Install SUSHI
npm install -g fsh-sushi
```

### Build Locally
```bash
git clone https://github.com/ClinyQAi/open-nursing-core-ig.git
cd open-nursing-core-ig
sushi .
```

---

## 📝 Contribution Guidelines

### FHIR Shorthand (FSH)
- Follow [FSH Best Practices](https://fshschool.org/docs/best-practices/)
- Use descriptive names for profiles and extensions
- Include proper cardinality and constraints
- Add examples for all new profiles

### Terminology
- Use standard terminologies when available (LOINC, SNOMED CT)
- Document rationale for code selections
- Include display names with all codes

### Commit Messages
Use clear, descriptive commit messages:
```
feat: Add NEWS2 observation profile
fix: Correct Braden scale LOINC codes
docs: Update README with IG links
```

---

## 🔍 Code Review Process

1. **Fork** the repository
2. **Create a branch** for your feature (`git checkout -b feature/new-profile`)
3. **Make changes** and commit
4. **Run SUSHI** to validate (`sushi .`)
5. **Submit a Pull Request**

All PRs will be reviewed for:
- ✅ FSH syntax correctness
- ✅ Clinical accuracy
- ✅ Alignment with existing profiles
- ✅ Proper terminology usage

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## 📬 Questions?

- Open an [Issue](https://github.com/ClinyQAi/open-nursing-core-ig/issues)
- Review existing [Discussions](https://github.com/ClinyQAi/open-nursing-core-ig/discussions)

Thank you for helping advance nursing informatics! 🩺
