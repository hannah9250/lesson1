books = ["goosebumps", "diary of a wimpy kid", "geronimo stilton", "percy jackson", "harry potter"]
stock = [20, 15, 0, 10, 5]
late_fees = [10, 15, 5, 2, 6]

available_books = [books[i] for i in range(len(books)) if stock[i] > 0]
print("Books currently available:", available_books)

library = dict(zip(books, stock))
print("\nLibrary Inventory:")
print(library)

updated_fees = list(map(lambda x: round(x * 1.10, 2), late_fees))
print("\nUpdated Late Fees:", updated_fees)


user = input("Enter the book you want to borrow: ")

if user not in library:
    print("Book not found in the library.")
    exit()

if library[user] == 0:
    print("Sorry, this book is currently unavailable.")
    exit()

index = books.index(user)

print("BORROW DETAILS")
print("Book Name:", user)
print("Available Copies:", stock[index])
print("Late Fee after 10% increase:", updated_fees[index])