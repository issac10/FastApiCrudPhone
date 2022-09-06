
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

phones = Table("phones", meta, Column(
    "id", Integer, primary_key=True), 
    Column("brand", String(255)),
    Column("model", String(255)),
    Column("price", Integer),
    Column("stock", Integer))
meta.create_all(engine)