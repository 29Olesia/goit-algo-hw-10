from pulp import *


limonad = LpVariable("Limonad", lowBound=0, cat='Integer')  
fruit_juice = LpVariable("Fruit_juice", lowBound=0, cat='Integer')  

problem = LpProblem("Maximize_Products", LpMaximize)

problem += 2 * limonad + fruit_juice <= 100  # вода
problem += limonad <= 50  # цукор
problem += limonad <= 30  # лимонний сік
problem += 2 * fruit_juice <= 40  # фруктове пюре

problem += limonad + fruit_juice

problem.solve()

print("Кількість лимонаду:", int(value(limonad)))
print("Кількість фруктового соку:", int(value(fruit_juice)))
