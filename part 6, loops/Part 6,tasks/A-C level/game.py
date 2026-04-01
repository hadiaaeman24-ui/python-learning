playing = True
while playing:
    print(" You are in a dark room. There is a door and a window.")
    print(" What do you do?")
    print("1. Open the door  so write 1")
    print("2. Look out the window so write 2 ")
    choice = int(input("What is your choice? "))
    if choice == 1:
        print("You open the door. A friendly cat greets you! You win!")
    elif choice == 2:
        print("You saw a ghost and you are injured.")
    again = input("('Play again? (yes/no): ')")
    if again == "yes":
        playing = True
    elif again == "no":
        playing = False
        break

