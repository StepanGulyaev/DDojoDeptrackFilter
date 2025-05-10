from datetime import datetime
from typing import List
from pydantic import BaseModel, Field

from .note_user import NoteUser
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
    private: bool
    edited: bool
    edit_time: datetime
