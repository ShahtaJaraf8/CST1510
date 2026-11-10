bill = float(input("What was the total bill? $"))

people = int(input("How many people are splitting the bill?\n"))

tip = int(input("What tip percentage would you like to give? 10, 12, or 15?\n"))

total_tip = bill * (tip / 100)
total_bill = bill + total_tip
bill_per_person = total_bill / people

final_amount = f"{bill_per_person:.2f}"

print(f"Each person should pay: ${final_amount}")