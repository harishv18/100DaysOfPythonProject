print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go? Type 'left' of 'right'")
leftOrRight = input()
if(leftOrRight=="left"):
  print("You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
  swimOrWait = input()
  if(swimOrWait=="wait"):
    print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?")
    color = input()
    if(color=="yellow"):
      print("You Win!")
    elif(color=="blue"):
      print("Eaten by beasts.\nGame Over.")
    elif(color=="red"):
      print("Burned by the fire.\nGame Over.")
    else:
      print("Game Over.")
  else:
    print("Attacked by trout.\nGame Over.")
else:
  print("Fall into a hole.\nGame Over.")