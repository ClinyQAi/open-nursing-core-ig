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
