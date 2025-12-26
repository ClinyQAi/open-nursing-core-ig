# Security Policy

## Supported Versions

We actively maintain the latest version of the Open Nursing Core Implementation Guide.

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via GitHub Security Advisories:

1. **GitHub Security Advisories** (Preferred):
   - Go to https://github.com/ClinyQAi/open-nursing-core-ig/security/advisories/new
   - Provide a detailed description of the vulnerability
   - Include steps to reproduce if applicable

### What to Include

- Type of vulnerability
- Full paths of affected source files
- Location of the affected code (tag/branch/commit)
- Step-by-step instructions to reproduce
- Proof-of-concept or exploit code (if possible)
- Impact assessment

### Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Fix Timeline**: Depends on severity
  - Critical: 7 days
  - High: 30 days
  - Medium: 60 days
  - Low: 90 days

## Security Best Practices for Contributors

1. **Never commit secrets**: Use GitHub Secrets for sensitive data
2. **Review dependencies**: Check third-party Actions before use
3. **Sign commits**: Consider using GPG signing for verified commits
4. **Keep dependencies updated**: Monitor Dependabot alerts
5. **Follow least privilege**: Request only necessary permissions in workflows

## Disclosure Policy

We follow coordinated disclosure:
1. Vulnerability is reported privately
2. We confirm and develop a fix
3. Fix is released
4. Public disclosure 30 days after fix release

## Security Features

This repository uses:
- ✅ **CodeQL Scanning**: Automated code security analysis
- ✅ **Secret Scanning**: Prevents accidental credential commits
- ✅ **Dependabot Alerts**: Monitors dependency vulnerabilities
- ✅ **Branch Protection**: Requires review before merging to main

Thank you for helping keep the Open Nursing Core IG secure!
