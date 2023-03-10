from mysql.connector import connect

with connect(
    host="localhost",
    user="root",
    password="password",
    database="db"
) as connection:
    create_movies_table_query = """
    CREATE TABLE movies(
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100),
        release_year YEAR(4),
        genre VARCHAR(100),
        collection_in_mil INT
    )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_movies_table_query)
        connection.commit()