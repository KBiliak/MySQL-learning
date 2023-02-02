from mysql.connector import connect


def create_connection():
    return connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="db"
    )

def read_users(connection):
    with connection.cursor() as cursor:
        cursor.execute("select * from user")
        rows = cursor.fetchall()
        result = []
        for row in rows:
            user = {
                "first_name": row[0],
                "last_name": row[1],
                "age": row[2],
                "id": row[3]
            }
            result.append(user)
        return result


def update_user(connection, id, age):
    with connection.cursor() as cursor:
        cursor.execute(f"Update user set age = {age} where id = {id}")
        connection.commit()


connection = create_connection()
users = read_users(connection)

for user in users:
    age = user['age']
    id = user['id']
    print("User:", user)
    print(f"age = {age}, id = {id}")
    age = age + 1
    update_user(connection, id, age)


users = read_users(connection)
print("Users:", users)