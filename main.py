from fastapi import FastAPI, Cookie, Header
import uvicorn
from enum import Enum
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Department(str, Enum):
    IT = "IT"
    Programming = "Programming"
    Database = "Database"


class Gender(str, Enum):
    Male = "Male"
    Female = "Female"


class Student(BaseModel):
    id: int
    department: Department
    name: str
    age: int
    gender: Optional[Gender] = None


class Student_info(Student):
    id: int
    department = Department
    name = str


@app.get("/status")
def check_status():
    return f"Hello World!"


@app.get("students/{student_id}")
def check_students(student_id: int, department: Department, gender: str = None):
    return f"list of students"


@app.post("/students", response_model=Student)
def create_student(student: Student):
    print(student)
    return student


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
