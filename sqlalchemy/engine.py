from sqlalchemy import create_engine

engine = create_engine("postgresql://feedback:feedback@localhost:5432/feedback")

result = engine.execute("select * from feedback_responses")

result.fetchall()
