import logging
import os
from core.settings import settings

def configure_logging():
    """
    Configure global logging based on settings.
    """
    log_level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)

    # Ensure log directory exists if writing to file
    log_file = settings.LOG_FILE
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        try:
            os.makedirs(log_dir, exist_ok=True)
        except OSError:
            # Fallback if cannot create directory (e.g. permission issue)
            pass

    handlers = [logging.StreamHandler()]

    # improved file handling logic
    try:
        handlers.append(logging.FileHandler(log_file))
    except (OSError, IOError) as e:
        print(f"Warning: Could not set up file logging to {log_file}: {e}")

    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=handlers,
        force=True  # Overwrite any existing config
    )

    # Quiet down some noisy libraries
    logging.getLogger("azure.core.pipeline.policies.http_logging_policy").setLevel(logging.WARNING)
    logging.getLogger("chromadb").setLevel(logging.WARNING)

    logger = logging.getLogger(__name__)
    logger.info(f"Logging configured at level {settings.LOG_LEVEL}")
