from typing import List, Optional
from pydantic import BaseModel
from datetime import date, time


# class ItemBase(BaseModel):
#     title: str
#     description: Optional[str] = None

# class ItemCreate(ItemBase):
#     pass

# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


class UserCreate(BaseModel):
    DEPTNO: int
    DNAME: str
    Locid: int

class User(BaseModel):
    email: str
    hashed_password: str

    class Config:
        orm_mode = True


class DepartmentSchema(BaseModel):
    DEPTNO: int
    DNAME: str
    Locid: int

    class Config:
        orm_mode = True
        
class AppointmentSchema(BaseModel):
    appointment_id: Optional[int] = None
    appointment_date: date
    appointment_time: time
    patient_name: str
    patient_age: int
    additional_information: str

    class Config:
       orm_mode = True


class Doctor(BaseModel):
    id: Optional[int] = None
    name: str
    specialization: str

class Patient(BaseModel):
    patient_id: Optional[int] = None
    name: str
    email: str
    gender: str
    age: int
    address: str
    phone: str
    region: str
    date_of_birth: date

class Visits(BaseModel):
    visitid: int
    doctorid: int
    patientid:int
    dateofvisit: date
    timeofvisit: time

    class Config:
        orm_mode = True

class Doctor2schema(BaseModel):
    DoctorID: int
    DoctorAge: int
    DoctorName: str
    Descriptions: str
    ExperienceInYears: float
    PatientDealt: int
    ShiftStart: time
    ShiftEnd: time
    Specialty: str
    Designation: str
    Rating: str

    class Config:
        orm_mode = True

        
class LoginSchema(BaseModel):
    EmailAddress: str
    Passwords: str
 
    class Config:
        orm_mode = True


class Patient2schema(BaseModel):
    PatientID: int
    FullName: str
    Age: str
    Gender: str
    HomeAdress: str
    ContactInformation: str
    EmergencyContact: str

    class Config:
        orm_mode = True