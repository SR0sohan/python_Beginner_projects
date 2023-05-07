name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")
answer = input(
    "You are ona dirt road it has come to an end you can go left or right.").lower()

if answer == "left":
    answer == input(
        "You have come to a river, you can walk around it or you can swim accross(swim/walk)").lower()
    if answer == "swim":
        print("OOPS!...You were swiming but an crocodile ate you.You loose the geme")
    elif answer == "walk":
        print("Nice........!You gave been walking for 200 miles and died out of hunger and thirst. You loose")
    else:
        print("Not a valid option, you loose.")
elif answer == "right":
    answer == input(
        "You came to a bridge, it looks broken.Do you wanr to cross it or head back where you came from?(cross/back)").lower()
    if answer == "back":
        print("Ok..!Go back to home cowred.")
    elif answer == "cross":
        answer = input(
            "You crossed the bridge and meet a strenger.Do you wan to talk to him?(yes/no)").lower()
        if answer == "yes":
            print("That man gave you some gold,congrats! You won the game.")
        elif answer == "no":
            print("You ignored the man, and he got offened and killed you")
        else:
            print("Not a valid option, you loose.")
    else:
        print("Not a valid option, you loose.")
else:
    print("Not a valid option, you loose.")

print(f"Thank you for playing{name}")
