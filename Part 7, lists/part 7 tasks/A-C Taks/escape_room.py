inventory =[]
print("You are in a room. There is a table and a locked door.")
choice = input("What do you do? (table/door): ")
if choice == "table":
    print("You look under the table and find a KEY!")
    print("You add it to your inventory.")
    inventory.append("KEY")
    print("inventory :", inventory)
    print("you escaped")
elif choice == "door":
    print("The door is locked")


