inventory = ["Key", "Map","torch"]
print("Your inventory");
for item in inventory:
    print("You have:", item)

choose = int(input("Which item do you want to use? (1-3):"))
if choose == 1 :
       print("You used the Key ")
       Item = inventory.pop(choose-1)
       for item in inventory:
            print("You have:", item) 
elif choose == 2:
        print("You used the Map ")
        Item = inventory.pop(choose-1)
        for item in inventory:
            print("You have:", item) 
elif choose == 3:
        print("You used the Torch ") 
        Item = inventory.pop(choose-1)
        for item in inventory:
            print("You have:", item) 



