import json

def get_data(file_path):
    with open(file_path) as f:
        data = json.load(f)
        return data

def write_data(file_path, data):
    with open(file_path, "r+") as f:
        f.seek(0)        
        json.dump(data,f, indent=4)
        f.truncate()
        return True

def get_all_students(file_path):
    data = get_data(file_path)
    return data["students"]

def get_student_by_id(file_path, id):
    all_students = get_all_students(file_path)
    for student in all_students:
        if student["id"] == id:
            return student
    raise FileNotFoundError(f'Student with id {id} not in db')

def add_student(file_path, new_student):
    with open(file_path, "r+") as f:
        f.seek(0)
        school_data = json.load(f)
        all_students = school_data["students"]

        # make sure that this student does not already exist:
        for student in all_students:
            if student["id"] == new_student.id:
                return {"Error": f"student with id {new_student.id} already exists"}
        
        # let's add the new student
        all_students.append(dict(new_student))
        f.seek(0)        
        json.dump(school_data,f, indent=4)
        f.truncate()
        
        return new_student
