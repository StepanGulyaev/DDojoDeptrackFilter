from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

from .inline_schemas.note_user import NoteUser

from .note_type import NoteType
from .note_history import NoteHistory

class Note(BaseModel):
    id: int
    author: NoteUser
    editor: NoteUser
    history: List[NoteHistory] = Field(default_factory=list)
    note_type: NoteType
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
