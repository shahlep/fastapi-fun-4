from fastapi import FastAPI
import uvicorn
from enum import Enum

app = FastAPI()


class Department(str, Enum):
    IT = 'IT'
    Prorgrammin = 'Programming'
    Database = 'Database'


@app.get('/status')
def check_status():
    return f'Hello World!'


@app.get('students/{student_id}')
def check_students(student_id: int, department: Department, gender: str = None):
    return f'list of students'


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
