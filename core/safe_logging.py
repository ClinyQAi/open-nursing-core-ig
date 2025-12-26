"""Safe logging utilities to prevent sensitive data leakage.

This module provides utilities for safely logging exceptions without exposing
sensitive information like passwords, tokens, or PII in application logs.
"""
import logging
from typing import Optional


def log_exception_safe(
    logger: logging.Logger,
    message: str,
    exception: Exception,
    level: str = "error",
    include_type: bool = True
) -> None:
    """
    Safely log an exception without exposing sensitive data.
    
    Instead of logging the full exception message (which may contain sensitive data),
    this function logs only the exception type or a generic message.
    
    Args:
        logger: Logger instance to use
        message: Context message describing what failed
        exception: Exception object to log safely
        level: Log level (error, warning, info, debug)
        include_type: Whether to include exception type name in the log
        
    Example:
        >>> try:
        >>>     create_user("admin", "SecretPassword123!")
        >>> except Exception as e:
        >>>     log_exception_safe(logger, "User creation failed", e)
        >>> # Logs: "User creation failed: IntegrityError"
        >>> # Does NOT log: "User creation failed: UNIQUE constraint failed: password=SecretPassword123!"
    """
    if include_type:
        safe_message = f"{message}: {type(exception).__name__}"
    else:
        safe_message = message
    
    log_func = getattr(logger, level.lower())
    log_func(safe_message)


def get_safe_error_message(exception: Exception) -> str:
    """
    Get a safe error message from an exception.
    
    Returns only the exception type name, not the potentially sensitive message.
    
    Args:
        exception: Exception object
        
    Returns:
        String containing only the exception type name
        
    Example:
        >>> try:
        >>>     raise ValueError("password=secret123")
        >>> except Exception as e:
        >>>     safe_msg = get_safe_error_message(e)
        >>> # safe_msg = "ValueError"
    """
    return type(exception).__name__


def mask_identifier(identifier: str, prefix: str = "id") -> str:
    """
    Mask an identifier for safe logging.
    
    Completely masks the identifier to prevent any sensitive data leakage.
    This security measure ensures no part of the identifier (which may contain
    or be derived from sensitive information) is exposed in logs.
    The prefix parameter is used to identify the type of identifier in logs.
    Completely masks the identifier value to prevent any sensitive data exposure.
    Returns only the prefix with masked content, without revealing any characters
    from the actual identifier.
    
    Args:
        identifier: The identifier to mask (patient_id, username, etc.)
        prefix: Prefix to use for the masked value (e.g., 'pat', 'user', 'id')
        
    Returns:
        Masked identifier string in the format: prefix_****
        Masked identifier string in format: "{prefix}_****"
        
    Example:
        >>> mask_identifier("patient12345", "pat")
        'pat_****'
        >>> mask_identifier("admin", "user")
        'user_****'
        >>> mask_identifier("", "id")  # Even empty strings are masked consistently
        'id_****'
    """
    return f"{prefix}_****"


def safe_log_info(
    logger: logging.Logger,
    message: str,
    **identifiers
) -> None:
    """
    Safely log an info message with masked identifiers.
    
    Args:
        logger: Logger instance to use
        message: Message template with {placeholders}
        **identifiers: Key-value pairs of identifiers to mask
        
    Example:
        >>> safe_log_info(logger, "Processing patient {patient_id}", 
        ...               patient_id=("patient12345", "pat"))
        # Logs: "Processing patient pat_****"
    """
    masked_values = {}
    for key, value in identifiers.items():
        if isinstance(value, tuple):
            identifier, prefix = value
            masked_values[key] = mask_identifier(identifier, prefix)
        else:
            masked_values[key] = mask_identifier(value, key)
    
    logger.info(message.format(**masked_values))


def safe_log_warning(
    logger: logging.Logger,
    message: str,
    **identifiers
) -> None:
    """
    Safely log a warning message with masked identifiers.
    
    Args:
        logger: Logger instance to use
        message: Message template with {placeholders}
        **identifiers: Key-value pairs of identifiers to mask
        
    Example:
        >>> safe_log_warning(logger, "No data for patient {patient_id}", 
        ...                  patient_id=("67890", "pat"))
        # Logs: "No data for patient pat_****"
    """
    masked_values = {}
    for key, value in identifiers.items():
        if isinstance(value, tuple):
            identifier, prefix = value
            masked_values[key] = mask_identifier(identifier, prefix)
        else:
            masked_values[key] = mask_identifier(value, key)
    
    logger.warning(message.format(**masked_values))

