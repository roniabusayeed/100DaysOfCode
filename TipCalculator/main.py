print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("How much tip would you likfe to give? 10, 12, or 15? ")) / 100
total_people = int(input("How many people to split the bill? "))

# Calculate payment for each person
payment_each = total_bill * (1 + tip_percentage) / total_people
final_amount = "{:.2f}".format(round(payment_each, 2))
print(f"Each person should pay: ${final_amount}")
