from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engines = {
    'chamcong' : create_engine("mysql+mysqlconnector://chamcong:123456@localhost:3306/chamcong_db"),
    'chamcong_base' : create_engine("mysql+mysqlconnector://chamcong_base:123456@172.16.1.174:3306/chamcong_base_db")  
}

chamcong_session = sessionmaker(bind=engines["chamcong"], autocommit=False, autoflush=False)
base_session = sessionmaker(bind=engines["chamcong_base"], autocommit=False, autoflush=False)

Base = declarative_base()