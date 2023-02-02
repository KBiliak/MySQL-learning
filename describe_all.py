from mysql.connector import connect

connection = connect(
        host="localhost",
        user="root",
        password="password",
        database="db"
)

describe_all_sql = "describe reviewers"

with connection.cursor() as cursor:
    cursor.execute(describe_all_sql)
    result = cursor.fetchall()
    for row in result:
        print(row)

# connection.close()
