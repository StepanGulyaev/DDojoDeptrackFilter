from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class DeptrackDescriptionExtractModel(BaseModel):
    functions: List[str] = Field(
            default_factory=list,
            description="Extracted vulnerable function names from the text"
        )
   
    packages: List[Dict[str,Optional[str]]] = Field(
            default_factory=list,
            description="List of packages with optional versions",
            example=[
                { "package": "openssl", "version": "3.0.7"},
                { "package": "django", "version": None},
                { "package": "pydantic", "version": "<2.0.0"}
            ]
        )

