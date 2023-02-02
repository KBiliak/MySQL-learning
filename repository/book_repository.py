from mysql.connector import connect


def create_connection():
    return connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="db"
    )


def create_book(book):
    connection = create_connection()
    with connection.cursor() as cursor:
        sql = f"insert into bookshelf( book_name, author, price, rate) " \
              f"value " \
              f"('{book['book_name']}', " \
              f"'{book['author']}'," \
              f"'{book['price']}', " \
              f"'{book['rate']}')"
        cursor.execute(sql)
        connection.commit()
    connection.close()


def update_book(id, book):
    connection = create_connection()

    sql = f"Update bookshelf set book_name = '{book['book_name']}', " \
          f"author ='{book['author']}'," \
          f"price = '{book['price']}'," \
          f"rate = '{book['rate']}' " \
          f"where id = {id}"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        connection.commit()
    connection.close()


def delete_book(id):
    connection = create_connection()
    with connection.cursor() as cursor:
        sql = f"delete from bookshelf where id = {id}"
        cursor.execute(sql)
        connection.commit()
    connection.close()


def get_all_books():
    connection = create_connection()
    with connection.cursor() as cursor:
        cursor.execute("select * from bookshelf")
        rows = cursor.fetchall()
        result = []
        for row in rows:
            book = {
                "id": row[0],
                "book_name": row[1],
                "author": row[2],
                "price": row[3],
                "rate": row[4]
            }
            result.append(book)
        connection.close()
        return result