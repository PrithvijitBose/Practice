"use client"
import { useState } from "react"

export default function Form() {
    const [title, setTitle] = useState('')
    const [content, setContent] = useState('')
    const [category, setCategory] = useState('')

    async function saveNote() {
        const response = await fetch("http://127.0.0.1:8000/notes",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    title,
                    content,
                    category
                })
            }

        )
  
    }


    function changeTitle(e) {
        setTitle(e.target.value);
    }
    function changeContent(e) {
        setContent(e.target.value);
    }
    function changeCategory(e) {
        setCategory(e.target.value)
    }
    function resetForm() {
        setTitle('')
        setCategory('')
        setContent('')
    }
    return (
        <>
            <button>New Note</button>
            <br />
            <br />
            <input value={title} onChange={changeTitle} placeholder="Enter Title" />
            <input value={content} onChange={changeContent} placeholder="Enter Content" />
            <input value={category} onChange={changeCategory} placeholder="Enter Category" />
            <br />
            <br />
            <button onClick={resetForm}>Reset</button>
            <br />
            <br />
            <button onClick={saveNote}>Save Note</button>
        </>
    )

}