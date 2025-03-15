# Initialize text file containing quiz questions and answers
# Make this code access the text file
quiz_file = open("the_quiz.txt", "r")
lines = quiz_file.read().splitlines()
print(lines[0])
print(lines[2])
print(lines[3])
print(lines[4])
print(lines[5])
print(lines[6])

answer = input("Answer here: ").strip().upper()
correct = lines[8].strip()
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