from fastapi import APIRouter, Path, HTTPException, Depends
from typing import Optional, Annotated
from models.students_modal import Student
import utils.db_helper as db
import utils.auth_helper as auth

router = APIRouter()
DB_FILEPATH = "./data/school_database.json"

@router.get("/students")
async def get_students(is_admin: Annotated[str, Depends(auth.verify_admin)], inclass: Optional[str] = None):
    """Root directory

    Returns:
        json: a list of all students
    """
    all_students = db.get_all_students(DB_FILEPATH)
    if not inclass:
        return all_students
    
    # If user is trying to filter by class, then make sure they are admin
    if not is_admin:
        raise HTTPException(status_code=401, detail="You don't have permission, only admins can filter by student class")
    
    students_in_class = [student for student in all_students if inclass.lower() in student["classes"]]
    return students_in_class

    
@router.get("/students/{id}", dependencies=[Depends(auth.verify_user)])
def get_student_by_id(id: int = Path(title="The ID of the student you want to get", description="It must be a non zero integer", gt=0)):
    return db.get_student_by_id(DB_FILEPATH, id)


@router.post("/students")
def post_student(is_admin: Annotated[str, Depends(auth.verify_admin)], new_student: Student):
    """Add new students to the database"""
    if not is_admin:
        raise HTTPException(status_code=401, detail="You don't have permission, only admins can add students")
    
    add_result = db.add_student(DB_FILEPATH, new_student)
    return add_result