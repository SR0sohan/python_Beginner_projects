import random
top_of_range = input("Please, type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 and try next time.")
        quit()
else:
    print("Please type a number and try next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Give it a try for the correct answer: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type an number and try next time.")
        continue

    if user_guess == random_number:
        print("Congratulation! You got it right.")
        break
    else:
        print("Sorry, attempt failed! Try again.")
print(f"You got it in {guesses} guesses")
