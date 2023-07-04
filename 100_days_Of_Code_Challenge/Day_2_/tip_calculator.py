'''
calculation:
===========

What was the Total bill ? $  ==> 200
How much tip would you like to give ? 10, 12, or 15?  ===> 12% tip
How many people to split the bill? ==> 3

Each person should pay ==> (200.00/3*1.12) =74.66
'''

print("Welcome to the Tip Calculator !")

bill = float(input("What was the Total bill ? $"))

tip = int(input("How much tip would you like to give ? 10, 12, or 15?"))

people = int(input("How many people to split the bill? "))

tip_as_percent = tip/100
total_tip_amount=bill*tip_as_percent
total_bill=bill+total_tip_amount
amount_to_pay = total_tip_amount/people

print("Each erson should pay $ {:.2f}".format(amount_to_pay))

