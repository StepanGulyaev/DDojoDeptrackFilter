from pydantic import Field
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    limit: int = Field(
            1000,
            ge=1,
            le=1000,
            description="Page size for findings retrieval",
            env='DDOJO_FINDINGS_LIMIT_SIZE'
        )
 
    workers: int = Field(
            15,
            description="Number of concurrent working threads",
            ge=1,
            le=20,
            env='DDOJO_CLIENT_WORKERS'
        )

    # Aliases for test types names for program to recognize and select handlers. Write these in lowercase!
    
    deptrack_aliases: List[str] = ["deptrack","dependency track","dependency-track"]



    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()
