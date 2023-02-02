import book_repository


def book_data():
    print("Bookshelf")
    book_name = input("Enter name of the book: ")
    author = input("Enter author of the book: ")
    price = input("Enter price of the book: ")
    rate = input("Enter rate of the book: ")
    return {
        "book_name": book_name,
        "author": author,
        "price": price,
        "rate": rate
    }


def create_book_command():
    print("Enter new book: ")
    book = book_data()
    book_repository.create_book(book)


def show_all_books_command():
    print("List of all books")
    result = book_repository.get_all_books()
    for index, row in enumerate(result):
        print(f"{index + 1}.", row)


def update_book_command():
    user_id = input('Enter id of book to update it: ')
    new_data = book_data()
    book_repository.update_book(user_id, new_data)


def delete_book_command():
    delete_id = input("Enter a book by id: ")
    book_repository.delete_book(delete_id)


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
                show_all_books_command()
            case "create":
                create_book_command()
            case "update":
                update_book_command()
            case "delete":
                delete_book_command()
            case "exit":
                print("Good bye")
                break

main()

