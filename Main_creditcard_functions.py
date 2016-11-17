
def paying_debt_x_month(outstanding_balance, annual_interest_rate, month,
    monthly_lower_bound, monthly_upper_bound):
    global minimum_monthly_payment2, month2, updated_balance_each_month2

    epsilon = .1
    previous_balance = outstanding_balance
    monthly_interest_rate = annual_interest_rate / 12.0
    month_counter = 0

    
    # minimum_monthly_payment
    minimum_monthly_payment = (monthly_upper_bound + monthly_lower_bound) / 2.0

    while previous_balance > epsilon:
        month_counter += 1
        updated_balance_each_month = previous_balance * (1 + monthly_interest_rate) - minimum_monthly_payment
        previous_balance = updated_balance_each_month
        if month_counter >= month:
            break        

    if abs(previous_balance) > epsilon:
        if previous_balance > 0:
            monthly_lower_bound = minimum_monthly_payment
            paying_debt_x_month(outstanding_balance, annual_interest_rate, month, 
                monthly_lower_bound, monthly_upper_bound)
        elif previous_balance < 0:
            monthly_upper_bound = minimum_monthly_payment
            paying_debt_x_month(outstanding_balance, annual_interest_rate, month,
                monthly_lower_bound, monthly_upper_bound)          
    else:
        if previous_balance > 0:
            monthly_lower_bound = minimum_monthly_payment
            paying_debt_x_month(outstanding_balance, annual_interest_rate, month,
                monthly_lower_bound, monthly_upper_bound)
        else:
            minimum_monthly_payment2 = minimum_monthly_payment
            month2 = month_counter
            updated_balance_each_month2 = updated_balance_each_month
    return minimum_monthly_payment2, month2, updated_balance_each_month2

def paying_debt_year(monthly_lower_bound, monthly_upper_bound, 
    outstanding_balance, annual_interest_rate):
    global minimum_monthly_payment2, month2, updated_balance_each_month2

    epsilon = .1
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
            paying_debt_year(monthly_lower_bound, monthly_upper_bound, outstanding_balance, annual_interest_rate)
        elif previous_balance < 0:
            monthly_upper_bound = minimum_monthly_payment
            paying_debt_year(monthly_lower_bound, monthly_upper_bound, outstanding_balance, annual_interest_rate)          
    else:
        if previous_balance > 0:
            monthly_lower_bound = minimum_monthly_payment
            paying_debt_year(monthly_lower_bound, monthly_upper_bound, outstanding_balance, annual_interest_rate)
        else:
            print "********** RESULTS **********"
            print "Monthly payment to pay off debt in 1 year: " + str(minimum_monthly_payment)
            print "Number of months needed: " + str(month)
            print "Balance: " + str(updated_balance_each_month)
            minimum_monthly_payment2 = minimum_monthly_payment
            month2 = month
            updated_balance_each_month2 = updated_balance_each_month
    return minimum_monthly_payment2, month2, updated_balance_each_month2











