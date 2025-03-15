# Initialize text file containing quiz questions and answers

score = 0
quiz_file = open("the_quiz.txt", "r") # Make this code access the text file
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

quiz_file.close()