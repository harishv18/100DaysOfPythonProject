import random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
UserInput = int(input())
options = ['Rock','Paper','Scissors']
ComputerChose = random.randint(0,2)
print(f"ComputerChose is: {ComputerChose}")
if(UserInput == ComputerChose):
  print(f"Draw! because you and computer chose {options[UserInput]}")
else:
  user_chose = options[UserInput]
  comp_chose = options[ComputerChose]
  if(user_chose == "Rock"):
    if(comp_chose == "Paper"):
      print("Computer Win")
    else:
      print("You Win")
  if(user_chose == "Paper"):
    if(comp_chose == "Scissors"):
      print("Computer Win")
    else:
      print("You Win")
  if(user_chose == "Scissors"):
    if(comp_chose == "Rock"):
      print("Computer Win")
    else:
      print("You Win")

