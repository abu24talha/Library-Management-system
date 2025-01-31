booksinLibrary = ["Algorithm", "Django", "C", "Python", "C++"]

print('''\/\/\/\/\/====Welcome to Central Library====\/\/\/\/\/
  Press *1 to Display the Books
      \t*2 to Borrow a Book 
      \t*3 to Return a Book
      \t*4 to Exit the Library
''')

while(True):
    
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            print(booksinLibrary)

        elif choice == 2:
            bookName = input("Please Enter Name of the Book : ")
            if bookName in booksinLibrary:
                name = input("Enter Your Name : ")
                id = input("Enter You Admission Number : ")
                branch = input("Enter Your Branch : ")
                dateofBorrow = input("Enter Today's Date : ")
                with open("Borrow_List.txt", "a") as f:
                    f.write(f"******************************\nBook = {bookName}\nName = {name}\nAdmission No. = {id}\nBranch = {branch}\nDate of Borrow = {dateofBorrow}\n******************************\n\n")
                print(f"You have been issued book {bookName}. Kindly return it within 30 days.")
                booksinLibrary.remove(bookName)
            else:
                print(f"The book {bookName} isn't available now. Please wait until it is available.\nThank you")

        elif choice == 3:
            returnBook = input("Please Enter the Name of the Book : ")
            name = input("Enter Your Name : ")
            id = input("Enter You Admission Number : ")
            branch = input("Enter Your Branch : ")
            dateofReturn = input("Enter Today's Date : ")
            with open("Return_List.txt", "a") as f:
                    f.write(f"******************************\nBook = {returnBook}\nName = {name}\nAdmission No. = {id}\nBranch = {branch}\nDate of Return = {dateofReturn}\n******************************\n\n")
            print("Thanks for providing this Book to Central Library.\nHope you enjoyed it!")
            booksinLibrary.append(returnBook)

        elif choice == 4:
            print("Thanks for chosing Central Library!")
            exit()

        else:
            print("Invalid Input")
