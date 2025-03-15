# Initialize text file containing quiz questions and answers

def random_quiz():
    score = 0
    quiz_file = open("random_quiz.txt", "r") # Make this code access the text file
    lines = quiz_file.read().splitlines()

    for i in range(0, len(lines), 8):
        print(lines[i])
        print(lines[i + 1])
        print(lines[i + 2])
        print(lines[i + 3])
        print(lines[i + 4])

        answer = input("Answer here: ").strip().upper()
        correct = lines[i + 6].strip() # Multiple choice picking from a-d
        if answer == correct:
            print("Correct!")
            score += 1 # Tracks the test scores
        else:
            print("Wrong!")
            print(f"The correct answer is {correct}")

    print(f"You got {score} correct answers!") # Show text scores
    input()

    quiz_file.close()

def math_quiz():
    score = 0
    quiz_file = open("math_quiz.txt", "r") # Make this code access the text file
    lines = quiz_file.read().splitlines()

    for i in range(0, len(lines), 8):
        print(lines[i])
        print(lines[i + 1])
        print(lines[i + 2])
        print(lines[i + 3])
        print(lines[i + 4])

        answer = input("Answer here: ").strip().upper()
        correct = lines[i + 6].strip() # Multiple choice picking from a-d
        if answer == correct:
            print("Correct!")
            score += 1 # Tracks the test scores
        else:
            print("Wrong!")
            print(f"The correct answer is {correct}")

    print(f"You got {score} correct answers!") # Show text scores
    input()

    quiz_file.close()

def world_affairs_quiz():
    score = 0
    quiz_file = open("world_affairs_quiz.txt", "r") # Make this code access the text file
    lines = quiz_file.read().splitlines()

    for i in range(0, len(lines), 8):
        print(lines[i])
        print(lines[i + 1])
        print(lines[i + 2])
        print(lines[i + 3])
        print(lines[i + 4])

        answer = input("Answer here: ").strip().upper()
        correct = lines[i + 6].strip() # Multiple choice picking from a-d
        if answer == correct:
            print("Correct!")
            score += 1 # Tracks the test scores
        else:
            print("Wrong!")
            print(f"The correct answer is {correct}")

    print(f"You got {score} correct answers!") # Show text scores
    input()

    quiz_file.close()

def world_history_quiz():
    score = 0
    quiz_file = open("world_history_quiz.txt", "r") # Make this code access the text file
    lines = quiz_file.read().splitlines()

    for i in range(0, len(lines), 8):
        print(lines[i])
        print(lines[i + 1])
        print(lines[i + 2])
        print(lines[i + 3])
        print(lines[i + 4])

        answer = input("Answer here: ").strip().upper()
        correct = lines[i + 6].strip() # Multiple choice picking from a-d
        if answer == correct:
            print("Correct!")
            score += 1 # Tracks the test scores
        else:
            print("Wrong!")
            print(f"The correct answer is {correct}")

    print(f"You got {score} correct answers!") # Show text scores
    input()

    quiz_file.close()

def science_quiz():
    score = 0
    quiz_file = open("science_quiz.txt", "r") # Make this code access the text file
    lines = quiz_file.read().splitlines()

    for i in range(0, len(lines), 8):
        print(lines[i])
        print(lines[i + 1])
        print(lines[i + 2])
        print(lines[i + 3])
        print(lines[i + 4])

        answer = input("Answer here: ").strip().upper()
        correct = lines[i + 6].strip() # Multiple choice picking from a-d
        if answer == correct:
            print("Correct!")
            score += 1 # Tracks the test scores
        else:
            print("Wrong!")
            print(f"The correct answer is {correct}")

    print(f"You got {score} correct answers!") # Show text scores
    input()

    quiz_file.close()

def quiz_start():
    while True:
        choice = input("What topic would you like to quiz? \n Pick (Science, Math, World Affairs, World History, or Random): ").strip().lower()

        if choice == "science":
            science_quiz()
        elif choice == "math":
            math_quiz()
        elif choice == "world affairs":
            world_affairs_quiz()
        elif choice == "world history":
            world_history_quiz()
        elif choice == "random":
            random_quiz()
        else:
            print("Please only pick from the choices. \n")

quiz_start()

while True:

    again = input("Would you like to try again? \n (Y or N): ").strip().upper()

    if again == "Y":
        print("Goodluck!")
        quiz_start()
    elif again == "N":
        print("Thank you for participating!")
        break
    else:
        print("Please pick either y or n")