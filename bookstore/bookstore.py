import client_repository
import book_repository


def main():

    while True:
        print("Bookshelf")
        print("Show all books - show all books on the shelf")
        print("Show all clients - show all clients in database")
        print("Create a book - create a new book")
        print("Create a client - create a new client")
        print("Update a book - update existing one book")
        print("Update a client - update existing one client")
        print("Delete a book - delete existing one book")
        print("Delete a client - delete existing one client")
        print("Exit - exit a program")

        command = input("Enter your action: ").capitalize()
        print(command)

        match command:
            case "Show all books":
                show_all_books()
            case "Show all clients":
                show_all_clients()
            case "Create a book":
                create_book()
            case "Create a client":
                create_client()
            case "Update a book":
                update_book()
            case "Update a client":
                update_client()
            case "Delete a book":
                delete_book()
            case "Delete a client":
                delete_client()
            case "Exit":
                print("Good luck")
                break
            case _:
                print("Unknown command, try again")



def book_data():
    name = input("Enter name of the book: ")
    author = input("Enter author of the book: ")
    price = input("Enter price of the book: ")
    genre = input("Enter genre of the book: ")
    return{
        "name": name,
        "author": author,
        "price": price,
        "genre": genre

    }
def client_data():
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

def create_book():
    print("Enter new book")
    book = book_data()
    book_repository.create_NewBook(book)

def create_client():
    print("Enter new client")
    client = client_data()
    client_repository.create_clientID(client)



def show_all_books():
    print("list of books")
    result = book_repository.show_books()
    for index, row in enumerate(result):
        print(index + 1, row)

def show_all_clients():
    print("list of clients")
    result = client_repository.show_all_clientsID()
    for index, row in enumerate(result):
        print(index+1, row)


def update_book():
    id_input = input("Enter id of book to update it: ")
    updated_book = book_data()
    book_repository.update_book_id(id_input, updated_book)

def update_client():
    id_input = input("Enter id of client to update it: ")
    updated_client = client_data()
    client_repository.update_clientID(id_input, updated_client)


def delete_book():
    id_input = input("Enter id of book to delete it: ")
    book_repository.delete_bookID(id_input)


def delete_client():
    print("Delete a client")
    delete_id = input("Enter ID of client you want to delete: ")
    client_repository.delete_clientID(delete_id)

main()