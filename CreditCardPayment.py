def bisection():

    original_balance = float(raw_input("Enter your outstanding credit card balance: "))

    balance = original_balance

    print original_balance

    monthly_interest_rate = float(raw_input("Enter your annual interest rate (decimal): "))

    monthly_interest_rate /= 12.0

    print monthly_interest_rate

    low = original_balance / 12.0

    high = original_balance * ((1 + monthly_interest_rate)**12)/12.0

    minimum_payment = (high + low)/12.0

    print low

    print high

    while original_balance > 0.02 or original_balance < -0.02:

        balance = original_balance

        minimum_payment = (low + high)/2 #finding the average

        for i in range(12):

            monthlyUnpaid = balance - minimum_payment

            balance = round(monthlyUnpaid + monthly_interest_rate*monthlyUnpaid,2)

        if balance > 0: 

            low = minimum_payment

        if balance < 0:

            high = minimum_payment

        print "Minimum fixed monthly payment to pay off your credit card debt in a year is is: " + str(round(minimum_payment,2))
        original_balance = 0.01 #exits the while loop


if __name__ == '__main__':
    bisection()
