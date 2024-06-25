#Figure out how much each person should pay

print("Welcome to the Tip Calculator")
Bill = float(input("What is the total bill?\n"))
Tip = float(input("What percentage tip would you like to give\n"))
People = float(input("How many people to split the bill?\n"))

Split = (Bill + (Bill * (Tip / 100)))/People

print(f"Each person should pay: {round(Split,2)}")

