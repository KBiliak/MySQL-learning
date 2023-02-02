from mysql.connector import connect

def create_connection():
    return connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="db"
    )

#
# def get_user_input():
#     user_input = input(
#         "Enter your first name, last name, age devided by comma: ")
#     user_input_list = user_input.split(",")
#     print(user_input_list)
#     return {
#         "first_name": user_input_list[0],
#         "last_name": user_input_list[1],
#         "age": user_input_list[2]
#     }


def get_new_user_input():
    first_input = input(
        "Enter new first name: ")
    last_input = input(
        "Enter new last name: ")
    age = input(
        "Enter new age: ")
    id = input("Enter your id: ")


    return {
        "first_name": first_input ,
        "last_name": last_input,
        "age": age,
        "id": id
    }

def insert_user(connection, user):
    with connection.cursor() as cursor:
        sql = f"insert into user(first_name, last_name, age) " \
              f" value ('{user['first_name']}', '{user['last_name']}', {user['age']})"
        print(sql)
        cursor.execute(sql)
        connection.commit()

def update_user(connection, user):
    print('update_user user: ', user)
    with connection.cursor() as cursor:
        sql = f"Update user set first_name = '{user['first_name']}'," \
              f" last_name = '{user['last_name']}', age = {user['age']} where id = {user['id']}"
        print(sql)
        cursor.execute(sql)
        connection.commit()



def read_user(connection):

    with connection.cursor() as cursor:
        cursor.execute("select * from user")
        rows = cursor.fetchall()
        result = []
        for row in rows:
            user = {
                "first_name" : row[0],
                "last_name" : row[1],
                "age": row[2],
                "id": row[3]
            }
            result.append(user)

        return result



connection = create_connection()
user = get_new_user_input()
print('user:', user)
# insert_user(connection, user)
# users = read_user(connection)
# print(users)


print("Update user:")
update_user(connection, user)
users = read_user(connection)
print(users)