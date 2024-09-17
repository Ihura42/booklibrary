import json
from datetime import datetime
import sys
import matplotlib.pyplot as plt

LIBRARY_FILE = 'library.json'

books = []
users = []
loans = []

def load_library():
    try:
        with open(LIBRARY_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'books': [], 'users': [], 'loans': []}

def save_library():
    library_data = {'books': books, 'users': users, 'loans': loans}
    with open(LIBRARY_FILE, 'w') as file:
        json.dump(library_data, file, indent=4)

def add_book(title, author, isbn):
    book = {'title': title, 'author': author, 'isbn': isbn, 'available': True}
    books.append(book)
    save_library()
    print(f"Book {title} was added")

def remove_book(title):
    for book in books:
        if book['title'] == title:
            books.remove(book)
            save_library()
            print(f"Book {title} was deleted")
            return
    print(f"Book '{title}' wasn't found")

def register_user(name, user_id):
    for user in users:
        if user['id'] == user_id:
            print("User is already registered")
            return
    users.append({'name': name, 'id': user_id, 'borrowed_books': []})
    save_library() 
    print(f"User {name} was registrated.")

def search_book(title="", author=""):
    found = False
    for book in books:
        if title and title.lower() in book['title'].lower():
            print(f"Book found: {book['title']} by {book['author']} (Available: {book['available']})")
            found = True
        elif author and author.lower() in book['author'].lower():
            print(f"Book found: {book['title']} by {book['author']} (Available: {book['available']})")
            found = True

    if found == False:
        print("No books found.")

def find_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    return 

def find_book(book_title):
    for book in books:
        if book['title'] == book_title:
            return book
    return 

def borrow_book(user_id, book_title):
    user = find_user(user_id)  
    if not user:
        print("User wasn't found.")
        return

    book = find_book(book_title)  
    if not book:
        print("Book wasn't found")
        return

    if not book['available']:
        print("The book is already borrowed")
        return

    book['available'] = False
    user['borrowed_books'].append(book_title)
    loans.append({'user_id': user_id, 'book_title': book_title, 'loan_date': datetime.now()})
    save_library()
    print(f"{user['name']} borrowed the book '{book_title}'.")

def plot_available_books_by_author():
    author_counts = {}
    for book in books:
        if book['available']:
            author = book['author']
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1

    authors = list(author_counts.keys())
    counts = list(author_counts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(authors, counts, color='skyblue')
    plt.xlabel('Authors')
    plt.ylabel('Number of Available Books')
    plt.title('Number of Available Books by Author')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_loans_by_user():
    user_loan_counts = {}
    for loan in loans:
        user_id = loan['user_id']
        if user_id in user_loan_counts:
            user_loan_counts[user_id] += 1
        else:
            user_loan_counts[user_id] = 1

    user_ids = list(user_loan_counts.keys())
    loan_counts = list(user_loan_counts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(user_ids, loan_counts, color='salmon')
    plt.xlabel('User IDs')
    plt.ylabel('Number of Borrowed Books')
    plt.title('Number of Borrowed Books by User')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

load_library()

while True:
    print('Library system')
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Register User")
    print("4. Search Book")
    print("5. Borrow Book")
    print("6. Plot Available Books by Author")
    print("7. Plot Loans by User")
    print("8. Exit")

    choice = input('What u want to do')
    if choice == '1':
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter isbn: ")
        add_book(title, author, isbn)

    if choice == '2':
        title = input('Enter title')
        remove_book(title)

    if choice == '3':
        name = input('Enter your name ')
        user_id = input('Enter your id ')
        register_user(name, user_id)

    if choice == '4':
        print('Search by 1. Title or 2. Author ')
        search_by = input('Enter your choice: ')
        if search_by == '1':
            title = input('Enter title: ')
            search_book(title=title)
        elif search_by == '2':
            author = input('Enter author: ')
            search_book(author=author)
        else:
            print('Invalid option')

    if choice == '5':
        user_id = input('Write your id')
        title = input('write title ')
        borrow_book(user_id, title)

    elif choice == '6':
        plot_available_books_by_author()

    elif choice == '7':
        plot_loans_by_user()

    elif choice == '8':
        print("Goodbye!")
        save_library()
        sys.exit()


