# Library Book Management

books = [
    {"title": "Python Basics", "author": "John", "available": 5, "borrowed": 12},
    {"title": "Data Structures", "author": "Alice", "available": 0, "borrowed": 18},
    {"title": "Machine Learning", "author": "Bob", "available": 3, "borrowed": 25},
    {"title": "Database Systems", "author": "David", "available": 0, "borrowed": 10},
    {"title": "Computer Networks", "author": "Emma", "available": 7, "borrowed": 15}
]

# Find the most borrowed book
most_borrowed = max(books, key=lambda x: x["borrowed"])

print("Most Borrowed Book")
print("Title :", most_borrowed["title"])
print("Author:", most_borrowed["author"])
print("Borrowed Count:", most_borrowed["borrowed"])

# Display books with zero available copies
print("\nBooks with Zero Available Copies")
for book in books:
    if book["available"] == 0:
        print(book["title"])

# Calculate total books available
total_available = sum(book["available"] for book in books)
print("\nTotal Books Available:", total_available)

# Sort books by popularity (borrowed count)
books.sort(key=lambda x: x["borrowed"], reverse=True)

print("\nBooks Sorted by Popularity")
for book in books:
    print(book["title"], "-", book["borrowed"])

# Summary Report
print("\nLibrary Summary Report")
for book in books:
    print("----------------------------")
    print("Title      :", book["title"])
    print("Author     :", book["author"])
    print("Available  :", book["available"])
    print("Borrowed   :", book["borrowed"])
