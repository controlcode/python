from sqlalchemy import create_engine

engine = create_engine("postgresql://feedback:feedback@localhost:5432/feedback")

connection = engine.connect()

result = connection.execute("select * from feedback_responses")

result.fetchall()

#class sqlalchemy.engine.result.RowProxy
row = result.fetchone()
#print the row keys
print(row.keys())

#iterate result set
for row in result:
    print(row)

result.close()
