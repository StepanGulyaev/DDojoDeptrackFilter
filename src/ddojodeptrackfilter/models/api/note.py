from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

from .inline_schemas.note_user import NoteUser

from .note_type import NoteType
from .note_history import NoteHistory

class Note(BaseModel):
    id: int
    author: Optional[NoteUser] = None
    editor: Optional[NoteUser] = None 
    history: List[NoteHistory] = Field(default_factory=list)
    note_type: Optional[NoteType] = None
    entry: str
    date: datetime
    private: Optional[bool] = None
    edited: Optional[bool] = None
    edit_time: datetime

    model_config = {
        "populate_by_name": True,
        "extra": "ignore",
        "json_encoders": {
            datetime: lambda v: v.isoformat(),
        }
    }
