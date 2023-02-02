from mysql.connector import connect


def create_connection():
    return connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="db"
    )

def get_all_clients():
    connection = create_connection()
    with connection.cursor() as cursor:
        cursor.execute("select * from client")
        rows = cursor.fetchall()
        result = []
        for row in rows:
            client = {
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "phone": row[3],
                "email": row[4]
            }
            result.append(client)
        connection.close()
        return result

def create_client(client):
    connection = create_connection()
    with connection.cursor() as cursor:
        sql = f"insert into client(first_name, last_name, phone, email)" \
              f" VALUE " \
              f"('{client['first_name']}', '{client['last_name']}', '{client['phone']}', '{client['email']}')"
        cursor.execute(sql)
        connection.commit()
    connection.close()


def update_client(user_id, new_data):
    connection = create_connection()
    sql = f"Update client set first_name = '{new_data['first_name']}'," \
          f" last_name = '{new_data['last_name']}', phone = {new_data['phone']}," \
          f" email = '{new_data['email']}'  where id = {user_id}"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        connection.commit()
    connection.close()


def delete_client(user_id):
    connection = create_connection()

    with connection.cursor() as cursor:
        sql = f"delete from client where id = {user_id}"
        print(sql)
        cursor.execute(sql)
        connection.commit()
    connection.close()