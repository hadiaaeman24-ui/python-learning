Password = input("What is password?")
correctpassword = "python123"
if Password == correctpassword:
    print("Access granted")
else:
    print("Wrong Password")

Temp = float(input("What is temperature?"))
if Temp >= 30:
    print("It's very hot! Drink water.")
elif Temp == 20:
   print("Nice weather! Go outside. ") 
elif Temp == 10:
   print("A bit cold. Wear a jacket.")
elif Temp <= 10 :
   print("Very cold! Wear a warm coat.")
else:
   print(" I don't have advise")


Secret = 7 
guess = int(input("Guess the number?"))
if guess >= 8 :
   print("This number is high")
elif guess <= 6 :
   print("This number is too low")
elif guess == 7 :
   print("It's correct")

