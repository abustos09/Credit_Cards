"""
Not in use when import

outstanding_balance = float(raw_input("What is your outstanding balance? "))
annual_interest_rate = float(raw_input("What is your annual interest rate? "))
"""
monthly_lower_bound = outstanding_balance / 12.0 # 12 is set because we are looking to pay this off in a year
monthly_upper_bound = (outstanding_balance * (1 + (annual_interest_rate / 12.0)) ** 12.0) / 12.0 # (Balance * (1 + (Annual interest rate / 12.0)) ** 12.0) / 12.0 
print "lower" + str(monthly_lower_bound)
print "higher" + str(monthly_upper_bound)

epsilon = .1

def paying_debt_year(outstanding_balance, monthly_lower_bound, monthly_upper_bound):
    previous_balance = outstanding_balance
    monthly_interest_rate = annual_interest_rate / 12.0
    month = 0
    
    # minimum_monthly_payment
    minimum_monthly_payment = (monthly_upper_bound + monthly_lower_bound) / 2.0

    while previous_balance > epsilon:
        month += 1
        updated_balance_each_month = previous_balance * (1 + monthly_interest_rate) - minimum_monthly_payment
        previous_balance = updated_balance_each_month
        if month >= 12:
            break        

    if abs(previous_balance) > epsilon:
        if previous_balance > 0:
            monthly_lower_bound = minimum_monthly_payment
            paying_debt_year(outstanding_balance, monthly_lower_bound, monthly_upper_bound)
        elif previous_balance < 0:
            monthly_upper_bound = minimum_monthly_payment
            paying_debt_year(outstanding_balance, monthly_lower_bound, monthly_upper_bound)          
    else:
        if previous_balance > 0:
            monthly_lower_bound = minimum_monthly_payment
            paying_debt_year(outstanding_balance, monthly_lower_bound, monthly_upper_bound)
        else:
            print "********** RESULTS **********"
            print "Monthly payment to pay off debt in 1 year: " + str(minimum_monthly_payment)
            print "Number of months needed: " + str(month)
            print "Balance: " + str(updated_balance_each_month)


paying_debt_year(outstanding_balance, monthly_lower_bound, monthly_upper_bound)



