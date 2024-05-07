from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = ("mssql+pyodbc://admin:12345@localhost/EmployeeData?driver=ODBC+Driver+18+for+SQL+Server&Trusted_Connection=No&TrustServerCertificate=Yes")


# SQLALCHEMY_DATABASE_URL = ("mssql+pyodbc://admin:12345@localhost/EmployeeData?driver=ODBC+Driver+18+for+SQL+Server&Trusted_Connection=No&TrustServerCertificate=Yes")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args={"check_same_thread": False},  # only needed for SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
