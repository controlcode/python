from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String

metadata = MetaData()

user_table = Table('user', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String),
                Column('fullname', String)
                )

print(user_table.name)
print(user_table.c.name)
print(user_table.c)
print(user_table.c.keys())
print(user_table.c['name'])

print(user_table.c.name.name)
print(user_table.c.name.type)

print(user_table.c.id.name)

print(user_table.primary_key)

#SQL Core expression language builds from metadata

print(user_table.select())
print(user_table.select().where(user_table.c.fullname == 'rich'))

engine = create_engine("postgresql://feedback:feedback@localhost:5432/feedback")
metadata.create_all(engine)
