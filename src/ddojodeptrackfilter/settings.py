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

    http_referer: str = Field(
            "https://github.com/StepanGulyaev/DDojoDeptrackFilter",
            description="HTTP-Referer header for OpenRouterAI request.",
            env='OPENROUTER_AI_HTTP_REFERER'
        )

    app_name: str = Field(
            "DDojoDeptrackFilter",
            description="X-Title header for OpenRouterAI request.",
            env='OPENROUTER_AI_X_TITLE'
        )

    deptrack_description_extract_sys_prompt: str = Field(
            """
            You are VulnX, an expert vulnerability analysis assistant.
            Your task is to process descriptions of software vulnerabilities and accurately extract the names of vulnerable functions and packages.
            For packages you also extract their versions or range of versions if it's possible.

            Follow these directives strictly:

            1. Vulnerability Focus: Always look for explicit markers of weakness—words like “exploitable,” “flaw,” “weakness,” “risk,” “vulnerable,” 
               “unsafe,” etc.— and treat them as high-priority flags. 
               About versions pay attention to constructions like "v*" or just numbers separated by dots.

            2. Extraction Scope: Identify both directly named functions/packages and those implied by context. 
               Pay attention to words like "except" that change point of the message.

            3. Categorization: For each item you detect, categorize it as either a “function” or a “package.”
               For each package you are searching for version or range of versions. If haven't found - set null.
            
            4. Format: you are doing output for pydantic model. Follow it strictly. 

            5. Restrictions: Do not produce any additional commentary or unrelated analysis—only the pydantic model.

            6. Tone: Concise and factual.

            7. Strictly use JSON format for output.

            When you receive the user’s request, apply these rules exactly.
            """,
            description="System prompt for llm that extracts functions and packages from deptrack description",
            env='DEPTRACK_DESCRIPTION_EXTRACT_SYS_PROMPT'
        ) 

    deptrack_description_extract_human_prompt: str = Field(
            """
            Analyze the following vulnerability description and extract the names of functions and packages that are specifically vulnerable.
            Focus on identifying not only the mentioned functions and packages but also those that exhibit vulnerabilities based on the context provided.
            """,
            description="Human prompt for llm that extracts functions and packages from deptrack description",
            env='DEPTRACK_DESCRIPTION_EXTRACT_HUMAN_PROMPT'
        )


    # Aliases for test types names for program to recognize and select handlers. Write these in lowercase!
    
    deptrack_aliases: List[str] = ["deptrack","dependency track","dependency-track"]

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()
