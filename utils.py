import json 
import os

def ask():
    isContinue = input("Wants to continue?: Y/N")
    if isContinue.lower() == 'y':
        from library_manager import menu
        menu();
    else:
        exit()
    

def addBook():
        newbook = {
            "title": "", "author": "", "publication year": 0, "genre": "", "isReaded": False
        }
        print('\n'+'----'*10+'Add Book'+'----'*10+'\n')
        newbook["title"] = input("Enter the book title: ")
        newbook["author"] = input("Enter the author: ")
        newbook["publication year"] = int(input("Enter the publication year: ")) 
        newbook["genre"] = input("Enter the genre: ")
        isreaded = input("Have you read this book? (yes/no): ")
        if isreaded.lower() == 'yes':
            newbook["isReaded"] = True
        else:
            newbook["isReaded"] = False
            
        with open('library.txt', 'a') as library:
            library.write(json.dumps(newbook) + "\n")
    
        print("✅ Book Added Successfully!")
        print('\n'+'----'*20+'\n')
        ask();
        

def removeBook():
    print('\n'+'----'*10+'Remove Book'+'----'*10+'\n')
    
    book_to_remove = input("Enter book title to remove: ")
    books = []
    
    if os.path.exists('library.txt'):
        with open('library.txt', 'r') as library:
            books = [json.loads(line) for line in library if line.strip()]
    filtered_books = [book for book in books if book['title'].lower() != book_to_remove.lower()]
    
    if len(filtered_books) == len(books):
        print("❌ Book not found!")
        print('\n'+'----'*20+'\n')
        ask();
    else:
        with open('library.txt', 'w') as library:
            for book in filtered_books:
                library.write(json.dumps(book) + "\n")
        print(" ✅ Book removed successfully!")
        print('\n'+'----'*20+'\n')
        ask();


def searchBook():
    print('\n'+'----'*10+'Search Book'+'----'*10+'\n')

    searchTerm = input("Enter book title to search: ")
    books = []
    
    if os.path.exists('library.txt'):
        with open('library.txt', 'r') as library:
            books = [json.loads(line) for line in library if line.strip()]
    filtered_books = [book for book in books if book['title'].lower() == searchTerm.lower()]
    
    if len(filtered_books) == 0:
        print("❌Book not found!")
        print('\n'+'----'*20 + '\n')
        ask();
    else:
        print('\n'+'----'*10+'\n')
        book = filtered_books[0]
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Publication Year: {book['publication year']}")
        print(f"Genre: {book['genre']}")
        print(f"Read Status: {'Read' if book['isReaded'] else 'Not Read'}")
        print('\n'+'----'*10+'\n')
        ask();
        
def showBooks():
    print('\n'+'----'*10+'All Books'+'----'*10+'\n')

    books = []
    
    if os.path.exists('library.txt'):
        with open('library.txt', 'r') as library:
            books = [json.loads(line) for line in library if line.strip()]
    for book in books:
        print('\n'+'----'*10)
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Publication Year: {book['publication year']}")
        print(f"Genre: {book['genre']}")
        print('\n'+'----'*10+'\n')
    
    ask();
    
    

def statistics():
    print('\n'+'----'*10+'Statistics'+'----'*10+'\n')
    books = []
    
    if os.path.exists('library.txt'):
        with open('library.txt', 'r') as library:
            books = [json.loads(line) for line in library if line.strip()]
    print(f"Total number of books: {len(books)}")
    read_books = [book for book in books if book['isReaded']]
    print(f"Number of read books: {len(read_books)}")
    unread_books = [book for book in books if not book['isReaded']]
    print(f"Number of unread books: {len(unread_books)}")
    print(f"Percentage of read books: {len(read_books) / len(books) * 100:.2f}%")
    print('\n'+'----'*20+'\n')
    ask();
    

def exit():
    print("Goodbye!")
    exit;