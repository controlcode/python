import psycopg2

connection = psycopg2.connect("dbname='feedback' user='feedback' host='localhost' password='feedback'")

cursor = connection.cursor()

cursor.execute("select * from feedback_responses")

feedback = cursor.fetchone()[1]

cursor.close()

cursor = connection.cursor()

cursor.execute("ionnection.execute("insert into feedback_responses values('2', 'Bad', 'Bad', 'New', '17/02/2017')")

cursor.close()

connection.commit()
