import random
user_data_file="file.txt"

topics = {
    "TCS_company": [
        {"question": "TCS comes under which group?", "options": ["Tata", "Birla", "Ambani", "None"], "answer": "Tata", "type": "multiple-choice"},
        {"question": "TCS is a service based company.", "options": ["True", "False"], "answer": "True", "type": "true-false"},
        {"question": "One of the office of TCS is in Gwalior", "options": ["True", "False"], "answer": "False", "type": "true-false"}
    ],
    "Data_science": [
        {"question": "Statistics is used in which of the following?", "options": ["Web dev", "data science", "Android dev", "none"], "answer": "data science", "type": "multiple-choice"},
        {"question": "Python is used in data science.", "options": ["True", "False"], "answer": "True", "type": "true-false"},
        {"question": "There is no need of learning mathematics in data science", "options": ["True", "False"], "answer": "False", "type": "true-false"}
    ],
    "Python": [
        {"question": "Which language is used in data science the most?", "options": ["C#", "Python", "Java", "C++"], "answer": "Python", "type": "multiple-choice"},
        {"question": "Python have so many libraries for better use.", "options": ["True", "False"], "answer": "True", "type": "true-false"},
        {"question": "Django is a framework of Python.", "options": ["True", "False"], "answer": "True", "type": "true-false"}
    ],
    "Personality_dev": [
        {"question": "Which of the following is the biggest factor to look into while giving an interview", "options": ["Way of communication", "Dressing sense", "Way of representation", "All of the above"], "answer": "All of the above", "type": "multiple-choice"},
        {"question": "English language plays important role in interview.", "options": ["True", "False"], "answer": "True", "type": "true-false"},
        {"question": "HR round is not that much important as technical one.", "options": ["True", "False"], "answer": "False", "type": "true-false"}
    ]
}

def register_user():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")

    if check_user_exists(username):
        print("Username already exists! Try logging in.")
        return False

    with open(USER_DATA_FILE, "a") as file:
        file.write(f"{username},{password}\n")

    print("Registration successful!")
    return True
def check_user_exists(username):
    try:
        with open(USER_DATA_FILE, "r") as file:
            for line in file:
                stored_username, _ = line.strip().split(",")
                if stored_username == username:
                    return True
    except FileNotFoundError:
        return False
    return False
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if not check_user_exists(username):
        print("Username not found! Please register.")
        return False

    with open(USER_DATA_FILE, "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if stored_username == username and stored_password == password:
                print("Login successful!")
                return True
    print("Invalid username or password!")
    return False
def ask_multiple_choice_question(topic, question_data):
    print(f"Topic: {topic}")
    print(f"Question: {question_data['question']}")
    
    for i, option in enumerate(question_data['options'], 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            answer = int(input("Choose the number corresponding to your answer: "))
            if answer < 1 or answer > len(question_data['options']):
                print(f"Invalid choice. Please enter a number between 1 and {len(question_data['options'])}.")
            else:
                break
        except ValueError:
            print("Not a valid number. Please choose a valid number from the options.")
    if question_data['options'][answer - 1] == question_data['answer']:
        print("Good job! That's the correct answer.\n")
        return True
    else:
        print(f"That's incorrect. The correct answer is: {question_data['answer']}\n")
        return False

def ask_true_false_question(topic, question_data):
    print(f"Topic: {topic}")
    print(f"Question: {question_data['question']}")
    
    for i, option in enumerate(question_data['options'], 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            answer = int(input("Enter 1 for True or 2 for False: "))
            if answer not in [1, 2]:
                print("Please enter 1 for True or 2 for False.")
            else:
                break
        except ValueError:
            print("Please enter a valid choice. Enter 1 for True or 2 for False.")
    if question_data['options'][answer - 1] == question_data['answer']:
        print("Nice work! That's correct.\n")
        return True
    else:
        print(f"That's incorrect. The correct answer is: {question_data['answer']}\n")
        return False

def run_quiz():
    user = login()

    print("\nWhat kind of questions would you like to attempt today?")
    print("1. Multiple Choice Questions")
    print("2. True/False Questions")
    
    while True:
        question_type_choice = input("Enter 1 for Multiple Choice or 2 for True/False: ")
        if question_type_choice in ["1", "2"]:
            break
        else:
            print("Please choose a valid option. Enter 1 for Multiple Choice or 2 for True/False.")

    print("\nWhich topic would you like to explore?")
    print("1. TCS_company")
    print("2. Data_science")
    print("3. Python")
    print("4. Personality_dev")
    
    while True:
        topic_choice = input("Enter the number corresponding to your chosen topic: ")
        if topic_choice in ["1", "2", "3", "4"]:
            break
        else:
            print("Please choose a valid topic. Enter a number from 1 to 4.")

    topic_mapping = {
        "1": "TCS_company",
        "2": "Data_science",
        "3": "Python",
        "4": "Personality_dev"
    }
    
    selected_topic = topic_mapping[topic_choice]
    score = 0
    total_questions = 0
    selected_questions = [q for q in topics[selected_topic] if q['type'] == ('multiple-choice' if question_type_choice == "1" else 'true-false')]
    

    random.shuffle(selected_questions)
    for question_data in selected_questions[:3]:
        if question_type_choice == "1":
            if ask_multiple_choice_question(selected_topic, question_data):
                score += 1
        elif question_type_choice == "2":
            if ask_true_false_question(selected_topic, question_data):
                score += 1
        total_questions += 1

    print(f"\nGreat job, {user}! You've completed the quiz.")
    print(f"Your final score is {score}/{total_questions}.")
    percentage = (score / total_questions) * 100 if total_questions > 0 else 0
    print(f"That's {percentage:.2f}% correct. Well done!")

run_quiz()