from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pyodbc

app = FastAPI()

DATABASE_URL = "mssql+pyodbc://admin:12345@localhost/EmployeeData?driver=ODBC+Driver+18+for+SQL+Server&Trusted_Connection=No&TrustServerCertificate=Yes"
engine = create_engine(DATABASE_URL)

name = ['abd']

# SQLALCHEMY_DATABASE_URL = ("mssql+pyodbc://admin:12345@localhost/EmployeeData?driver=ODBC+Driver+18+for+SQL+Server&Trusted_Connection=No&TrustServerCertificate=Yes")

@app.get("/")
def read_root():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT @@VERSION"))
        row = result.fetchone()
        return {"database_version": row[0]}

@app.get("/Emp")
def read_movie_table():
    with engine.connect() as conn:
        column_names = [column[0] for column in conn.execute(text("SELECT * FROM dept where deptno = 10 ")).keys()]
        result = conn.execute(text("SELECT * FROM dept where deptno = 10"))
        rows = result.fetchall()
        data = [dict(zip(column_names, row)) for row in rows]
        return {"data": data}

@app.post("/dept")
def create_dept(Deptno: int, dname: str, locid: int, db: Session):
    db.execute(
        dept.insert().values(
            Deptno=Deptno,
            dname=dname,
            locid=locid,
        )
    )
    db.commit()
    return {"message": "Department added successfully"}
# @app.get("/")
# def read_root():
#     return {"messagea": "Hello, FastAPI!"}

