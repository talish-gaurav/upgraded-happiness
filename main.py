import random

while True:
  comp_cho = random.choice(["Rock","Scissor","Paper"])
  user_cho = input("Enter your choice - Rock, Paper, Scissors")
  
  if comp_cho == user_cho:
    print("A tie")
  elif comp_cho == "Rock":
    if user_cho == "Scissor":
      print("You lose")
    else:
      print("You won") 
  elif comp_cho == "Paper":
    if user_cho == "Scissor":
      print("You won")
    else:
      print("You lose")     
  elif comp_cho == "Scissor":
    if user_cho == "Rock":
      print("You win")
    else:
      print("You lose") 
  play_again = input("Play again? Y for yes and N for no")
  if play_again != "Y":
    break
  
