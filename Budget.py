class Budget:
    balances = {}

    def __init__(self, category):
        self.category = category.lower()
        try:
            Budget.balances[self.category]
            # print("category " + self.category + " exists, make we rest")
        except:
            # print("category " + self.category + " does not exist, creating an index")
            Budget.balances[self.category] = 0
        
    def canTransfer(self, amount):
        balance = Budget.balances[self.category]
        if(amount > balance):
          return False
        return True
        

    def getBalance(self):
        return Budget.balances[self.category]
    
    def deposit(self, amount):
        Budget.balances[self.category] += amount
    
    def withdraw(self, amount):
        if(self.canTransfer(amount)):
            Budget.balances[self.category] -= amount
            return
        print("CANNOT WITHDRAW, reason insufficient funds")
    
    def getAllBalances(self):
        return Budget.balances

    def transfer(self, destination, amount):
        if(self.canTransfer(amount)):
            category = destination.category
            Budget.balances[self.category] -= amount
            Budget.balances[category] += amount
        print("CANNOT TRANSFER, reason: insufficient funds")


    

    
    