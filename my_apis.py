from fastapi import FastAPI, Path
from students import get_student, get_student_name, get_student_by_name, get_student_with_id_and_name, list_students, append_student
from student_model import Student
app = FastAPI()

@app.get("/")
def index():
    """
    Base url
    """
    return {"status":"EndPoint connected"}

@app.get("/healthCheck")
def healtCheck():
    """
    Verifies server deployed and configured properly
    """
    return {"status":"healthy"}

# path params 
# {server-ip}/path/{path_param}
@app.get("/getStudentDetail/{student_id}")
def get_student_detail(student_id:int = Path(description="Requires student id")):
    return get_student(student_id)

@app.get("/getStudentName/{student_id}")
def get_student_name_endpoint(student_id:int = Path(description="Requires student id")):
    return get_student_name(student_id)

# Query params
# {server-ip}/path?name=chaitanya
@app.get("/getStudentDetailByName")
def get_student_detail_by_name(name: str = "chaitanya"):
    """
    arguments are treated as query param, if you want to make them as optional provide default values
    """
    return get_student_by_name(name)

# Combining Path param and query param
# Dont create the same path name though you have different set of arguments, fast api is taking the latest endpoint
@app.get("/getStudentDetailByIdName/{student_id}")
def get_student_detail_with_id_name(student_id: int, name: str):
    return get_student_with_id_and_name(student_id, name)


@app.get("/listAllStudents")
def list_all_students():
    return list_students()


# Post methods
@app.post("/addStudent/{student_id}")
def add_student(student_id: int, student: Student):
    return append_student(student_id, student)
