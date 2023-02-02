from mysql.connector import connect

with connect(
        host="localhost",
        user="root",
        password="password",
        database="db"
) as connection:
    create_reviewers_table_query = """
    CREATE TABLE reviewers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100)
    )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_reviewers_table_query)
        connection.commit()