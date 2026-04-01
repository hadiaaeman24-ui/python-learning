print("You are in a forest. You see a path and a river.")
print("Which way you will choose (path/river)")
firstChoice =input("What is your choice ? ")
if firstChoice == "path" :
    print(" Now you have 2 more choices what you will do? Enter cave or climb tree? ")
    choice2= input("What is your choice? ")
    if choice2 == "cave":
        print ("You enter the !cave. You find a sleeping bear!")
    elif choice2 == "climb tree":
        print("You were climbing but you fell down")
elif firstChoice == "river":
    print("You saw a boat and the brigde in rive what you will choose ? ")
    secondchoice = input("What you will choose ? " )
    if secondchoice == "boat" :
        print(" you sre save now")
    elif secondchoice == "bridge" :
        print("Brigde break down and you fell in water")