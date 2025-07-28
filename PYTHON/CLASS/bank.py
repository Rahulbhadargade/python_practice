'''class banking:
    bank_name = "SBI"
    ifsc = "SBI0001234"

    def display(self):
        print("Customer Name:", self.cname)
        print("Account No:", self.acc_no)
        print("Balance:", self.bal)

    def deposit(self, amt):
        self.bal = self.bal + amt

    def withdraw(self, amt):
        self.bal = self.bal - amt
cust1 = banking()
cust1.cname = "Rahul"
cust1.acc_no = "123456"
cust1.bal = 5000

cust2 = banking()
cust2.cname = "Amit"
cust2.acc_no = "987654"
cust2.bal = 5000

cust1.display()
cust1.deposit(20000)
cust1.display()
cust1.withdraw(17000)
cust1.display()
cust1.withdraw(5000)
cust1.display()
cust1.deposit(15000)

cust2.display()
cust2.deposit(50000)
cust2.display()
cust2.withdraw(55000)
cust2.display()
cust2.withdraw(5000)
cust2.display()
cust2.deposit(100000)
'''

'''class banking:
    bank_name = "SBI"
    ifsc = "SBI0001234"

    def display(self):
        print("Customer Name:", self.cname)
        print("Account No:", self.acc_no)
        print("Balance:", self.bal)

    def deposit(self, amt):
        self.bal = self.bal + amt
        print("Deposited:", amt)

    def withdraw(self, amt):
        check = self.bal >= amt
        self.bal = self.bal - amt * check
        print("Withdrawn:", amt * check + 0 * (not check))
        print("Insufficient Balance!" * (not check))


# Create Customer
cust = banking()
cust.cname = "Rahul"
cust.acc_no = "123456"
cust.bal = 0

# Test Cases
cust.display()

cust.withdraw(1000)
cust.display()

cust.deposit(3000) 
cust.display()'''

class banking:
    bank_name = "SBI"
    ifsc = "SBI0001234"

    def __init__(self, cname="", acc_no="", bal=0):
        self.cname = cname
        self.acc_no = acc_no
        self.bal = bal

    def display(self):
        print("C_Name:", self.cname)
        print("Acc_No:", self.acc_no)
        print("Balance:", self.bal)

    def deposit(self, amt):
        self.bal += amt
        print("Deposited:", amt)

    def withdraw(self, amt):
        if self.bal >= amt:
            self.bal -= amt
            print("Withdrawn:", amt)
        else:
            print("Insufficient Balance!")

cust = banking("Rahul", "123456", 0)