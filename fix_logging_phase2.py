"""
Automated script to fix remaining 13 clear-text logging CodeQL alerts.

This script applies identifier masking to info/warning logs that include
sensitive identifiers like patient_id, username, user_id, etc.
"""

import re
from pathlib import Path

# Define all the fixes to apply
FIXES = [
    # database.py - Line 240
    {
        "file": "db/database.py",
        "search": '            logger.info(f"User created: {username} (ID: {user_id})")',
        "replace": '''            from core.safe_logging import mask_identifier
            logger.info(f"User created: {mask_identifier(username, 'user')} (ID: {mask_identifier(str(user_id), 'id')})")''',
        "description": "Mask username and user_id in user creation log"
    },
    
    # app_phase2.py - Line 137
    {
        "file": "app_phase2.py",
        "search": '                logger.info(f"Seeded user: {username}")',
        "replace": '''                from core.safe_logging import mask_identifier
                logger.info(f"Seeded user: {mask_identifier(username, 'user')}")''',
        "description": "Mask username in user seeding log"
    },
]

# Additional fixes for files that need pattern searching
PATTERN_FIXES = [
    {
        "file": "core/ehr_integration.py",
        "patterns": [
            {
                "search_regex": r'logger\.warning\(f"No data for patient \{patient_id\}"\)',
                "replace": 'from core.safe_logging import mask_identifier\n        logger.warning(f"No data for patient {mask_identifier(patient_id, \'pat\')}")',
                "description": "Mask patient_id in warning log"
            },
            {
                "search_regex": r'logger\.info\(f"Processing patient \{patient_id\}"\)',
                "replace": 'from core.safe_logging import mask_identifier\n        logger.info(f"Processing patient {mask_identifier(patient_id, \'pat\')}")',
                "description": "Mask patient_id in info log"
            },
        ]
    },
    {
        "file": "ml/ml_recommendations.py",
        "patterns": [
            {
                "search_regex": r'logger\.info\(f"Generating recommendations for patient \{patient_id\}"\)',
                "replace": 'from core.safe_logging import mask_identifier\n        logger.info(f"Generating recommendations for patient {mask_identifier(patient_id, \'pat\')}")',
                "description": "Mask patient_id in recommendations log"
            },
            {
                "search_regex": r'print\(json\.dumps\(care_plan,',
                "replace": '# Removed sensitive data logging\n        # print(json.dumps(care_plan,',
                "description": "Comment out care_plan printing (contains sensitive data)"
            },
        ]
    },
    {
        "file": "ml/ml_anomaly_detection.py",
        "patterns": [
            {
                "search_regex": r'logger\.info\(f"Analyzing patient \{patient_id\}"\)',
                "replace": 'from core.safe_logging import mask_identifier\n        logger.info(f"Analyzing patient {mask_identifier(patient_id, \'pat\')}")',
                "description": "Mask patient_id in analysis log"
            },
            {
                "search_regex": r'logger\.debug\(f"Patient \{patient_id\} data:',
                "replace": 'from core.safe_logging import mask_identifier\n        logger.debug(f"Patient {mask_identifier(patient_id, \'pat\')} data:',
                "description": "Mask patient_id in debug log"
            },
        ]
    },
]


def apply_fixes():
    """Apply all logging security fixes."""
    base_path = Path("c:/Users/g0226/OneDrive/Desktop/fhir-git/open-nursing-core-ig")
    
    fixes_applied = 0
    
    # Apply direct string replacements
    for fix in FIXES:
        file_path = base_path / fix["file"]
        if not file_path.exists():
            print(f"⚠️  File not found: {file_path}")
            continue
            
        content = file_path.read_text(encoding='utf-8')
        
        if fix["search"] in content:
            content = content.replace(fix["search"], fix["replace"])
            file_path.write_text(content, encoding='utf-8')
            print(f"✅ {fix['file']}: {fix['description']}")
            fixes_applied += 1
        else:
            print(f"⚠️  Pattern not found in {fix['file']}")
    
    # Apply regex pattern fixes
    for file_fix in PATTERN_FIXES:
        file_path = base_path / file_fix["file"]
        if not file_path.exists():
            print(f"⚠️  File not found: {file_path}")
            continue
            
        content = file_path.read_text(encoding='utf-8')
        modified = False
        
        for pattern in file_fix["patterns"]:
            if re.search(pattern["search_regex"], content):
                content = re.sub(pattern["search_regex"], pattern["replace"], content)
                print(f"✅ {file_fix['file']}: {pattern['description']}")
                fixes_applied += 1
                modified = True
            else:
                print(f"⚠️  Pattern not found in {file_fix['file']}: {pattern['description']}")
        
        if modified:
            file_path.write_text(content, encoding='utf-8')
    
    print(f"\n🎉 Applied {fixes_applied} fixes total")
    return fixes_applied


if __name__ == "__main__":
    print("=" * 60)
    print("Fixing Clear-text Logging CodeQL Alerts")
    print("=" * 60)
    print()
    
    fixes_applied = apply_fixes()
    
    print()
    print("=" * 60)
    print(f"✅ Complete! Applied {fixes_applied} security fixes")
    print("=" * 60)
