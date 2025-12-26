# GitHub Packages for FHIR Implementation Guide

## What is GitHub Packages?

GitHub Packages is a software package hosting service that allows you to host your software packages privately or publicly and use them as dependencies in your projects. It provides:

- **Unified Platform**: Source code and packages in one place
- **Integrated Permissions**: Uses GitHub's existing access controls
- **Multiple Registries**: Supports npm, Docker, Maven, NuGet, RubyGems
- **Free for Public Repos**: Unlimited bandwidth and storage for public packages

## Current Status

**Your Repository**: Currently has **NO packages published**  
**URL**: https://github.com/ClinyQAi/open-nursing-core-ig/packages

## Why Publish Your FHIR IG as a Package?

### 1. **Standard FHIR Distribution Method**
FHIR Implementation Guides are commonly distributed as **npm packages**. This allows:
- Other developers to install your IG as a dependency: `npm install @cliniqai/open-nursing-core-ig`
- Automated dependency management and versioning
- Integration with FHIR tooling (SUSHI, IG Publisher, validators)

### 2. **Benefits for Your Project**

#### **For Developers**:
- Easy installation: `npm install @cliniqai/open-nursing-core-ig`
- Version management: Pin to specific versions
- Dependency resolution: Automatically pull required dependencies

#### **For Healthcare Organizations**:
- Simplified deployment of your nursing profiles
- Consistent versioning across environments
- Integration with existing FHIR servers (HAPI, Firely, etc.)

#### **For the FHIR Community**:
- Discoverable on npm registry
- Reusable profiles and extensions
- Contributes to NHS/UK FHIR ecosystem

### 3. **What You Can Publish**

Based on your repository structure:

| Package Type | What to Publish | Use Case |
|--------------|-----------------|----------|
| **npm** | FHIR IG package (profiles, extensions, valuesets) | Primary distribution method |
| **Docker** | Containerized IG website + HAPI FHIR server | Easy deployment |
| **npm** | Validation tools (if you create custom validators) | Developer tooling |

## How to Publish Your FHIR IG as an npm Package

### Step 1: Create `package.json` in Root Directory

```json
{
  \"name\": \"@cliniqai/open-nursing-core-ig\",
  \"version\": \"0.1.0\",
  \"description\": \"Open Nursing Core FHIR Implementation Guide - UK Core compliant nursing profiles\",
  \"main\": \"package/package.json\",
  \"files\": [
    \"docs/package.tgz\",
    \"docs/package/**\",
    \"input/**\",
    \"fsh-generated/**\"
  ],
  \"keywords\": [
    \"fhir\",
    \"nursing\",
    \"uk-core\",
    \"nhs\",
    \"implementation-guide\",
    \"hl7\"
  ],
  \"author\": \"ClinyQAi\",
  \"license\": \"Apache-2.0\",
  \"repository\": {
    \"type\": \"git\",
    \"url\": \"https://github.com/ClinyQAi/open-nursing-core-ig.git\"
  },
  \"publishConfig\": {
    \"registry\": \"https://npm.pkg.github.com\"
  },
  \"fhir\": {
    \"canonical\": \"https://fhir.clinyq.ai\",
    \"version\": \"4.0.1\"
  }
}
```

### Step 2: Authenticate with GitHub Packages

Create a Personal Access Token:
1. Go to: https://github.com/settings/tokens
2. Click \"Generate new token (classic)\"
3. Select scopes: `write:packages`, `read:packages`
4. Copy the token

Configure npm:
```bash
# Create/edit ~/.npmrc
echo \"//npm.pkg.github.com/:_authToken=YOUR_TOKEN_HERE\" >> ~/.npmrc
echo \"@cliniqai:registry=https://npm.pkg.github.com\" >> ~/.npmrc
```

### Step 3: Build Your IG

```bash
# Run the FHIR IG Publisher
./_genonce.sh  # or _genonce.bat on Windows

# This generates:
# - docs/package.tgz (the npm package)
# - docs/package/ directory with FHIR resources
```

### Step 4: Publish to GitHub Packages

```bash
# From repository root
npm publish
```

### Step 5: Automate with GitHub Actions

Create `.github/workflows/publish-package.yml`:

```yaml
name: Publish FHIR IG Package

on:
  release:
    types: [published]
  workflow_dispatch:

jobs:
  publish:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          registry-url: 'https://npm.pkg.github.com'
          scope: '@cliniqai'
      
      - name: Build FHIR IG
        run: |
          ./_genonce.sh
      
      - name: Publish to GitHub Packages
        run: npm publish
        env:
          NODE_AUTH_TOKEN: \${{ secrets.GITHUB_TOKEN }}
```

## How Others Would Use Your Package

### Install the Package

```bash
# Configure npm to use GitHub Packages
echo \"@cliniqai:registry=https://npm.pkg.github.com\" >> .npmrc

# Install your IG
npm install @cliniqai/open-nursing-core-ig
```

### Use in FHIR Projects

```javascript
// In a FHIR validator or server
const igPackage = require('@cliniqai/open-nursing-core-ig');

// Access profiles
const newsProfile = igPackage.profiles['ONCore-NEWS2-Observation'];

// Use in HAPI FHIR
// Add as dependency in pom.xml or package.json
```

## Alternative: Publish to Official FHIR Registry

You can also publish to the official FHIR package registry:

1. **Register at**: https://registry.fhir.org
2. **Submit your IG**: After building, submit `docs/package.tgz`
3. **Benefits**: 
   - Listed on official FHIR registry
   - Discoverable by all FHIR tools
   - Part of the global FHIR ecosystem

## Docker Container Publishing

You can also publish a Docker container with your IG:

```dockerfile
# Dockerfile for IG website
FROM nginx:alpine
COPY docs/ /usr/share/nginx/html/
EXPOSE 80
CMD [\"nginx\", \"-g\", \"daemon off;\"]
```

Build and publish:
```bash
# Build
docker build -t ghcr.io/cliniqai/open-nursing-core-ig:latest .

# Login to GitHub Container Registry
echo \$GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin

# Push
docker push ghcr.io/cliniqai/open-nursing-core-ig:latest
```

## Recommended Next Steps

1. ✅ **Create `package.json`** in repository root (see template above)
2. ✅ **Build your IG** to generate `docs/package.tgz`
3. ✅ **Test locally** before publishing
4. ✅ **Publish first version** manually to verify
5. ✅ **Set up GitHub Actions** for automated publishing on releases
6. ✅ **Document installation** in your README.md

## Benefits Summary

| Benefit | Description |
|---------|-------------|
| **Discoverability** | Listed on GitHub and npm registries |
| **Version Control** | Semantic versioning (0.1.0, 0.2.0, 1.0.0) |
| **Dependency Management** | Automatic updates and compatibility |
| **Professional Distribution** | Standard method used by HL7 and NHS Digital |
| **CI/CD Integration** | Automated builds and releases |
| **Community Adoption** | Easier for others to use your profiles |

## Example: How NHS Digital Does It

NHS Digital publishes their FHIR packages:
- **UK Core**: `uk.nhsdigital.r4`
- **Care Connect**: `uk.nhsconnect.r4`

Your package would be:
- **Package Name**: `@cliniqai/open-nursing-core-ig`
- **Canonical URL**: `https://fhir.clinyq.ai`
- **Version**: Following semantic versioning

## Questions?

- **Cost**: Free for public repositories
- **Storage**: Unlimited for public packages
- **Bandwidth**: Unlimited for public packages
- **Private Packages**: Included in GitHub Pro/Team plans

---

**Ready to publish?** Start with Step 1 above and create your `package.json` file!
