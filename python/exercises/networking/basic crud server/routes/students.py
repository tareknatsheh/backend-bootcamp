from fastapi import APIRouter, Path
from typing import Optional
from models.students_modal import Student
import utils.db_helper as db

router = APIRouter()

DB_FILEPATH = "./data/school_database.json"

@router.get("/students")
def get_students(inclass: Optional[str] = None):
    """Root directory, returns all students

    Returns:
        json: a list of all students
    """
    all_students = db.get_all_students(DB_FILEPATH)
    if not inclass:
        return all_students
    students_in_class = [student for student in all_students if inclass.lower() in student["classes"]]
    return students_in_class

    
@router.get("/students/{id}")
def get_student_by_id(id: int = Path(title="The ID of the student you want to get", description="It must be a non zero integer", gt=0)):
    return db.get_student_by_id(DB_FILEPATH, id)


@router.post("/students")
def post_student(new_student: Student):
    add_result = db.add_student(DB_FILEPATH, new_student)
    return add_result