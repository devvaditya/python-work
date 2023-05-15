#Tip Calculator
print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill?\n$"))
bill_percent = int(input("What percentage of tip would you like to give?10, 12 or 15?\n"))
people = int(input("How amny people to slit the bill?\n"))
individual_bill = round((bill + bill * (bill_percent / 100)) / people , 2)
print(f"Each person should pay:\n${individual_bill} ")