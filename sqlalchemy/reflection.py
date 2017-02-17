from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, DateTime, Enum, Numeric, ForeignKey
from sqlalchemy import inspect

import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

metadata = MetaData()
engine = create_engine("postgresql://feedback:feedback@localhost:5432/feedback")

'''
user_table = Table('user', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String),
                Column('fullname', String)
                )

fancy_table = Table('fancy', metadata,
                Column('key', String(50), primary_key=True),
                Column('timestamp', DateTime),
                Column('amount', Numeric(10, 2)),
                Column('type', Enum('a', 'b', 'c', name='type'))
                )
address_table = Table('address', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('email', String(100), nullable=False),
                    Column('user_id', Integer, ForeignKey('user.id'))
                    )
'''

user_reflected = Table('user', metadata, autoload=True, autoload_with=engine)

print(user_reflected.c)

inspector = inspect(engine)

print(inspector.get_table_names())
print(inspector.get_columns('user'))
print(inspector.get_foreign_keys('address'))
