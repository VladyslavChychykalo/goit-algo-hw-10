from pulp import LpProblem, LpVariable, LpMaximize, LpStatus, value

model = LpProblem("Maximize_Production", LpMaximize)

lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

model += 2*lemonade + fruit_juice <= 100, "Water_Limit"
model += 1*lemonade <= 50, "Sugar_Limit"
model += 1*lemonade <= 30, "Lemon_Juice_Limit"
model += 2*fruit_juice <= 40, "Fruit_Puree_Limit"

# максимізація загальної кількості вироблених одиниць
model += lemonade + fruit_juice, "Total_Production"

model.solve()

print("Статус:", LpStatus[model.status])
print("Максимальна кількість Лимонаду:", lemonade.varValue)
print("Максимальна кількість Фруктового соку:", fruit_juice.varValue)
print("Загальна кількість продуктів:", value(model.objective))
