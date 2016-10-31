outstanding_balance = float(raw_input("What is your outstanding balance? "))
annual_interest_rate = float(raw_input("What is your annual interest rate? "))

minimum_monthly_payment = 10

def paying_debt_year(monthly_payment, outstanding_balance):
	global minimum_monthly_payment
	previous_balance = outstanding_balance
	monthly_interest_rate = annual_interest_rate / 12.0
	month = 0
	# every new call to paying_debt_year, previous balance must restart

	while previous_balance > 0:
		month += 1
		updated_balance_each_month = previous_balance * (1 + monthly_interest_rate) - minimum_monthly_payment
		previous_balance = updated_balance_each_month
		if month >= 12:
			break

	if previous_balance > 0:
		minimum_monthly_payment += 10
		paying_debt_year(minimum_monthly_payment, outstanding_balance)
	else:
		print "********** RESULTS **********"
		print "Monthly payment to pay off debt in 1 year: " + str(minimum_monthly_payment)
		print "Number of months needed: " + str(month)
		print "Balance: " + str(updated_balance_each_month)

paying_debt_year(minimum_monthly_payment, outstanding_balance)



