def valid_age(promt):
    while True:
        try:
            age= int(input(promt))
            return age
        except:
            print("PLEASE ENTER A VALID AGE")

age = valid_age("Enter your age.. ")
print(f"You are {age} old")
