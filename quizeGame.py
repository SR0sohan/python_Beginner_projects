print("Welcome to my Quize game.")

playing =  input("So.... do you want to play? Type 'yes' to play, type 'no' to quite.\n")

if playing.lower() != "yes":
    quit()
print("Ok,Let's play! :)")
score = 0 
answer1 = input("what does it mean by CPU?\n")
if answer1.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer2 = input("What does it mean by GPU?\n")
if answer2.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer3 = input("What does it mean by RAM\n")
if answer3.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer4 = input("What does it mean by PSU\n")
if answer4.lower() == "power suply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " question correct!")
print("You got "+ str((score / 4) * 100)+ "% marks.")