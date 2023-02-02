from mysql.connector import connect


def create_connection():
    return connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="db"
    )


def get_all_books(connection):
    with connection.cursor() as cursor:
        cursor.execute("select * from book")
        return cursor.fetchall()


def insert_book(connection):
    with connection.cursor() as cursor:
        cursor.execute("insert into book (name, author, price) VALUE ("
                       "'Vitalii', 'Go', 4356)")
        connection.commit()


def update_book(connection, id):
    with connection.cursor() as cursor:
        cursor.execute(f"update book set name = 'Updated Name' where id = {id}")
        connection.commit()


def delete_book(connection, id):
    with connection.cursor() as cursor:
        cursor.execute(f"delete from book where id = {id}")
        connection.commit()


def print_books(books):
    for book in books:
        print(book)


connection = create_connection()
books = get_all_books(connection)
print_books(books)

print("Insert new book")
insert_book(connection)

books = get_all_books(connection)
print_books(books)

print("Update a book")
update_book(connection, 8)
books = get_all_books(connection)
print_books(books)

print("Delete a book")
delete_book(connection, 5)
books = get_all_books(connection)
print_books(books)

connection.close()
