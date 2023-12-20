from fastapi import FastAPI
from Schemas.student import Student
from config.db import con
from models.index import students
from sqlalchemy import select
app=FastAPI()

# @app.get("/students")
# async def index():
#     data=con.execute(students.select()).fetchall()
#     return{
#          "success":True,
#         "data":data
#     }




@app.post('/students')
async def store(student: Student):
    data = con.execute(students.insert().values(
        name=student.name,
        email=student.email,
        country=student.country
    ))
    if data.rowcount == 1:
        return {
            "success": True,
            "msg": 'Student Stored Successfully'
        }
    else:
        return {
            "success": False,
            "msg": 'Student Storage Failed'
        }


@app.get('/students')
async def get_students():
    query = select([students.c.name, students.c.email, students.c.country]).where(students.c.source == "API")
    result = con.execute(query)
    students_list = result.fetchall()
    return students_list
