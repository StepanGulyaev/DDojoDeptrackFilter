from pydantic import BaseModel, Field
from typing import Optional

class NoteType(BaseModel):
    id: int
    name: str = Field(...,max_length=100)
    description: str = Field(...,max_length=100)
    is_single: Optional[bool]
    is_active: Optional[bool]
    is_mandatory: Optional[bool]
