from pydantic import BaseModel, Field
from typing import Any,Dict,List,Optional

class NoteUser(BaseModel):
    id: int
    username: str = Field(...,max_length=150,pattern=r'^[\w.@+-]+$')
    first_name: Optional[str] = Field(None,max_length=150)
    last_name: Optional[str] = Field(None,max_length=150)

