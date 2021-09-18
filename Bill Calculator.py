print("Welcome to the Bill Calculator!")
bill = float(input("What is the total bill amount? \n$"))
tip = int(input("how much tip would you like to pay in percent?\n")) 
tip_in_percent = tip / 100
total_tip_amount = bill * tip_in_percent
total_bill = bill + total_tip_amount
total_persons = int(input("How many people to split the bill?\n"))
amount_per_person = total_bill / total_persons
final_amount = round(amount_per_person, 2)
print(f"The amount per person to be paid is :${final_amount}")
