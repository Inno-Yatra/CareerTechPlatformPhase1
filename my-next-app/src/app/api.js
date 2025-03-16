const API_URL = "http://127.0.0.1:8000"; // Django backend URL

export async function insertStudent() {
    try {
        const response = await fetch(`${API_URL}/students/insert-student/`);
        const data = await response.json();
        console.log("Student inserted:", data);
    } catch (error) {
        console.error("Error inserting student:", error);
    }
}
