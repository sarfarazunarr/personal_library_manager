from utils import addBook, exit, removeBook, searchBook, showBooks, statistics

print("Welcome to Your Own Library!")



def menu():
    while True:
        try:
            print(
                '''
            1. Add a book  
            2. Remove a book  
            3. Search for a book  
            4. Display all books  
            5. Display statistics  
            6. Exit   
            ''')
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a numeric value")
            continue
        if choice == 1:
            addBook()
            break
        elif choice == 2:
            removeBook()
            break
        elif choice == 3:
            searchBook()
            break
        elif choice == 4:
            showBooks()
            break
        elif choice == 5:
            statistics()
            break
        elif choice == 6:
            exit()
            break
        else:
            print("Invalid Choice")
        
menu()
