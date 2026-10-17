def tip(bill_amount, tip_percentage=2):
    amount = bill_amount * (tip_percentage / 100)
    print("The tip amount is:" ,amount)

bill_amount = int(input("Enter the bill amount: "))
tip_percentage = int(input("Enter the tip percentage: "))
tip(bill_amount, tip_percentage)