import random

# Define the questions and answers
questions = {
    "What is the output of the following code?\nprint(3 + 2 * 2)": "7",
    "Which keyword is used to define a function in Python?": "def",
    "What is the result of the expression 2 ** 3?": "8",
    "What is the output of the following code?\nprint('Hello' + 'World')": "HelloWorld",
    "What is the file extension for Python files?": ".py",
    "What is the output of the following code?\nprint(len('Python'))": "6",
    "What is the result of the expression 10 / 3?": "3.3333333333333335",
    "Which data type is used to represent a sequence of characters in Python?": "string",
    "What is the output of the following code?\nprint(10 == 10.0)": "True",
    "What is the result of the expression 7 // 2?": "3",
    "What is the output of the following code?\nprint(type(10))": "<class 'int'>",
    "What is the result of the expression 'Hello' * 3?": "HelloHelloHello",
    "What is the output of the following code?\nprint('Python'[2:])": "thon",
    "What is the result of the expression 4 % 2?": "0",
    "Which operator is used for exponentiation in Python?": "**",
    "What is the output of the following code?\nprint(10 != 5)": "True",
    "What is the result of the expression 3 + 2 * 4?": "11",
    "What is the output of the following code?\nprint('Python'.lower())": "python",
    "What is the result of the expression 2 + 3 * 4 / 2?": "8.0",
    "Which data type is used to represent a non-integer number in Python?": "float",
    "What is the output of the following code?\nprint(2 > 5)": "False",
    "What is the result of the expression 5 > 3 and 2 < 4?": "True",
    "What is the output of the following code?\nprint('Python'[1:4])": "yth",
    "What is the result of the expression 3 == 5 or 2 > 1?": "True",
    "What is the output of the following code?\nprint('Python'.upper())": "PYTHON",
    "What is the result of the expression 4 + 5 ** 2?": "29",
    "Which operator is used for floor division in Python?": "//",
    "What is the output of the following code?\nprint(len('Python Programming'))": "18",
    "What is the result of the expression 5 != 5?": "False",
    "What is the output of the following code?\nprint(10 // 3)": "3",
    "What is the result of the expression 2 > 1 and 3 < 4?": "True",
    "What is the output of the following code?\nprint('Python'[::2])": "Pto",
    "What is the result of the expression 2 + 2 * 3 - 1?": "7",
    "What is the output of the following code?\nprint('Python'.find('y'))": "1",
    "What is the result of the expression 7 % 2?": "1",
    "Which operator is used for string concatenation in Python?": "+",
    "What is the output of the following code?\nprint(10 < 5)": "False",
    "What is the result of the expression 3 < 2 or 2 > 1?": "True",
    "What is the output of the following code?\nprint('Python'[::-1])": "nohtyP",
    "What is the result of the expression (4 + 5) * 2?": "18",
    "What is the output of the following code?\nprint('Python'.replace('P', 'J'))": "Jython",
    "What is the result of the expression 2 ** 0?": "1",
    "What is the output of the following code?\nprint(10 >= 10)": "True",
    "What is the result of the expression 3 < 4 and 2 > 1?": "True",
    "What is the output of the following code?\nprint('Python'[1])": "y",
    "What is the result of the expression 5 < 3 or 2 > 4?": "False",
    "What is the output of the following code?\nprint('Python'.split('t'))": "['Py', 'hon']",
    "What is the result of the expression 4 / 2?": "2.0",
    "What is the output of the following code?\nprint(10 <= 5)": "False",
    "What is the result of the expression 2 < 3 and 4 > 1?": "True",
    "What is the output of the following code?\nprint('Python' + ' Programming')": "Python Programming",
    "What is the result of the expression 5 > 3 or 1 > 4?": "True",
    "What is the output of the following code?\nprint('Python'.split())": "['Python']",
    "What is the result of the expression 2 * 3 + 4?": "10",
    "What is the output of the following code?\nprint(10 == '10')": "False",
    "What is the result of the expression 3 <= 2 or 2 >= 1?": "True"
}

# Shuffle the questions
question_list = list(questions.items())
random.shuffle(question_list)

# Initialize the score and user_answers list
score = 0
user_answers = []

# Function to display a specific question
def display_question(index):
    question, _ = question_list[index]
    print(f"\nQ{index + 1}: {question}")
    user_answer = input("Your answer: ")
    return user_answer

# Iterate through the questions
while len(question_list) > 0:
    user_input_index = int(input(f"\nEnter the index number of the question you want to answer (1 to {len(question_list)}): "))
    user_index = user_input_index - 1

    while user_index < 0 or user_index >= len(question_list):
        print("Invalid index number. Please enter a valid index.")
        user_input_index = int(input(f"\nEnter the index number of the question you want to answer (1 to {len(question_list)}): "))
        user_index = user_input_index - 1

    user_answer = display_question(user_index)
    user_answers.append(user_answer)

    correct_answer = question_list[user_index][1]
    if user_answer.lower() == correct_answer.lower():
        score += 1

    # Remove the question from the list
    question_list.pop(user_index)

# Print all the user answers and correct answers
print("\n********************************************")
print("Your answers and correct answers:")
for i in range(len(user_answers)):
    question, answer = list(user_answers[i].keys())[0], list(user_answers[i].values())[0]
    correct_answer = questions[question]
    print(f"'User_answer': {answer} \n Q{i+1}: {question}\n A{i+1}: {correct_answer}\n")

# Print the final score
print(f"\nQuiz finished! Your score is {score}/{len(questions)}")
