init_outstanding_balance = float(raw_input("What is your total Credit Card balance: "))
annual_interest_rate = float(raw_input("What is the annual interest rate: "))
min_monthly_payment_rate = float(raw_input("What is monthly payment amount "))



def paying_the_min(init_outstanding_balance, annual_interest_rate, min_monthly_payment_rate):
	for m in range(1, 13):
		min_monthly_amount = min_monthly_payment_rate * init_outstanding_balance
		interest_paid = (annual_interest_rate / 12) * init_outstanding_balance
		principle_paid = min_monthly_amount - interest_paid
		remaining_new_balance = init_outstanding_balance - principle_paid
		init_outstanding_balance = remaining_new_balance
		print "Month: " + str(m)
		print "Minimum monthly payment: " + str(min_monthly_amount)
		print "Principle paid: " + str(principle_paid)
		print "Remaining balance: " + str(remaining_new_balance)

paying_the_min(init_outstanding_balance, annual_interest_rate, min_monthly_payment_rate)