'''
File name: ebookstore.py

'''


import sqlite3



def create_database_and_table():
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()

    

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        qty INTEGER NOT NULL
    )
    """)

    

    cursor.execute("SELECT COUNT(*) FROM book")
    if cursor.fetchone()[0] == 0:
        initial_data = [
            (3001, "A Tale of Two Cities", "Charles Dickens", 30),
            (3002, "Harry Potter and the Philosopher's Stone", "J.K Rowling", 40),
            (3003, "The Lion, the Witch and the Wardrobe", "C.S Lewis", 25),
            (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
            (3005, "Alice in Wonderland", "Lewis Carroll", 12)
        ]
        cursor.executemany("INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)", initial_data)

    conn.commit()
    conn.close()



def add_book():
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()

    

    cursor.execute("SELECT MAX(id) FROM book")
    max_id = cursor.fetchone()[0]
    if max_id is None:
        new_id = 3001
    else:
        new_id = max_id + 1

    title = input("Enter book title: ")
    author = input("Enter author: ")
    qty = int(input("Enter quantity: "))

    cursor.execute("INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)", (new_id, title, author, qty))
    conn.commit()
    conn.close()
    print("Book added successfully!")



def update_book():
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()

    id = int(input("Enter book ID to update: "))
    qty = int(input("Enter new quantity: "))

    cursor.execute("UPDATE book SET qty = ? WHERE id = ?", (qty, id))
    conn.commit()
    conn.close()
    print("Book information updated successfully!")



def delete_book():
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()

    id = int(input("Enter book ID to delete: "))

    cursor.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    print("Book deleted successfully!")



def search_books():
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()

    keyword = input("Enter book title or author to search: ")
    cursor.execute("SELECT * FROM book WHERE title LIKE ? OR author LIKE ?", ('%' + keyword + '%', '%' + keyword + '%'))
    books = cursor.fetchall()

    if books:
        print("\nSearch Results:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")
    else:
        print("No matching books found.")

    conn.close()



if __name__ == "__main__":
    create_database_and_table()

    while True:
        print("\nMenu:")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            search_books()
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")