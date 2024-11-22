"""Tip Calculator"""

print("Welcome to The Tip Calculator!\n")

bill = float(input("What was the total bill of the restaurant?\nRs. "))
tip = int(input("How much tip (in percentage) would you like to give?\n"))

total_bill = bill * ((tip / 100) + 1)
split = int(input("How many people to split the bill?\n"))

each_pay = round(total_bill / split, 2)

print(f"Each person should pay: Rs. {each_pay}")
