from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL = ''

engine = create_engine(URL,connect_args={'check_same_thread':False})
sessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)
Base = declarative_base()