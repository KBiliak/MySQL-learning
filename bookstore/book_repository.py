from mysql.connector import connect

def create_connection():
    return connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="db"
    )

def create_NewBook(book):
    connection = create_connection()
    with connection.cursor() as cursor:
        sql = f"insert into bookstore(name, author, price, genre) " \
              f"value"\
               f"('{book['name']}', " \
               f"'{book['author']}', " \
               f"'{book['price']}', " \
               f"'{book['genre']}')"
        cursor.execute(sql)
        connection.commit()
    connection.close()


def show_books():
    connection = create_connection()
    with connection.cursor() as cursor:
        cursor.execute("select * from bookstore")
        rows = cursor.fetchall()
        result = []
        for row in rows:
            book = {
                "id": row[0],
                "name": row[1],
                "author": row[2],
                "price": row[3],
                "genre": row[4]

            }
            result.append(book)
    connection.close()
    return result

def update_book_id(id_input, book):
    connection = create_connection()

    sql = f"Update bookstore set " \
          f"name = '{book['name']}', " \
          f"author = '{book['author']}', " \
          f"price = '{book['price']}', " \
          f"genre = '{book['genre']}' " \
          f"where id = {id_input}"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        connection.commit()
    connection.close()

def delete_bookID(id_input):
    connection = create_connection()
    with connection.cursor() as cursor:
        sql = f"delete from bookstore where id = {id_input}"
        cursor.execute(sql)
        connection.commit()
    connection.close()





