print ("Welcome to the tip Calculator.")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("how many people to split the bill?"))
bill_with_tip = percentage /100 * total_bill + total_bill
bill_per_one_peron= bill_with_tip/people
finala_ampount=round(bill_per_one_peron,2)
last_amount= f"Each person should pay: ${finala_ampount}"
last_amount= "{:.2f}".format(bill_per_one_peron)
#google = f"{Greeting}\n  {total_bill}\n {percentage} "
print(last_amount)