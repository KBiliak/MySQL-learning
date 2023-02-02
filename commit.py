from mysql.connector import connect

with connect(
    host="localhost",
    user="root",
    password="password",
    database="db"
) as connection:
    create_ratings_table_query = """
    CREATE TABLE ratings (
        movie_id INT,
        reviewer_id INT,
        rating DECIMAL(2,1),
        FOREIGN KEY(movie_id) REFERENCES movies(id),
        FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
        PRIMARY KEY(movie_id, reviewer_id)
    )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_ratings_table_query)
        connection.commit()
