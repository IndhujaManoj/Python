from sqlalchemy import create_engine,MetaData
engine=create_engine('mysql+pymysql://root:indhu23@localhost:3306/todo')
meta=MetaData()
con=engine.connect()


