from Tkinter import *

fields = ("What is your outstanding balance?", 
	"What is your annual interest rate?", 
	"What is your minimum monthly payment rate?")

class App():
	def __init__(self, master, fields):
		self.master = master
		self.topframe(fields)
		self.bottomframe()
		self.buttonframe()


	def topframe(self, fields):
		#dictionary to store the entry values
		self.entries = {}
       	
       	# for loop will create the label and entry fields
		for field in fields:
			top_frame = Frame(self.master, bg = "grey", bd = 1, relief = "groove")
			label = Label(top_frame, bg = "grey", text = field + " : ")
			entry = Entry(top_frame, bd = 3, highlightbackground = "grey", relief = "sunken")
			top_frame.pack(side = "top", fill = "x")
			label.pack(side = "left")
			entry.pack(side = "right")

			# append the dictionary value and keys
			self.entries[field] = entry


		"""
		# initializing frame
		top_frame = Frame(self.master, bg = "grey", bd = 1, relief = "groove")
		top_frame.pack(side = "top", fill = "both")

		# first label and entry field
		self.label1 = Label(top_frame, text = "What is your outstanding balance?", bg = "grey")
		self.label1.grid(column = 0, row = 0, sticky = "w")
		self.entry1 = Entry(top_frame, bd = 3, highlightbackground = "grey", relief = "sunken")
		self.entry1.grid(column = 1, row = 0, ipadx = 2,ipady = 2)

		# second label and entry field
		self.label2 = Label(top_frame, text = "What is your annual interest rate?", bg = "grey")
		self.label2.grid(column = 0, row = 1, sticky = "w")
		self.entry2 = Entry(top_frame, bd = 3, highlightbackground = "grey", relief = "sunken")
		self.entry2.grid(column = 1, row = 1, ipadx = 2, ipady = 2)

		# third label and entry field
		self.label3 = Label(top_frame, text = "What is your minimum monthly payment rate?", bg = "grey")
		self.label3.grid(column = 0, row = 2, sticky = "w")
		self.entry3 = Entry(top_frame, bd = 3, highlightbackground = "grey", relief = "sunken")
		self.entry3.grid(column = 1, row = 2, ipadx = 2, ipady = 2)
		"""
	def bottomframe(self):
		# initializing center (solution text box) frame
		bottom_frame = Frame(self.master, bg = "grey", bd = 1, relief = "groove")
		bottom_frame.pack(side = "top", fill = "both", expand = True)
		
		# initializing text widget to display the solution
		self.solution_frame = Text(bottom_frame, relief = "groove") # height = 20, width = 60 
		self.solution_frame.pack(side = "left", fill = "both", expand = True) # fill = "both", expand = True
	
	def buttonframe(self):
		# initilaize the button frame
		button_frame = Frame(self.master, bg = "grey", bd = 1, relief = "groove")
		button_frame.pack(side = "top", fill = "x")

		# initialize the button and its command
		compute_button = Button(button_frame, text = "Compute", highlightbackground = "grey",  command = self.solution)
		compute_button.pack(side = "top")

	def solution(self):
		init_outstanding_balance = float(self.entries["What is your outstanding balance?"].get())
		annual_interest_rate = float(self.entries["What is your annual interest rate?"].get())
		min_monthly_payment_rate = float(self.entries["What is your minimum monthly payment rate?"].get())

		# call paying the min method below
		self.paying_the_min(init_outstanding_balance, annual_interest_rate, min_monthly_payment_rate)
		
	def paying_the_min(self, init_outstanding_balance, annual_interest_rate, min_monthly_payment_rate):
		for m in range(1, 13):
			min_monthly_amount = min_monthly_payment_rate * init_outstanding_balance
			interest_paid = (annual_interest_rate / 12) * init_outstanding_balance
			principle_paid = min_monthly_amount - interest_paid
			remaining_new_balance = init_outstanding_balance - principle_paid
			init_outstanding_balance = remaining_new_balance

			# print to text frame 
			self.final = """
			Month: %d
			Minimum monthly payment: %s
			Principle paid: %s
			Remaining balance: %s

			""" % (m, min_monthly_amount, float(principle_paid), float(remaining_new_balance))

			# print to text frame
			self.solution_frame.insert(END, self.final)

		self.final = """
Your remaining credit card balance after 12 months paying the minimum
at an annual interest rate of %s is %s
			""" % (str(annual_interest_rate), str(remaining_new_balance))
		
		# print to text frame
		self.solution_frame.insert(END, self.final)

root = Tk()
root.geometry("510x510")
root.configure(bg = "grey")
root.title("Credit Calculator: Paying The Minimum")
app = App(root, fields)
root.mainloop()

