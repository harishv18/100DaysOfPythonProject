print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? $"))
percentage_tip = total_bill * (percentage_tip/100)
total_people = int(input("How many people to split the bill?"))
money = (total_bill + percentage_tip) / 7
print(f"Each person sould pay: ${round(money,2)}")