
from Tkinter import *
import Main_creditcard_functions

symbols = ("$", "%", "")
dropdown_choices = (6, 12, 18, 24)
fields = ("What is your outstanding balance? ", "What is your annual interest rate? ", 
    "How many months? ")
solution_message = """*************RESULTS*************
Monthly payment needed to pay off
debt in %d months is $%s
*
Number of months needed: %d
Balance: $%s

"""

class Credit_Debt():
    def __init__(self, master, fields, symbols):
        self.master = master
        self.labelframe()
        self.topframe(fields, symbols)
        self.middleframe()
        self.buttonframe()

    def labelframe(self):
        """ 
        'Payoff Calculator' and 'What will it take to pay of my credit debt?''
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
        self.solution_display.pack(side = "top", expand = True)

    def buttonframe(self):
        #'compute' button will call the solution method
  
        button_frame = Frame(self.master, bg = "seagreen3")
        button_frame.pack(side = "bottom", fill = "both", pady = 4)
        
        button = Button(button_frame, bd = 0, width = 48, 
            highlightbackground = "seagreen3", text = "Compute", 
            command = self.solution)
        button.pack(side = "top", padx = 3, pady = 3, ipadx = 1, ipady = 1)

    def solution(self):
        """
        Retrieve values from self.entries dictionary and call
        paying_debt_year method with values.
        """
        self.months = float(self.var.get()) 
        self.outstanding_balance = float(self.entries
            ["What is your outstanding balance? "].get())
        self.annual_interest_rate = float(self.entries
            ["What is your annual interest rate? "].get())

        monthly_lower_bound = self.outstanding_balance / self.months
        monthly_upper_bound = ((self.outstanding_balance * 
            (1 + (self.annual_interest_rate / 12.0)) ** self.months) / self.months)

##        # call to paying_debt_year method
##        computation = Main_creditcard_functions.paying_debt_year(monthly_lower_bound, 
##            monthly_upper_bound, self.outstanding_balance, 
##            self.annual_interest_rate)

        # call to paying_debt_x_months method
        computation = Main_creditcard_functions.paying_debt_x_month( 
            self.outstanding_balance, self.annual_interest_rate, 
            self.months, monthly_lower_bound, monthly_upper_bound)
        
        # round to results to 2 decimel places
        min_pay = round(computation[0],2)
        bal = round(computation[2],2)
        
        # message printed to screen
        sm = solution_message % (computation[1], min_pay, computation[1], bal)

        # updates text widget with the new message 
        self.solution_display.insert(END, sm)
       
root = Tk()
root.geometry("500x600")
root.title("Payoff Calculator")
app = Credit_Debt(root, fields, symbols)
root.mainloop()
