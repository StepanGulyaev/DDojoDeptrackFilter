from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    findings_limit_size: int = Field(
            1000,
            ge=1,
            le=1000,
            description="Page size for findings retrieval",
            env='DDOJO_FINDINGS_LIMIT_SIZE'
        )
 
    max_workers: int = Field(
            5,
            description="Number of concurrent working threads",
            ge=1,
            le=20,
            env='DDOJO_CLIENT_WORKERS'
        )

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()
