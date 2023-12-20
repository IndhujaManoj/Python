from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE='mysql+pymysql://root:indhu23@localhost:3306/BlogApplication'

engine=create_engine(URL_DATABASE)

sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()