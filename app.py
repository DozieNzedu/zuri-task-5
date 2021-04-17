from Budget import Budget
import math

foodBudget = Budget("Food")
foodBudget.deposit(100)
foodBudget1 = Budget("food")
foodBudget1.withdraw(29)
# foodBudget.deposit(39)
clothesBudget = Budget("clothing")

# foodBudget.transfer(clothesBudget, 1000)
# print(foodBudget.getBalance(), clothesBudget.getBalance(), Budget.balances)
print(clothesBudget.getAllBalances())