# Dictionary for storing login credentials. Here, only one username-password pair is provided.
login_credentials = {
    "harish": "1234"
}

# Dictionary to store student records where each student's ID is the key and their details are stored as a dictionary.
students = {}

# Function to handle user login
def login():
    # Prompt the user to enter username and password
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    # Check if the entered username exists in the login_credentials and if the password matches
    if username in login_credentials and login_credentials[username] == password:
        print("Login Successfully!\n")
        return True  # Login successful
    else:
        print("Login Failed! Please enter a valid username and password.\n")
        return False  # Login failed

# Function to add a new student to the student record
def add_students():
    # Prompt the user to enter a unique student ID
    stud_id = input("Enter the Student ID: ")
    # Check if the student ID already exists in the students dictionary
    if stud_id in students:
        print("A student with this ID already exists!\n")
    else:
        # Collect additional student details
        name = input("Enter the name of the student: ")
        location = input("Enter the location of the student: ")
        grade = input("Enter the grade of the student: ")
        ph_number = input("Enter the parent's phone number: ")
        
        # Add the student information to the students dictionary with stud_id as the key
        students[stud_id] = {
            "Name": name,
            "Location": location,
            "Grade": grade,
            "Ph_Number": ph_number
        }
        print("Student added successfully!\n")

# Function to display all students and their details
def view_students():
    # Check if there are any students in the dictionary
    if students:
        print("\nList of students:")
        # Loop through each student record
        for stud_id, details in students.items():
            print(f"ID: {stud_id}, Name: {details['Name']}, Location: {details['Location']}, "
                  f"Grade: {details['Grade']}, Ph_Number: {details['Ph_Number']}")
    else:
        print("No students found!\n")

# Function to update an existing student's details
def update_students():
    # Prompt the user to enter the student ID they want to update
    stud_id = input("Enter the book: ID to update: ")
    # Check if the student ID exists in the students dictionary
    if stud_id in students:
        print(f"Current details: {students[stud_id]}")
        
        # Collect new information. Leave blank to keep the current information
        name = input("Enter new name of student (leave blank to keep current): ")
        location = input("Enter new location of student (leave blank to keep current): ")
        grade = input("Enter new grade of student (leave blank to keep current): ")
        ph_number = input("Enter new parent's phone number (leave blank to keep current): ")

        # Update only fields that were entered
        if name:
            students[stud_id]["Name"] = name
        if location:
            students[stud_id]["Location"] = location
        if grade:
            students[stud_id]["Grade"] = grade
        if ph_number:
            students[stud_id]["Ph_Number"] = ph_number

        print("Student details updated successfully!\n")
    else:
        print("Student not found!\n")

# Function to delete a student record
def delete_students():
    # Prompt the user to enter the student ID they want to delete
    stud_id = input("Enter the Student ID to delete: ")
    # Check if the student ID exists in the students dictionary
    if stud_id in students:
        del students[stud_id]  # Delete the student record
        print("Student deleted successfully!\n")
    else:
        print("Student not found!\n")

# Function to display all students in a particular grade
def display_students():
    # Prompt the user to enter the grade to filter by
    grade = input("Enter the grade to display: ")
    # Loop through the students and print those in the specified grade
    for details in students.values():
        if details['Grade'] == grade:
            print(f"{details['Name']}")

# Function to count the number of students in a specific grade
def count_students():
    # Prompt the user to enter the grade to count
    grade_count = input("Enter the grade to count: ")
    count = 0  # Initialize count variable
    # Loop through the students and count those in the specified grade
    for details in students.values():
        if details['Grade'] == grade_count:
            print(f"{details['Name']}")
            count += 1
    print("Student Count:", count)

# Function to search for a student by their ID
def search_students():
    # Prompt the user to enter the student ID to search for
    stud_id = input("Enter the Student ID: ")
    
    # Check if the student ID exists in the students dictionary
    if stud_id in students:
        print("Student is present.")
    else:
        print("Student is not present.")

# Main program that displays the menu and allows the user to interact with the system
if login():  # Check if login is successful
    while True:
        # Display the menu options
        print("\nStudent Record Management System")
        print("1. Add Students")
        print("2. View Students")
        print("3. Update Students")
        print("4. Delete Students")
        print("5. Display Students by Grade")
        print("6. Count Students by Grade")
        print("7. Search Students by ID")
        print("8. Exit")

        # Prompt the user to choose an option
        choice = input("Enter your choice: ")
        
        # Execute the appropriate function based on the user's choice
        if choice == "1":
            add_students()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_students()
        elif choice == "4":
            delete_students()
        elif choice == "5":
            display_students()
        elif choice == "6":
            count_students()
        elif choice == "7":
            search_students()
        elif choice == "8":
            print("Exiting the system.")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice! Please try again.")
