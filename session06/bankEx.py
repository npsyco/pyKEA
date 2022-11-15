class Bank:

    def __init__(self, name, address, dept):
        self.name = name
        self.address = address
        self.dept = dept
    
    def __str__(self):
        return f"Bank name: {self.name}\n Address: {self.address}\n Department: {self.dept}"

class Account(Bank):
    def __init__(self, customer, balance, dept):
        self.customer = customer
        self.balance = balance
        self.dept = dept

class Customer(Account):
    def __init__(self, name, address, ssn, dept):
        self.name = name
        self.address = address
        self.ssn = ssn
        self.dept = dept
        
    def __str__(self):
        return f"Customer name: {self.name}\n Address: {self.address}\n Social Security: {self.ssn}\n Department: {self.dept}"


if __name__ == "__main__":
    
    bank1 = Bank("First Bank", "10 Wall St.", "NY-01")
    cust1 = Customer("Name", "Address", 121212, "AZ-01")
    print(bank1)
    print(cust1)
