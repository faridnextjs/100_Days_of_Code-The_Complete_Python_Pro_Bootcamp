print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? $\n"))
tip = int(input("What percentage tip would you like to give? 10 12 15 \n"))
people = int(input("How many people to split the bill? \n"))

tipAsPercent = tip/100
print(f'Tip as percent: {tipAsPercent}')

totalTipAmount = bill * tipAsPercent
print(f'Total tip amount: {totalTipAmount}')

totalBill = bill + totalTipAmount
print(f'Total bill: {totalBill}')

billPerPerson = totalBill / people
print(f'Bill per person: {billPerPerson}')

finalAmount = round(billPerPerson, 2)
print(f'Final amount: {finalAmount}')

print(f'Each person should pay ${finalAmount}')