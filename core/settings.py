from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
import os
import logging

logger = logging.getLogger(__name__)

class Settings(BaseSettings):
    """
    Application configuration via environment variables.
    """
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # Application
    APP_ENV: str = Field(default="development")
    LOG_LEVEL: str = Field(default="INFO")
    LOG_FILE: str = Field(default="/tmp/nursing_validator.log")

    # Security / Users
    # IMPORTANT: In production, these must be set via env vars.
    # Default values are provided for development convenience only.
    ADMIN_PASSWORD: str = Field(default="change_me_admin")
    NURSE_PASSWORD: str = Field(default="change_me_nurse")
    CLINICIAN_PASSWORD: str = Field(default="change_me_clinician")

    # Database
    USE_DATABASE: bool = Field(default=True)
    DB_HOST: str = Field(default="localhost")
    DB_PORT: str = Field(default="5432")
    DB_NAME: str = Field(default="nursing_validator")
    DB_USER: str = Field(default="nursing_admin")
    DB_PASSWORD: str = Field(default="nursing_password")
    DB_POOL_MIN: int = Field(default=2)
    DB_POOL_MAX: int = Field(default=20)

    # Vector Database
    VECTOR_DB_PATH: str = Field(default="chroma_db_fons")
    LOCAL_DB_PATH: str = Field(default="/tmp/chroma_db_fons_fast")
    EMBEDDING_MODEL: str = Field(default="text-embedding-ada-002")

    # Azure OpenAI
    AZURE_OPENAI_ENDPOINT: Optional[str] = Field(default=None)
    AZURE_OPENAI_API_KEY: Optional[str] = Field(default=None)
    AZURE_OPENAI_API_VERSION: Optional[str] = Field(default="2023-05-15")
    AZURE_OPENAI_DEPLOYMENT: Optional[str] = Field(default=None)

    # Streamlit Specific
    STREAMLIT_SERVER_HEADLESS: bool = Field(default=True)
    STREAMLIT_SERVER_ENABLE_CORS: bool = Field(default=False)

    def is_production(self) -> bool:
        return self.APP_ENV.lower() == "production"

    def check_security(self):
        """Warn if using default insecure passwords."""
        defaults = ["change_me_admin", "change_me_nurse", "change_me_clinician"]
        if self.ADMIN_PASSWORD in defaults or \
           self.NURSE_PASSWORD in defaults or \
           self.CLINICIAN_PASSWORD in defaults:
            logger.warning(
                "SECURITY WARNING: Default passwords are in use. "
                "Set ADMIN_PASSWORD, NURSE_PASSWORD, and CLINICIAN_PASSWORD in .env."
            )

# Create a global instance
settings = Settings()
settings.check_security()
