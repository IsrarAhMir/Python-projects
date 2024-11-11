print("welcome to my game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! lets play then")

score = 0

answer = input("What is the capital of France?")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Paris.")
    
answer = input("Who wrote the play 'Romeo and Juliet'? ")
if answer.lower() == "william shakespeare":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is William Shakespeare.")

answer = input("What is the largest planet in our solar system? ")
if answer.lower() == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Jupiter.")

answer = input("What is the chemical symbol for water? ")
if answer.upper() == "H2O":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is H2O.")

answer = input("Which year did the Titanic sink? ")
if answer == "1912":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 1912.")

answer = input("What is the hardest natural substance on Earth? ")
if answer.lower() == "diamond":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Diamond.")

answer = input("How many continents are there in the world? ")
if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 7.")


print("you got  " + str(score) + "  questions correct")
print("you got  " + str((score/7)*100) + "%. ")


