
import Form from "./newForm"
type Note = {
  id: number
  title: string
  content: string
  category: string
}

export default async function Page() {

  const data = await fetch('http://localhost:8000/get')
  const notes = await data.json()  as Note[]
  return (
    <>
    <ul>
      {notes.map((note) => (
        <li key={note.id}>{note.title}</li>
      ))}
    </ul>
    
    <h1>Notes App</h1>
    <Form/>
    </>
  )
}