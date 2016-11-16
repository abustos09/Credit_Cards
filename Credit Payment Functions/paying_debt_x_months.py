
from Tkinter import *
"""
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
		print "Monthly payment to pay off debt in 1 year: " + str(minimum_monthly_payment)
		print "Number of months needed: " + str(month)
		print "Balance: " + str(updated_balance_each_month)

paying_debt_year(minimum_monthly_payment, outstanding_balance)
"""

fields = ("What is your outstanding balance? ", "What is your annual interest rate? ", 
	"How many months? ")

choices = (1, 10, 20)

class Credit_Debt():
	def __init__(self, master, fields):
		self.master = master
		self.topframe(fields)
		#self.middleframe()
		self.button_frame()

	def topframe(self, fields):
		self.entries = {}

		for field in fields:
			if field == "How many months? ":
				top_frame = Frame(self.master)
				label = Label(top_frame, text = field)
				self.var = StringVar(top_frame)
				self.var.set(12)
				dropdown = OptionMenu(top_frame, self.var, *choices)
				top_frame.pack(side = "top")
				label.pack(side = "left")
				dropdown.pack(side = "right")

			else:
				top_frame = Frame(self.master)
				label = Label(top_frame, text = field)
				entry = Entry(top_frame)
				top_frame.pack(side = "top")
				label.pack(side = "left")
				entry.pack(side = "right")
				# append to fields dictionary
				self.entries[field] = entry

	def middleframe(self):
		pass
	def button_frame(self):
		button_frame = Button(self.master, text = "Compute", command = self.solution)
		button_frame.pack(side = "top")

	def solution(self):
		#print float(self.entries["What is your outstanding balance? "].get())
		months = float(self.var.get())
		outstanding_balance = float(self.entries["What is your outstanding balance? "].get())
		annual_interest_rate = float(self.entries["What is your annual interest rate? "].get())
		print months
		print outstanding_balance
		print annual_interest_rate


root = Tk()
root.geometry("500x500")
root.title("Credit Calculator: Paying Debt Off")
app = Credit_Debt(root, fields)
root.mainloop()

