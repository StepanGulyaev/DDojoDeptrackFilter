from pydantic import BaseModel

class NoteAuthor(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str

