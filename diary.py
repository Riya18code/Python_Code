
class PersonalDiary:     #created a class called personal diary

    def write_entry(self): #defined a method called write_entry
        date = input("Enter date (DD-MM-YYYY): ") # taking user input for date,title and content.
        title = input("Enter diary title: ")
        content = input("Write your diary entry: ")
#using file handliing to save the diary entry to a text file.
        file = open("diary.txt", "a")
        file.write("Date: " + date + "\n")
        file.write("Title: " + title + "\n")
        file.write("Entry: " + content + "\n")
        file.write("-------------------------\n")
        file.close()

        print("Diary entry saved successfully!")
#defined a method called view_entries to read and display the diary enteries from the text file.
    def view_entries(self):
        file = open("diary.txt", "r")  # open the diary in read mode to read the content
        content = file.read()            # read the content of the diary
        file.close()

        print("\nYour Diary Entries:")
        print(content)
    
    #defined a method called run to provide a menu_driven interface for the user to write and view diary entries.
    def run(self):
        while True:
            print("\n===== PERSONAL DIARY =====")
            print("1. Write a new entry")
            print("2. View diary entries")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.write_entry()

            elif choice == "2":
                self.view_entries()

            elif choice == "3":
                print("Thank you for using Personal Diary!")
                break

            else:
                print("Invalid choice. Please try again.")


diary = PersonalDiary()
diary.run()
