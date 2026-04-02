kitchen = {
    "Description" : "In the kitchen you can see a table and stove",
    "items":["apple", "glass"]
}
garden = {
    "Description" : "In the garden there are many flowers",
    "items":["rose","sunflowers"]
}
def room(Look):
    choice = input("What you want to look (description/Items): ")
    if choice == "description":
        print(Look["Description"])
    elif choice == "Items":
        print(Look["items"])
    choice2 = input("What you want to look now (description/Items):")
    if choice2 == "description":
        print(Look["Description"])
    elif choice2 == "Items":
        print(Look["items"])
    else:()

    
print("You are in the kitchen") 
room(kitchen)
choose = input("You want to look in garden: (yes/no): ")
if choose == "yes":
    room(garden)
else:()

