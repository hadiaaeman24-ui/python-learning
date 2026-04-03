import random
def dice_roller(promt, min , max):
    while True:
        try:
            number = int(input(promt))
            if min <= number <= max:
                return number
            else: 
                print("Enter a number between 1 to 5 ")
        except: 
            print(" Enter a valid number  ")

num = dice_roller("Enter a number...", 1 , 5 )
print("rolling dice....")
dice_results = []
for i in range(num):
    roll = random.randint(1, 6)
    dice_results.append(roll)
    print(f"Dice {i + 1}: {roll}")



