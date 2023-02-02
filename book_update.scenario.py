from mysql.connector import connect

def create_connection():
    return connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="db"
    )

def read_book(connection):
    with connection.cursor() as cursor:
        cursor.execute("select * from book")
        rows = cursor.fetchall()
        result = []
        for row in rows:
            book = {
                "name": row[0],
                "author": row[1],
                "price": row[2],
                "id": row[3]
            }
            result.append(book)
        return result

def update_price(connection, id, price):
    with connection.cursor() as cursor:
        cursor.execute(f"Update book set price = {price} where id = {id}")
        connection.commit()


connection = create_connection()
books = read_book(connection)

for book in books:
    name = book["name"]
    author = book["author"]
    price = book["price"]
    print("Book:", book)
    id = book['id']
    print(f"price = {price}, id = {id}")
    price = price + 10
    update_price(connection, id, price)

books = read_book(connection)
print("Books: ", books)

