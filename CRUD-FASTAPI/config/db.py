from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:Univalle@localhost:3306/phonedb")

meta = MetaData()

conn = engine.connect()