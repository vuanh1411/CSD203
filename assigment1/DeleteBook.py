from LinkedList import LinkedList

books_list = LinkedList()

def delete_book():
    bid = input("Enter book ID to delete: ")
    if books_list.delete_node(bid):
        print(f"Book with ID {bid} deleted successfully.")
    else:
        print(f"Book with ID {bid} not found.")
