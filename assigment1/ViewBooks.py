from LinkedList import LinkedList

books_list = LinkedList()

def view_books():
    if books_list.is_empty():
        print("No books available.")
    else:
        print("Bid | Title | Author | Status")
        print("-----------------------------")
        books_list.display()
