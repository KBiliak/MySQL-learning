import client_repository

def show_list_of_clients():
    print("List of all clients")
    result = client_repository.get_all_clients()
    for index, r in enumerate(result):
        print(f"{index + 1}.", r)


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
    client = get_client_data()
    client_repository.create_client(client)
    print(f"Successfully created client: {client}")




def handle_update_command():
    user_id = input("Enter id of client to update: ")
    new_data = get_client_data()
    client_repository.update_client(user_id, new_data)
    print(f"Successfully updated client with id: {user_id}")




def handle_delete_command():
    print("Delete a client")
    user_id = input("Enter id of client you want to delete: ")
    client_repository.handle_delete(user_id)



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
                show_list_of_clients()
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
