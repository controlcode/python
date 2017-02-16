from sqlalchemy import create_engine

engine = create_engine("postgresql://feedback:feedback@localhost:5432/feedback")

connection = engine.connect()

result = connection.execute("select * from feedback_responses")

result.fetchall()
