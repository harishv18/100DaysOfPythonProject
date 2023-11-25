import random
from math import ceil
print("Welcome to the PyPassword Generator")
length_of_letter = int(input("How many letters would you like in your password?\n"))
length_of_symbol = int(input("How many symbols would you like?\n"))
length_of_numbers = int(input("How many numbers would you like?\n"))

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','^','&','*','(',')','+']
numbers = ['0','1','2','3','4','5','6','7','8','9']

allCharacter = letters + symbols + numbers
password = ''
length_of_password = length_of_letter + length_of_symbol + length_of_numbers
for i in range(0,len(allCharacter)):
  random_number = ceil(random.random() * len(allCharacter)-1)
  if((length_of_password)!=len(password)):
    password += allCharacter[random_number]

print(f"Here is your password: {password}")