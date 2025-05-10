from pydantic import BaseModel

class NoteType(BaseModel):
    id: int
    name: str
    description: str
    is_single: bool
    is_active: bool
    is_mandatory: bool
