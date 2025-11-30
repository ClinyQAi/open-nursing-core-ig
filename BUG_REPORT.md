# Bug Report: Open Nursing Core

## High Severity

### 1. Hardcoded Credentials
**File:** `app.py`, `app_phase2.py`
**Description:** Admin, Nurse, and Clinician passwords (e.g., `admin2025`) are hardcoded in the source code.
**Risk:** Critical security vulnerability if code is exposed.
**Recommendation:** Use environment variables or a secure vault for initial credentials, and enforce password changes on first login.

### 2. Insecure Docker Deployment (Phase 1 vs Phase 2)
**File:** `Dockerfile`
**Description:** The Dockerfile executes `CMD ["streamlit", "run", "app.py", ...]`. However, `app.py` is the insecure, JSON-based "Phase 1" application. The robust, database-backed application is `app_phase2.py`.
**Risk:** Production deployments will run the inferior, thread-unsafe version of the app.
**Recommendation:** Update Dockerfile to run `app_phase2.py`.

### 3. Thread-Safety in Chat History
**File:** `app.py`
**Description:** Uses `.chat_history.json` to store chat logs. Streamlit is multi-threaded; concurrent writes to this JSON file will cause data corruption or race conditions.
**Risk:** Data loss in multi-user environments.
**Recommendation:** Switch to `app_phase2.py` which uses PostgreSQL, or implement file locking (though DB is preferred).

### 4. FHIR Profile Validation Errors
**File:** `input/fsh/onc-profiles.fsh`
**Description:**
- **`ONCNursingAssessment`**: Slicing discriminator path is set to `coding.code` for `category` (CodeableConcept). SUSHI best practice and memory guidelines suggest using pattern slicing with path `$this` or `value` for fixed assignments to avoid validation errors.
- **`ONCBradenScaleAssessment`**: The `valueQuantity` element restricts unit and system but fails to restrict the code to `#{score}` as required by the "Assessment profiles" memory rule.
**Risk:** Generated profiles may fail validation or not be interoperable.
**Recommendation:** Update the FSH definitions to match best practices and memory constraints.

## Medium Severity

### 5. Dependency Issues
**File:** `requirements.txt`
**Description:**
- Duplicate `bcrypt==5.0.0` entry.
- Suspicious version `chromadb==1.3.5`: This appears to be a very recent (or future/non-standard) version compared to the common `0.4.x` series. It might be valid but warrants verification.
- Suspicious version `pandas==2.3.3`: While 2.3.x exists in some indices, standard stability might favor 2.2.3.
- Missing `ml_*.py` support: The Dockerfile does not copy `ml_*.py` files, but `requirements.txt` installs heavy ML libraries (scikit-learn, shap, etc.), creating a bloated image with unusable code.
**Risk:** Build failures or runtime errors due to version mismatches.
**Recommendation:** Clean up `requirements.txt` and verify `chromadb`/`pandas` versions.

### 6. Missing Monk Skin Tone Implementation
**File:** `input/fsh/onc-equity.fsh`
**Description:** Memory states "The Monk Skin Tone (MST) scale is implemented in `ONCMonkSkinToneObservation`...". This profile is **missing** from `onc-equity.fsh`. Only `ONCSkinToneObservation` (Fitzpatrick) is present.
**Risk:** Missing feature mandated by project requirements.
**Recommendation:** Implement the Monk Scale profile and CodeSystem.

## Low Severity

### 7. Missing Dependencies in Sushi Config
**File:** `sushi-config.yaml`
**Description:** `fhirVersion: 4.0.1` is set, but no `dependencies` section explicitly excludes `hl7.fhir.r4.core`. While often handled automatically, explicit exclusion is recommended to prevent "double loading" errors in some build environments.
**Risk:** Potential build warnings or slowness.

### 8. Unused Code
**File:** `ml_*.py`, `database.py` (in context of `app.py`)
**Description:** The ML modules are present but not integrated into the main application entry point (`app.py`). `database.py` is also unused by `app.py`.
**Risk:** Tech debt and confusion.
