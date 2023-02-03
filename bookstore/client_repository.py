from mysql.connector import connect

def create_connection():
    return connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="db"
    )

def show_all_clientsID():
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

def create_clientID(client):
    connection = create_connection()
    with connection.cursor() as cursor:
        sql = (f"insert into client(first_name, last_name, phone, email)"
               f"value('{client['first_name']}', "
               f"'{client['last_name']}', "
               f"'{client['phone']}',"
               f"'{client['email']}')")
        cursor.execute(sql)
        connection.commit()
    connection.close()

def update_clientID(id_input,updated_client):
    connection = create_connection()
    with connection.cursor() as cursor:
        sql = (f"Update client set first_name = '{updated_client['first_name']}'," \
          f" last_name = '{updated_client['last_name']}', phone = {updated_client['phone']}," \
          f" email = '{updated_client['email']}'  where id = {id_input}")
        cursor.execute(sql)
        connection.commit()
    connection.close()

def delete_clientID(delete_id):
    connection = create_connection()
    with connection.cursor() as cursor:
        sql = f"delete from client where id = {delete_id}"
        cursor.execute(sql)
        connection.commit()
    connection.close()


