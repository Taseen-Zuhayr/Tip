bill = int(input("please enter the total bill : "))
tip = int(input("please enter the tip you want to give : "))
def totalcal(bill,tip):
    total = bill + tip
    print("Please pay",total,"Taka")
totalcal(bill,tip)