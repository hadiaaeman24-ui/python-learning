Player ={
    "name" : "leo",
    "Level": 1,
    "Health" : 50
}
file = open("Player.txt" , "w")
file.write(Player["name"] + "\n")
file.write(str(Player["Level"])+ "\n")
file.write(str(Player["Health"]) + "\n")
print("Saving...")
file.close()

print("Loading...")
file = open("Player.txt", "r")

name = file.readline().strip()   
level = file.readline().strip()  
health = file.readline().strip() 

file.close()

print("Name:", name)      
print("Level:", level)    
print("Health:", health)
