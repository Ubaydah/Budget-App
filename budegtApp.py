class Budget:

    """
    A budget app to compute for some functions for  categories

    """

    def __init__(self, category):
        self.category = category
        
    # Money deposited
    def deposit(self, d_amount):
        return d_amount

    #Money withdrawn
    def withdraw(self, w_amount):
        return w_amount

    #Get the balance remaining in the category
    def getBalance(self, d_amount = 0, w_amount = 0):
        depositM = self.deposit(d_amount)
        Withdrawal = self.withdraw(w_amount)
        balance = depositM - Withdrawal
        return balance

    #Transfer to a category
    def transfer(self, transfer):
        return transfer
        
Entertainment = Budget("Entertainment")
Food = Budget("Food")
Clothing = Budget("Clothing")
entertainment_d = Entertainment.deposit(500)
entertainment_w = Entertainment.withdraw(100)
entertainment_b = Entertainment.getBalance(entertainment_d, entertainment_w)
Food_t = Food.transfer(entertainment_b)
print(Food_t)
