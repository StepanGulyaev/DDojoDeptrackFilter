from datetime import datetime
from pydantic import BaseModel

from .note_author import NoteAuthor
from .note_type import NoteType

class NoteHistory(BaseModel):
    id: int
    current_editor: NoteAuthor
    note_type: NoteType
    data: str
    time: datetime
