from mysql.connector import connect


def create_connection():
    return connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="db"
    )


def get_all_clients(connection):
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
        return result


def handle_list_command():
    print("List of all clients")
    connection = create_connection()
    result = get_all_clients(connection)
    for index, r in enumerate(result):
        print(f"{index + 1}.", r)
    connection.close()


def get_client_data():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    return {
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "email": email
    }


def handle_create_command():
    print("Enter new client data below.")
    connection = create_connection()
    client = get_client_data()
    with connection.cursor() as cursor:
        sql = f"insert into client(first_name, last_name, phone, email)" \
              f" VALUE " \
              f"('{client['first_name']}', '{client['last_name']}', '{client['phone']}', '{client['email']}')"
        cursor.execute(sql)
        connection.commit()
    connection.close()

    print(f"Successfully created client: {client}")


def handle_update_command():
    connection = create_connection()
    user_id = input("Enter id of client to update: ")
    new_data = get_client_data()

    sql = f"Update client set first_name = '{new_data['first_name']}'," \
              f" last_name = '{new_data['last_name']}', phone = {new_data['phone']}," \
          f" email = '{new_data['email']}'  where id = {user_id}"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        connection.commit()
    connection.close()
    print(f"Successfully updated client with id: {user_id}")



def handle_delete_command():
    print("Delete a client")
    connection = create_connection()
    user_id = input("Enter id of client you want to delete: ")
    with connection.cursor() as cursor:
        sql = f"delete from client where id = {user_id}"
        print(sql)
        cursor.execute(sql)
        connection.commit()
    connection.close()



def main():
    print("Client store v1")
    while True:
        print("Possible commands:")
        print("    list - list all clients in the store")
        print("    create - create a new client")
        print("    update - update a new client by id")
        print("    delete - update a new client by id")
        print("    exit - stop program")
        command = input("Enter command: ")
        match command:
            case "list":
                handle_list_command()
            case "create":
                handle_create_command()
            case "update":
                handle_update_command()
            case "delete":
                handle_delete_command()
            case "exit":
                print("Good bye")
                break


main()
