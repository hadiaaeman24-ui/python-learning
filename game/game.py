import random

print("-"*40)
print("WELCOME TO ROCK, PAPPER, SISSOR WORLD  ")
print("-"*40)
print(" You have to play it 10 time to know if you win, loose or draw ")
print("Ready.......")

def playerchoice(choice,min ,max):
   while True:
     try:
      print("You can choose between...")
      print("1. Rock 🪨")
      print("2. Paper 📄")
      print("3. Scissors ✂️")
      choice = int(input("Choose... "))
      if min <= choice <= max : 
          if choice == 1:
           choice = "Rock"
           print("Player choice : Rock")
           return choice
          elif choice == 2:
           choice = "Papper"
           print("Player choice : Papper")
           return choice
          elif choice == 3:
           choice ="Scissors"
           print("Player choice : Scissors")
           return choice
      else :
           print("Not a valid number")
     except:
        print("Please enter a number ... ")

def computerchoice():
    score = random.randint(1, 3)
    if score == 1:
        compchoice = "Rock"
        print("Computer choice : Rock")
        return compchoice
    elif score == 2:
        compchoice = "Papper"
        print("Computer choice : Papper")
        return compchoice
    elif score == 3:
        compchoice = "Scissors"
        print("Computer choice : Scissor")
        return compchoice

def win(player,comp):
   if player == comp:
      print("draw! Computer and you make the same choice")
      return "draw"
   elif player == "Rock" and comp == "Papper":
      print("Computer win Papper kill Rock")
      return "Computer"
   elif player == "Rock" and comp == "Scissors":
      print("Player win Rock kill Scissors")
      return("Player")
   elif player == "Papper" and comp == "Rock":
      print("Player win Papper kill rock")
      return("Player")
   elif player == "Papper" and comp == "Scissors":
      print("Computer win Scissors kill Papper")
      return("Computer")
   elif player == "Scissors" and comp == "Papper":
      print("Player win Scissors kill Papper")
      return("Player")
   elif player == "Scissors" and comp == "Rock":
      print("Computer win Rock kills Siccors")
      return("Computer")


while True:  # Outer loop for playing again
    Player_score = 0  # Reset scores for new game
    Comp_score = 0
    draw_score = 0  
    count = 0  # Reset count for new game
    
    while count <= 9:
        player_choice = playerchoice("",1,3)   
        compchoice = computerchoice()
        winner = win(player_choice,compchoice)
        if winner == "Player":
            Player_score += 1
        elif winner == "Computer":
            Comp_score += 1
        elif winner == "draw":
            draw_score += 1
        print(f"Score - You: {Player_score}, Computer: {Comp_score}, Draws: {draw_score}")
        print()
        print()
        count = count + 1
   
    print("\n" + "="*40)
    print(f"FINAL - You: {Player_score}, Computer: {Comp_score}, Draws: {draw_score}")
    print("="*40)
    
 
    playagain = input("You want to play again (yes/no)? ").lower()
    if playagain != "yes":
        break 
    print("\n" * 2)  




