from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

from database import create_database, save_note,get_note_by_id

app = FastAPI()


class Note(BaseModel):
    title: str
    content: str
    category: str


create_database()


@app.get("/notes/{note_id}")
def get_note(note_id:int):
    note = get_note_by_id(note_id)
    if note is None:
       raise HTTPException(status_code=404, detail="Note not found")
    return {"note": note}


@app.post("/notes")
def create_note(note: Note):
    save_note(
        note.title,
        note.content,
        note.category
    )

    return {
        "message": "Note created successfully",
        "note": note
    }