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

<<<<<<< HEAD
    deptrack_description_extract_sys_prompt: str = Field(
=======
    openrouter_model_name: str = Field(
            "qwen/qwen3-32b:free",
            description="AI model for OpenRouterAI",
            env="OPENROUTER_MODEL_NAME"
        )

    openrouter_api_base_url: str = Field(
            "https://openrouter.ai/api/v1",
            description="API base url for OpenRouter AI",
            env='OPENROUTER_API_BASE_URL'
        )
           
    openrouter_api_key: str = Field(
            ...,
            description="API key for OpenRouter account",
            env="OPENROUTER_API_KEY"
        )
 

    # Deptrack variables part

    deptrack_description_extract_func_sys_prompt: str = Field(
>>>>>>> 6c6d366 (Dev: works not bad, only need to do report and early version of program done)
            """
            You are VulnX, an expert vulnerability analysis assistant.
            You are DefectDojo and Dependency Track expert.
            Your task is to process descriptions of software vulnerabilities and accurately extract the names of vulnerable functions.

            Follow these directives strictly:

            1. Vulnerability Focus: Always look for explicit markers of weakness—words like “exploitable”, “flaw”, “weakness”, “risk”, “vulnerable” 
               “unsafe” etc.— and treat them as high-priority flags. 

            2. Extraction Scope: Identify only directly named functions, always check if it is a function name. 
               Pay attention to words like "except","not" etc. that change point of the message.
          
            3. Format: you are doing output for pydantic model. Follow it strictly.

            4. Restrictions: Do not produce any additional commentary or unrelated analysis—only the pydantic model.

            5. Tone: Concise and factual.

            6. Strictly use JSON format for output.

            7. Check: before sending output - always check if functions you have extracted exist in text.
               Before sending output - always check if it's function and not something else.

            When you receive the user’s request, apply these rules exactly.
            """,
            description="System prompt for llm that extracts functions and packages from deptrack description",
            env='DEPTRACK_DESCRIPTION_EXTRACT_FUNC_SYS_PROMPT'
        ) 

    deptrack_description_extract_func_human_prompt: str = Field(
            """
            Analyze the following vulnerability description and extract the names of functions that are specifically vulnerable.
            Focus on identifying only vulnerable functions.
            """,
            description="Human prompt for llm that extracts functions and packages from deptrack description",
            env='DEPTRACK_DESCRIPTION_EXTRACT_FUNC_HUMAN_PROMPT'
        )

    deptrack_description_extract_package_sys_prompt: str = Field(
            """
            You are VulnX, an expert vulnerability analysis assistant.
            You are DefectDojo and Dependency Track expert.
            Your task is to process descriptions of software vulnerabilities and accurately extract the names of vulnerable packages
            and their versions or range of versions if there are any.

            Follow these directives strictly:

            1. Vulnerability Focus: Always look for explicit markers of weakness—words like “exploitable,” “flaw,” “weakness,” “risk,” “vulnerable,” 
               “unsafe,” etc.— and treat them as high-priority flags. 
                With versions pay attention to constructions like "v*" or numbers separated by dots.


            2. Extraction Scope: Identify only directly named packages. 
               Pay attention to words like "except" that change point of the message.
               Pay attention to versions. Version output may be not only just version, it may be range of versions.
               In text there could be mentioned not vulnerable versions but safe ones.
               If safe version is 7.1.1 and it's newer one then write output version like that: "<7.1.1".             

            3. For each package you are searching for version or range of versions. If haven't found version - set version null.
            
            4. Format: you are doing output for pydantic model. Follow it strictly. Version field may contain "<",">","=" to show range of versions.

            5. Restrictions: Do not produce any additional commentary or unrelated analysis—only the pydantic model.
               You are extracting data from given package description and you are not interested in this package by itself and don't put it in the output.
               User is giving you file_path and component_name of that package like that: 
               "Don't include package with file_path: <file_path> and component_name: <component_name> in output." 

            6. Tone: Concise and factual.

            7. Strictly use JSON format for output.

            8. Check package: before sending output - always check if package you have extracted exist in text.
               Before sending output - always check if it's a package/plugin and not something else.

            9. Check version: before sending output - always check if versions of package you found are vulnerable ones.

            10. Check added packages: before sending output - take given by user file_path and component_name of package you have been said to ignore and if 
                you had put it to the output - remove it from the output.

            When you receive the user’s request, apply these rules exactly.
            """,
            description="System prompt for llm that extracts functions and packages from deptrack description",
            env='DEPTRACK_DESCRIPTION_EXTRACT_FUNC_SYS_PROMPT'
        ) 

    deptrack_description_extract_package_human_prompt: str = Field(
            """
            Analyze the following vulnerability description and extract the names of packages and packages versions that are specifically vulnerable.
            Focus on identifying only vulnerable packages and versions. 
            Don't include package with file_path: {file_path} and component_name: {component_name} in output.
            """,
            description="Human prompt for llm that extracts functions and packages from deptrack description",
            env='DEPTRACK_DESCRIPTION_EXTRACT_FUNC_HUMAN_PROMPT'
        )

    # Aliases for test types names for program to recognize and select handlers. Write these in lowercase!
    
    deptrack_aliases: List[str] = ["deptrack","dependency track","dependency-track"]

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()