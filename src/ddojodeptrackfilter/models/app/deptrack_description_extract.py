from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class FunctionExtractModel(BaseModel):
    functions: List[str] = Field(
        default_factory=list,
        description="Extracted vulnerable function names from the text"
    )

class PackageInfo(BaseModel):
    package: str
    version: Optional[str]

class PackageExtractModel(BaseModel):
    packages: List[PackageInfo] = Field(
        default_factory=list,
        description="List of packages with optional versions",
        example=[
            PackageInfo(package="openssl", version="3.0.7"),
            PackageInfo(package="django", version=None),
            PackageInfo(package="pydantic", version="<2.0.0"),
        ],
    )
