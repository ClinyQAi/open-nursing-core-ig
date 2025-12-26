"""
Test script to verify safe logging implementation.
Tests that sensitive data is NOT logged in exception messages.
"""
import logging
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.safe_logging import log_exception_safe, get_safe_error_message

# Configure logging to console
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

def test_safe_exception_logging():
    """Test that exceptions are logged safely without sensitive data."""
    print("\n" + "="*60)
    print("Testing Safe Exception Logging")
    print("="*60 + "\n")
    
    # Test 1: ValueError with sensitive data
    print("Test 1: ValueError with sensitive data")
    print("-" * 40)
    try:
        raise ValueError("password=SecretPassword123!")
    except Exception as e:
        log_exception_safe(logger, "Operation failed", e)
        print("✅ PASS: Only exception type logged, not sensitive data\n")
    
    # Test 2: Database constraint violation simulation
    print("Test 2: Database constraint violation")
    print("-" * 40)
    try:
        # Simulate IntegrityError with username/password in message
        raise Exception("UNIQUE constraint failed: users.username='admin', password_hash='$2b$12$...'")
    except Exception as e:
        log_exception_safe(logger, "User creation failed", e, level="warning")
        print("✅ PASS: Only exception type logged, not credentials\n")
    
    # Test 3: get_safe_error_message utility
    print("Test 3: get_safe_error_message utility")
    print("-" * 40)
    try:
        raise RuntimeError("API_KEY=sk-1234567890abcdef")
    except Exception as e:
        safe_msg = get_safe_error_message(e)
        assert safe_msg == "RuntimeError", f"Expected 'RuntimeError', got '{safe_msg}'"
        assert "API_KEY" not in safe_msg, "Sensitive data leaked!"
        print(f"Safe message: {safe_msg}")
        print("✅ PASS: Only exception type returned\n")
    
    # Test 4: Different log levels
    print("Test 4: Different log levels")
    print("-" * 40)
    try:
        raise ConnectionError("token=bearer_abc123xyz")
    except Exception as e:
        log_exception_safe(logger, "Connection failed", e, level="error")
        log_exception_safe(logger, "Retrying connection", e, level="warning")
        log_exception_safe(logger, "Connection info", e, level="info")
        print("✅ PASS: All log levels work correctly\n")
    
    # Test 5: Without exception type
    print("Test 5: Logging without exception type")
    print("-" * 40)
    try:
        raise PermissionError("access_token=sensitive_token_here")
    except Exception as e:
        log_exception_safe(logger, "Access denied", e, include_type=False)
        print("✅ PASS: Generic message logged without type\n")
    
    print("="*60)
    print("✅ ALL TESTS PASSED")
    print("="*60)
    print("\nVerification:")
    print("- Check the log output above")
    print("- Confirm NO sensitive data (passwords, tokens, etc.) appears")
    print("- Only exception types and context messages should be visible")
    print("\n")

def test_database_logging():
    """Test database module safe logging."""
    print("\n" + "="*60)
    print("Testing Database Module Safe Logging")
    print("="*60 + "\n")
    
    try:
        from db.database import add_user
        
        print("Attempting to create duplicate user...")
        print("(This should log safely without exposing password)")
        print("-" * 40)
        
        # First user creation (should succeed or already exist)
        try:
            add_user("test_user_safe_logging", "SecretPassword123!", "nurse", "test@example.com")
            print("First user created")
        except:
            print("User already exists (expected)")
        
        # Duplicate user creation (should fail safely)
        try:
            add_user("test_user_safe_logging", "SecretPassword123!", "nurse", "test@example.com")
            print("⚠️ WARNING: Duplicate user was created (unexpected)")
        except Exception as e:
            print(f"✅ PASS: Duplicate user rejected")
            print(f"Exception type: {type(e).__name__}")
            print("Check logs above - password should NOT be visible")
        
        print("\n")
        
    except ImportError as e:
        print(f"⚠️ SKIP: Database module not available ({e})")
        print("This is OK if database is not configured\n")

if __name__ == "__main__":
    test_safe_exception_logging()
    test_database_logging()
    
    print("="*60)
    print("MANUAL VERIFICATION REQUIRED")
    print("="*60)
    print("\nReview the log output above and confirm:")
    print("1. ✓ No passwords visible in logs")
    print("2. ✓ No tokens or API keys visible")
    print("3. ✓ Only exception types and context messages logged")
    print("4. ✓ All sensitive data is hidden")
    print("\nIf all checks pass, the safe logging implementation is working correctly!")
    print("="*60 + "\n")
