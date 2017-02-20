from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy import Integer, String
from sqlalchemy import and_, or_

metadata = MetaData()

#use logging shortcut
engine = create_engine("postgresql://feedback:feedback@localhost:5432/feedback", echo=True)

user_table = Table('my_users', metadata,
                Column('id', Integer, primary_key=True),
                Column('username', String(50)),
                Column('fullname', String(50))
                )

metadata.create_all(engine)

#sqlalchemy

print(user_table.c.username.__class__.__mro__)

#special comparator method
#print(user_table.c.user.__eq__)

print(
    (user_table.c.username == 'ed') | (user_table.c.username == 'jack')
)

print(
    and_(
        user_table.c.fullname == 'rich',
            or_(
                user_table.c.username == 'richard',
                user_table.c.username == 'dan'
                )
            )
        )

print(user_table.c.id > 5)

print(user_table.c.fullname == None)

# "+" might mean addition or string concatenation

print(user_table.c.id + 5)
print(user_table.c.fullname + "some name")

print(user_table.c.username.in_(["wendy", "mary"]))

expression = user_table.c.username == "rich"
print(expression)
compiled = expression.compile()
print(compiled.params)

result = engine.execute(
    user_table.select().where(user_table.c.username == "rich")
)
print(result)

# Postgresql dialect

from sqlalchemy.dialects import postgresql

print(expression.compile(dialect=postgresql.dialect()))

#inserts
'''
insert_stmt = user_table.insert().values(username='rich', fullname='Richard Weeks')
conn = engine.connect()
result = conn.execute(insert_stmt)

conn.execute(user_table.insert(), [
    {'username' : 'jack', 'fullname' : 'Jack Sparrow'},
    {'username' : 'alice', 'fullname' : 'Alice Cooper'}
])
'''
from sqlalchemy import select
conn = engine.connect()
select_stmt = select([user_table.c.username, user_table.c.fullname]).\
    where(user_table.c.username == 'jack')

result = conn.execute(select_stmt)

for row in result:
    print(row)

print(conn.execute(select([user_table])).fetchall())

#update

update_stmt = user_table.update().\
                values(fullname='Jack Brown').\
                where(user_table.c.username == 'jack')

result = conn.execute(update_stmt)

delete_stmt = user_table.delete().\
                where(user_table.c.username == 'jack')

result = conn.execute(delete_stmt)
