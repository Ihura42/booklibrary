from datetime import datetime

books = [
    {'title': '1984', 'author': 'George Orwell', 'isbn': '9780451524935', 'available': True},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'isbn': '9780060935467', 'available': True}
]

users = [
    {'name': 'Alice', 'id': 'U12345', 'borrowed_books': []},
    {'name': 'Bob', 'id': 'U67890', 'borrowed_books': []}
]


loans = [
    {'user_id': 'U12345', 'book_title': '1984', 'loan_date': datetime(2024, 9, 10)}
]

def add_book(title, author, isbn, available=True):
    new_book = {
        'title': title,
        'author': author,
        'isbn': isbn,
        'available': available
    }
    books.append(new_book)
    print(f"Book '{title}' added to the system.")

def remove_book(books, title):
    new_books = []
    for book in books:
        if book['title'] != title:
            new_books.append(book)
    books[:] = new_books

    print(f"Book '{title}' removed.")

def register_user(name, user_id):
    for user in users:
        if user['id'] == user_id:
            print(f"User ID '{user_id}' already exists.")
            return
    new_user = {
        'name': name,
        'id': user_id,
        'borrowed_books': []
    }
    users.append(new_user)
    print(f"User '{name}' registered with ID '{user_id}'.")


def search_books(title=None, author=None):
    for book in books:
        if (title and title in book['title']) or (author and author in book['author']):
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Available: {book['available']}")
            return
    print("No books found.")

def find_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    return None

def find_book(book_title):
    for book in books:
        if book['title'] == book_title:
            return book
    return None

def borrow_book(user_id, book_title):
    user = find_user(user_id)  
    book = find_book(book_title)  

    if user is None:  
        print(f"User with ID '{user_id}' not found.")
        return

    if book is None: 
        print(f"Book '{book_title}' not found.")
        return

    if not book['available']:  
        print(f"Book '{book_title}' is already borrowed.")
        return


    user['borrowed_books'].append(book_title)  
    book['available'] = False  
    loans.append({'user_id': user_id, 'book_title': book_title, 'loan_date': datetime.now()})  
    print(f"Book '{book_title}' successfully borrowed by {user['name']}.")


add_book('The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565')

#delete book
remove_book(books, 'To Kill a Mockingbird')

#register new user
register_user('Charlie', 'U54321')

#find book by name
search_books(title='1984')

#find book by author
search_books(author='George Orwell')

# borrow book
borrow_book('U54321', '1984')

# lists 
print("\nCurrent books in the system:", books)
print("\nCurrent users in the system:", users)
print("\nCurrent loans in the system:", loans)




