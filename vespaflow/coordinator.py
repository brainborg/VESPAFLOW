Read Coordinator · PY
"""
VespaFlow configuration — driven entirely by environment variables.
All settings are prefixed with VESPAFLOW_.
"""

from __future__ import annotations
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="VESPAFLOW_",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # LLM backend
    llm_backend: str = "ollama"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2"
    anthropic_api_key: str = ""
    anthropic_model: str = "claude-3-haiku-20240307"

    # Remediation behaviour
    max_fix_iterations: int = 3
    auto_apply: bool = False

    # Webhook security
    webhook_secret: str = ""


settings = Settings()
