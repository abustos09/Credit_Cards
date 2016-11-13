
from Tkinter import *

symbols = ("$", "%", "")
dropdown_choices = (6, 12, 18, 24)
fields = ("What is your outstanding balance? ", "What is your annual interest rate? ", 
    "How many months? ")

class Credit_Debt():
    def __init__(self, master, fields, symbols):
        self.master = master
        self.labelframe()
        self.topframe(fields, symbols)
        self.middleframe()
        self.buttonframe()

    def labelframe(self):
        """ 'Payoff Calculator' and 'What will it take to pay of my credit debt?''
        labels
        """
        label1 = Label(self.master, text = "Payoff Calculator", bg = "white", 
            anchor = "w", padx = 10, pady = 20, font = ("helvetica", 30))
        label1.pack(side = "top", fill = "x")

        label2 = Label(self.master, text = "What will it take to pay of my credit debt?", 
            bg = "cornflower blue", anchor = "w", padx = 10, pady = 10, fg = "white", 
            font = ("helvetica", 15))
        label2.pack(side = "top", fill = "x")
                
    def topframe(self, fields, symbols):
        """
        One frame with label, entry and optionmenu widgets.
        Entry fields will will be stored in the self.entries dictionary -
        key = label str : value = float.
        """
        self.entries = {}
        for (field, symbol) in zip(fields, symbols):
            top_frame = Frame(self.master, bg = "cornflower blue")
            top_frame.pack(side = "top", fill = "x")
            label = Label(top_frame, text = field, pady = 5, 
                padx = 10, anchor = "w", font = ("helvetica", 15))
            label.pack(side = "top", fill = "x")
            if field == "How many months? ": # will produce a drop down menu
                self.var = StringVar(top_frame)
                self.var.set("Months")
                dropdown = OptionMenu(top_frame, self.var, *dropdown_choices)
                dropdown.pack(side = "top", fill = "x")
            else: #will produce label and entry fields
                symbollabel = Label(top_frame, text = symbol, fg = "white", 
                    bg = "cornflower blue", font = ("helvetica", 15), anchor = "w")
                symbollabel.pack(side = "left", fill = "x")
                entry = Entry(top_frame, bd = 0)
                entry.pack(side = "right", fill = "x",expand = True, padx = 3, 
                    pady = 3, ipadx = 1, ipady = 1)
                self.entries[field] = entry

    def middleframe(self):
        """
        middle_frame = Frame(self.master)
        middle_frame.pack(side = "top")
        """
        self.solution_display = Text(self.master, width = 55, height = 15, 
            highlightbackground = "lightgrey")
        self.solution_display.pack(side = "top")

    def buttonframe(self):
        """
        'compute' button will call the solution method
        """
        
        button_frame = Frame(self.master, bg = "seagreen3")
        button_frame.pack(side = "top", fill = "both", pady = 4, expand = True)
        
        button = Button(button_frame, bd = 0, width = 48, 
            highlightbackground = "seagreen3", text = "Compute", 
            command = self.solution)
        button.pack(side = "top", padx = 3, pady = 3, ipadx = 1, ipady = 1)

    def solution(self):
        """
        Retrieve values from self.entries dictionary and call
        paying_debt_year method with values.
        """
        months = float(self.var.get()) #no functionality at the moment
        self.outstanding_balance = float(self.entries
            ["What is your outstanding balance? "].get())
        self.annual_interest_rate = float(self.entries
            ["What is your annual interest rate? "].get())
        monthly_lower_bound = self.outstanding_balance / 12.0 # 12 is set because we are looking to pay this off in a year
        monthly_upper_bound = ((self.outstanding_balance * 
            (1 + (self.annual_interest_rate / 12.0)) ** 12.0) / 12.0)

        # call to paying_debt_year method
        self.paying_debt_year(monthly_lower_bound, monthly_upper_bound)
        print self.month_sol
        print self.updated_balance_each_month_sol
        print self.monthly_payment_sol

        sol_dis = """
        ********** RESULTS ***********
        Monthly payment to pay off debt in 1 year: %f
        Number of months needed: %f
        Balance: %f
        """ % (self.monthly_payment_sol,self.month_sol, self.updated_balance_each_month_sol)

        self.solution_display.insert(END, sol_dis)
            
        
    def paying_debt_year(self, monthly_lower_bound, monthly_upper_bound):
        """
        method will use bisection search and recursion to return 
        the minimum monthly payment amount thats needed to pay
        off credit card balance. User will select the length of time
        in months from drop down, and method will calculate compounding
        interest and updated balance.
        """ 
        month = 0
        epsilon = .1
        previous_balance = self.outstanding_balance
        monthly_interest_rate = self.annual_interest_rate / 12.0
        minimum_monthly_payment = (monthly_upper_bound + monthly_lower_bound) / 2.0

        while previous_balance > epsilon:
            month += 1
            updated_balance_each_month = previous_balance \
            * (1 + monthly_interest_rate) - minimum_monthly_payment
            previous_balance = updated_balance_each_month
            if month >= 12:
                break        

        if abs(previous_balance) > epsilon:
            if previous_balance > 0:
                monthly_lower_bound = minimum_monthly_payment
                self.paying_debt_year(monthly_lower_bound, monthly_upper_bound)
            elif previous_balance < 0:
                monthly_upper_bound = minimum_monthly_payment
                self.paying_debt_year(monthly_lower_bound, monthly_upper_bound)          
        else:
            if previous_balance > 0:
                monthly_lower_bound = minimum_monthly_payment
                self.paying_debt_year(monthly_lower_bound, monthly_upper_bound)
            else:       
                print "********** RESULTS ***********"
                print "Monthly payment to pay off debt in 1 year: " + str(minimum_monthly_payment)
                print "Number of months needed: " + str(month)
                print "Balance: " + str(updated_balance_each_month)
                self.month_sol = month
                self.updated_balance_each_month_sol = updated_balance_each_month
                self.monthly_payment_sol = minimum_monthly_payment

root = Tk()
root.geometry("500x600")
root.title("Payoff Calculator")
app = Credit_Debt(root, fields, symbols)
root.mainloop()
