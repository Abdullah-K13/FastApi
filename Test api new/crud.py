from sqlalchemy import Date
from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session):
    return (
        db.query(models.User)
        .all()
    )


def create_dept(db: Session, user: schemas.DepartmentSchema):
    db_dept = models.Department(
        DEPTNO=user.DEPTNO, DNAME=user.DNAME,Locid = user.Locid
    )
    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept



def create_appointment(db: Session, user: schemas.AppointmentSchema):
    db_appt = models.Appointment(
        appointment_date=user.appointment_date, appointment_time=user.appointment_time,patient_name = user.patient_name,patient_age=user.patient_age,
        additional_information = user.additional_information
    )
    db.add(db_appt)
    db.commit()
    db.refresh(db_appt)
    return db_appt

def get_time_by_dates(db: Session,doctorid:int,date:Date):
    return db.query(models.Visits).filter((models.Visits.doctorid == doctorid) & (models.Visits.dateofvisit == date)).all()




def fetch_doctor2by_id(db: Session,docid:int):
    return db.query(models.Doctor2model).filter(models.Doctor2model.DoctorID == docid).all()

def fetch_alldoctors_byspecs(db: Session,specialty:str):
    return db.query(models.Doctor2model).filter(models.Doctor2model.Specialty == specialty).all()

def fetch_loginInfo(db: Session,emailaddress:str):
    return db.query(models.LoginModels).filter(models.LoginModels.EmailAddress == emailaddress).first()



def fetch_patientInformation(db: Session,patinetid:int):
    return db.query(models.Patient2Model).filter(models.Patient2Model.PatientID == patinetid).first()


def update_patient_information(db: Session, patientid: int, updated_patient_info: schemas.Patient2schema):
    # Retrieve the patient from the database
    db_patient = db.query(models.Patient2Model).filter(models.Patient2Model.PatientID == patientid).first()
    
    # Check if the patient exists
    if db_patient is None:
        return None  # Patient not found
    
    # Update patient information with the provided data
    db_patient.FullName = updated_patient_info.FullName
    db_patient.Age = updated_patient_info.Age
    db_patient.Gender = updated_patient_info.Gender
    db_patient.HomeAdress = updated_patient_info.HomeAdress
    db_patient.ContactInformation = updated_patient_info.ContactInformation
    db_patient.EmergencyContact = updated_patient_info.EmergencyContact
    
    # Commit the changes to the database
    db.commit()
    
    # Return the updated patient information
    return db_patient

# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return (
#         db.query(models.Item)
#         .order_by(models.Item.id)
#         .offset(skip)
#         .limit(limit)
#         .all()
#     )


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item


# def get_all_Department():
#     session = Session()
#     employees = session.query(models.Department).all()
#     session.close()
#     return employees