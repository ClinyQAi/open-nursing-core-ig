"""
Automated script to fix vulnerable logging patterns across all Python files.
This script replaces logger.error(f"...: {e}") with safe logging utility calls.
"""
import re
from pathlib import Path

# Base directory
BASE_DIR = Path(r"c:\Users\g0226\OneDrive\Desktop\fhir-git\open-nursing-core-ig")

# Files to update with their vulnerable patterns
FILES_TO_UPDATE = {
    "ml/analytics_dashboard.py": [
        (173, 'logger.error(f"Failed to load usage analytics: {e}")', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Failed to load usage analytics", e)'),
        (279, 'logger.error(f"Failed to load compliance report: {e}")', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Failed to load compliance report", e)'),
        (329, 'logger.error(f"Failed to load knowledge gaps: {e}")', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Failed to load knowledge gaps", e)'),
        (411, 'logger.error(f"Failed to load user activity: {e}")', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Failed to load user activity", e)'),
    ],
    "db/db_migrations.py": [
        (74, 'logger.error(f"Backup error: {e}")', 'from core.safe_logging import log_exception_safe\n        log_exception_safe(logger, "Backup error", e)'),
        (116, 'logger.error(f"Restore error: {e}")', 'from core.safe_logging import log_exception_safe\n        log_exception_safe(logger, "Restore error", e)'),
        (145, 'logger.warning(f"Failed to delete {backup.name}: {e}")', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Failed to delete backup file", e, level="warning")'),
        (271, 'logger.error(f"Migration failed: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n        log_exception_safe(logger, "Migration failed", e)'),
        (309, 'logger.error(f"Rollback failed: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n        log_exception_safe(logger, "Rollback failed", e)'),
    ],
    "core/validator.py": [
        (91, 'logger.error(f"Database authentication error: {e}")', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Database authentication error", e)'),
        (128, 'logger.error(f"Failed to copy vector DB: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Failed to copy vector DB", e)'),
        (144, 'logger.error(f"Failed to load vector DB: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n        log_exception_safe(logger, "Failed to load vector DB", e)'),
        (157, 'logger.warning(f"Failed to save to database: {e}")', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Failed to save to database", e, level="warning")'),
        (177, 'logger.error(f"Failed to save chat history to file: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n        log_exception_safe(logger, "Failed to save chat history to file", e)'),
        (193, 'logger.warning(f"Failed to load from database: {e}")', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Failed to load from database", e, level="warning")'),
        (203, 'logger.warning(f"Failed to load chat history from file: {e}")', 'from core.safe_logging import log_exception_safe\n        log_exception_safe(logger, "Failed to load chat history from file", e, level="warning")'),
        (215, 'logger.warning(f"Failed to log audit event to DB: {e}")', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Failed to log audit event to DB", e, level="warning")'),
        (227, 'logger.warning(f"Failed to log analytics to DB: {e}")', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Failed to log analytics to DB", e, level="warning")'),
    ],
    "core/ehr_integration.py": [
        (92, 'logger.error(f"Error retrieving patient: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Error retrieving patient", e)'),
        (127, 'logger.error(f"Error retrieving conditions: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Error retrieving conditions", e)'),
        (168, 'logger.error(f"Error retrieving observations: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Error retrieving observations", e)'),
        (202, 'logger.error(f"Error retrieving care plans: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Error retrieving care plans", e)'),
        (233, 'logger.error(f"Error retrieving goals: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Error retrieving goals", e)'),
        (277, 'logger.error(f"Error creating observation: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Error creating observation", e)'),
        (310, 'logger.error(f"Error updating care plan: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Error updating care plan", e)'),
        (362, 'logger.error(f"Error parsing HL7 message: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Error parsing HL7 message", e)'),
        (402, 'logger.error(f"Error creating HL7 message: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Error creating HL7 message", e)'),
        (541, 'logger.error(f"Error syncing patient data: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Error syncing patient data", e)'),
        (564, 'logger.error(f"Error sending observation: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Error sending observation", e)'),
        (582, 'logger.error(f"Error processing HL7 message: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Error processing HL7 message", e)'),
    ],
    "app_phase2.py": [
        (113, 'logger.error(f"Database initialization failed: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Database initialization failed", e)'),
        (138, 'logger.warning(f"Could not seed user {username}: {e}")', 'from core.safe_logging import log_exception_safe\n            log_exception_safe(logger, "Could not seed user", e, level="warning")'),
        (336, 'logger.error(f"QA error: {e}", exc_info=True)', 'from core.safe_logging import log_exception_safe\n                        log_exception_safe(logger, "QA error", e)'),
    ],
}

def fix_file(filepath, replacements):
    """Fix vulnerable logging patterns in a single file."""
    full_path = BASE_DIR / filepath
    
    print(f"\nProcessing: {filepath}")
    
    # Read file
    with open(full_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Apply replacements (in reverse order to preserve line numbers)
    for line_num, old_pattern, new_pattern in reversed(replacements):
        idx = line_num - 1  # Convert to 0-indexed
        if idx < len(lines):
            # Check if line matches expected pattern
            if old_pattern in lines[idx]:
                lines[idx] = lines[idx].replace(old_pattern, new_pattern)
                print(f"  ✓ Fixed line {line_num}")
            else:
                print(f"  ⚠ Line {line_num} doesn't match expected pattern")
                print(f"    Expected: {old_pattern[:50]}...")
                print(f"    Found: {lines[idx].strip()[:50]}...")
    
    # Write back
    with open(full_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"  ✅ {filepath} updated")

def main():
    """Main function to fix all files."""
    print("=" * 60)
    print("Fixing Vulnerable Logging Patterns")
    print("=" * 60)
    
    total_fixes = sum(len(replacements) for replacements in FILES_TO_UPDATE.values())
    print(f"\nTotal files to update: {len(FILES_TO_UPDATE)}")
    print(f"Total fixes to apply: {total_fixes}")
    
    for filepath, replacements in FILES_TO_UPDATE.items():
        fix_file(filepath, replacements)
    
    print("\n" + "=" * 60)
    print("✅ All files updated successfully!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review changes with: git diff")
    print("2. Test with: python test_safe_logging.py")
    print("3. Commit changes")

if __name__ == "__main__":
    main()
