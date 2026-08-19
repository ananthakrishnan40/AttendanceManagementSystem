from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text

user = 'root'
password = 'deepas'
database = 'AttendenceManagement'


URL = f'mysql+pymysql://{user}:{password}@localhost:3306/{database}'

engine = create_engine(URL)
sessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)
Base = declarative_base()