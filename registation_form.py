import csv

def create_exam_register():
    # Get information from the user
    print("Welcome to the NEB Exam Register Form!")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    school = input("Enter your school name: ")
    subjects = input("Enter subjects you want to register for (comma-separated): ")
    
    # Store the data in a dictionary
    data = {
        "Name": name,
        "Age": age,
        "School": school,
        "Subjects": subjects
    }
    
    # Save the data to a CSV file
    with open("exam_register.csv", "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if file.tell() == 0:
            writer.writeheader()  # Write header only if the file is empty
        writer.writerow(data)
    
    print("Registration successful. Your data has been saved.")

if __name__ == "__main__":
    create_exam_register()
