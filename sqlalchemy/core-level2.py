from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, DateTime, Enum, Numeric, ForeignKey

import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

metadata = MetaData()

user_table = Table('user', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String),
                Column('fullname', String)
                )

address_table = Table('address', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('email', String(100), nullable=False),
                    Column('user_id', Integer, ForeignKey('user.id'))
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

fancy_table = Table('fancy', metadata,
                Column('key', String(50), primary_key=True),
                Column('timestamp', DateTime),
                Column('amount', Numeric(10, 2)),
                Column('type', Enum('a', 'b', 'c', name='type'))
                )
#this will throw exception if table or type already exists, so use check first
fancy_table.create(engine, checkfirst=True)
fancy_table.drop(engine)
metadata.create_all(engine)
