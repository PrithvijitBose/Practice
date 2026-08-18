from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Any

from database import create_database, save_note,get_note_by_id,get_note_all,update_note,delete_note
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins=[
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    category: str


class Note(BaseModel):
    title: str
    content: str
    category: str


create_database()


@app.get("/notes/{note_id}",response_model=NoteResponse)
def get_note(note_id:int):
    note = get_note_by_id(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    response= NoteResponse(
        id=note[0],
        title=note[1],
        content=note[2],
        category=note[3]
    )
    return response

@app.get("/get",response_model=list[NoteResponse])
def all_notes():
    notes = get_note_all()
    responses=[]
    
    for note in notes:
        response = NoteResponse(
            id=note[0],
        title=note[1],
        content=note[2],
        category=note[3]
        )
        responses.append(response)
    return responses



@app.post("/notes")
def create_note(note: Note):
    note_id= save_note(
        note.title,
        note.content,
        note.category
    )

    return {
        "message": "Note created successfully",
        "note": note,
        "note_id": note_id
    }

@app.put("/notes/{note_id}")
def update(note:Note,note_id:int):
    updated_rows= update_note(
        note.title,
        note.category,
        note.content,
        note_id
    )
    if updated_rows==0:
        raise HTTPException(status_code=404,detail="Note not found")
    return {
        "message": "Note Updated successfully",
        "rows updated": updated_rows

    }
        
@app.delete("/notes/{note_id}")
def delete(note_id:int):
    deleted_rows = delete_note(note_id)

    if deleted_rows==0:
        raise HTTPException(status_code=404,detail="Note not found")

    return {
        "message":"Note deleted successfully"
    }


    



