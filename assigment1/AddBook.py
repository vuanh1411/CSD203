from LinkedList import LinkedList

books_list = LinkedList()

def add_book():
    bid = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    status = '0'  # Initially available

    book_info = f"{bid} | {title} | {author} | {status}"
    books_list.append(book_info)
    print("Book added successfully.")
