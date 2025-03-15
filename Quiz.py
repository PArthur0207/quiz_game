# Initialize text file containing quiz questions and answers
# Make this code access the text file
quiz_file = open("the_quiz.txt", "r")
lines = quiz_file.read().splitlines()

for i in range(0, len(lines), 8):
    print(lines[i])
    print(lines[i + 1])
    print(lines[i + 2])
    print(lines[i + 3])
    print(lines[i + 4])

    answer = input("Answer here: ").strip().upper()
    correct = lines[i + 6].strip()
    print(correct)
    if answer == correct:
        print("Correct!")
    else:
        print("Wrong!")
# Multiple choice picking from a-d
# Make code shorter
# Tracks the test scores
# Show text scores

quiz_file.close()