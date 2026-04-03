print(" You can give commands. Take key, Use key or look what you want to do?")
inventory =[]
command = input("Enter a command?.. ")
command = command.strip()
command = command.lower()
if command == "take key":
    print("Taking key...")
    inventory.append("key")
    print("inventory")
    print("do you want to use key or look")
    command2 = input("Do you?(yes/no) ")
    command2 = command2.strip()
    command2 = command2.lower()
    if command2 == "yes":
        print("What you want to do?")
        next = input("Look or use key ")
        next = next.strip()
        next = next.lower()
        if next == "look":
            print(" You can see a table and chair.")
            print(" Do you want to use key")
            key = input("(yes/no)")
            key = key.strip()
            key = key.lower()
            if key == "yes":
                print("using key....")
            elif key == "no":
                ()
        elif next == "use key":
            print("using key...")
            print(" Do you want to look around")
            look = input("(yes/no)")
            look = look.strip()
            look = look.lower()
            if look == "yes":
                print(" You can see a table and chair.")
            elif look == "no":
                ()
    else:
        ()
elif command == "use key":
        print("dont have key..")
        print("Do you want to take key or look around..")
        command3 = input("Take key so type take key  ")
        command3 = command3.strip()
        command3 = command3.lower()
        if command3 == "take key":
            print("taking key...")
            inventory.append("key")
            print("inventory")
            print("do you want to use key or look")
            command2 = input("Do you?(yes/no) ")
            command2 = command2.strip()
            command2 = command2.lower()
            if command2 == "yes":
               print("What you want to do?")
               next = input("Look or use key ")
               next = next.strip()
               next = next.lower()
               if next == "look":
                  print(" You can see a table and chair.")
                  print(" Do you want to use key")
                  key = input("(yes/no)")
                  key = key.strip()
                  key = key.lower()
                  if key == "yes":
                    print("using key....")
                  elif key == "no":
                      ()
            elif next == "use key":
               print("using key...")
               print(" Do you want to look around")
               look = input("(yes/no)")
               look = look.strip()
               look = look.lower()
               if look == "yes":
                 print(" You can see a table and chair.")
               elif look == "no":
                  ()
            else:
              ()

elif command == "look" :
    print(" You can see a table and chair.")