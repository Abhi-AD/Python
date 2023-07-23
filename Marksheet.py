import json

def get_subject_marks():
    subject_marks = []
    num_subjects = int(input("Enter the number of subjects: "))
    
    for i in range(num_subjects):
        subject_name = input(f"Enter Subject {i+1} name: ")
        marks = int(input(f"Enter marks for {subject_name}: "))
        subject_marks.append((subject_name, marks))
    
    return subject_marks

def main():
    student_range = int(input("Enter the number of students: "))
    data = []

    for i in range(student_range):
        name = input("Enter a student name: ")
        print(f"**---Enter the subject marks for student: {name}---**")
        
        # Get user input for subject marks
        subject_marks = get_subject_marks()

        data.append({"name": name, "marks": subject_marks})

    # Save the data to a JSON file
    with open("student_data.json", "w") as file:
        json.dump(data, file)

if __name__ == "__main__":
    main()
