secret = 7
guess = ""
while guess != secret:
    guess = int(input("guess the number : "))
    if guess <= 6:
        print("The number is low")
    elif guess == 7:
        print(" its correct")
        break;
    elif guess >=8:
        print("this number is high")
