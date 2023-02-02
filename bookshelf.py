from mysql.connector import connect

def create_connection():
    return connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="db"
    )

def book_data():
    print("Bookshelf")
    book_name = input("Enter name of the book: ")
    author = input("Enter author of the book: ")
    price = input("Enter price of the book: ")
    rate = input("Enter rate of the book: ")
    return{
        "book_name": book_name,
        "author": author,
        "price": price,
        "rate": rate
    }


def create_book():
    print("Enter new book: ")
    connection = create_connection()
    bookshelf = book_data()
    with connection.cursor() as cursor:
        sql = f"insert into bookshelf( book_name, author, price, rate) " \
              f"value " \
              f"('{bookshelf['book_name']}', " \
              f"'{bookshelf['author']}'," \
              f"'{bookshelf['price']}', " \
              f"'{bookshelf['rate']}')"
        cursor.execute(sql)
        connection.commit()
    connection.close()


def get_all_books(connection):
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
        return result

def show_all_books():
    print("List of all books")
    connection = create_connection()
    result = get_all_books(connection)
    for index, row in enumerate(result):
        print(f"{index + 1}.", row)
    connection.close()


def update_book():
    connection = create_connection()
    user_id = input('Enter id of book to update it: ')
    new_data = book_data()

    sql = f"Update bookshelf set book_name = '{new_data['book_name']}', " \
          f"author ='{new_data['author']}'," \
          f"price = '{new_data['price']}'," \
          f"rate = '{new_data['rate']}' " \
          f"where id = {user_id}"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        connection.commit()
    connection.close()



def delete_book():
    delete_id = input("Enter a book by id")
    connection = create_connection()
    with connection.cursor() as cursor:
        sql = f"delete from bookshelf where id = {delete_id}"
        cursor.execute(sql)
        connection.commit()
    connection.close()

def main():
    while True:
        print("show all - Show all books on the shelf")
        print("create - add new book to the shelf")
        print("update = update existing book on the shelf")
        print("delete - delete existing book on the shelf")
        print("exit - to close the program")
        command = input("Enter your command: ")

        match command:
            case "show all":
                show_all_books()

            case "create":
                create_book()
            case "update":
                update_book()
            case "delete":
                delete_book()
            case "exit":
                print("Good bye")
                break

main()

