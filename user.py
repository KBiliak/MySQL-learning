from mysql.connector import connect


def create_connection():
    return connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="db"
    )

def creat_user(connection):
    with connection.cursor() as cursor:
        cursor.execute("insert into user (first_name, last_name, age) VALUE "
                       "('Kateryna', 'Biliak', 22)")
        connection.commit()

def read_user(connection):
    with connection.cursor() as cursor:
        cursor.execute("select * from user")
        return cursor.fetchall()

def update_user(connection, id):
    with connection.cursor() as cursor:
        cursor.execute(f"Update user set first_name = 'Qwert' where id = {id}")
        connection.commit()

def delete_user(connection, id):
    with connection.cursor() as cursor:
        cursor.execute(f"delete from user where id = {id}")
        connection.commit()

def print_user(user):
    for u in user:
        print(u)


connection = create_connection()
users = read_user(connection)
print_user(users)

print("Insert new user")
creat_user(connection)

users = read_user(connection)
print_user(users)

print("Update user:")
update_user(connection, 36)
users = read_user(connection)
print_user(users)

print("Delete a user")
delete_user(connection, 35)
users = read_user(connection)
print_user(users)
