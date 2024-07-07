"""
This file will be used as database
"""

students = {
    1: {"name":"chaitanya", 
        "age":25,
        "education": "IITM"},
    2:{"name":"sudeer kumar", 
        "age":23,
        "education": "IITB"}
}

def get_student_with_id_and_name(student_id, name):
    if student_id in students:
        student = students[student_id]
        if student["name"] == name:
            return student
    return {"status": "data not matching"}

def get_student_by_name(name:str) -> dict:
    for student_id, student in students.items():
        if student["name"] == name:
            return student
    return {"status": "Student not found"}


def get_student(id: int) -> dict:
    if id in students:
        return students[id]
    else:
        return {"status":"not found"}


def get_student_name(id: int) -> str:
    if id in students:
        return students[id]["name"]
    return {"status": "student not found"}