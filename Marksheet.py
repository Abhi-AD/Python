# Function to take user input for subject marks
student_range = int(input("Enter a save data number: "))

for i in range(student_range):
    name = input("Enter a student name: ")
    print("Slow the student name:   ")
    def get_subject_marks():
        subject_marks = []
        num_subjects = int(input("Enter the number of subjects: "))
        
        for i in range(num_subjects):
            subject_name = input(f"Enter Subject {i+1} name: ")
            marks = int(input(f"Enter marks for {subject_name}: "))
            subject_marks.append((subject_name, marks))
        
        return subject_marks

    # Get user input for subject marks
    subject_marks = get_subject_marks()

    print("\nOriginal list of tuples:")
    print(subject_marks)

    subject_marks.sort(key=lambda x: x[1])

    print("\nSorting the List of Tuples based on marks:")
    print(subject_marks)
