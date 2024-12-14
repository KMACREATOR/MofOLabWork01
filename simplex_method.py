from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

#задаем в модели проблему максимизации
model = LpProblem(name="small-problem", sense=LpMaximize)

#огранчения на неотрицаительность переменных
x1 = LpVariable(name="x1", lowBound=0)
x2 = LpVariable(name="x2", lowBound=0)
x3 = LpVariable(name="x3", lowBound=0)

#записываем ограничения в модель
model += (2 * x1 + x2 + x3 <= 3, "first_constraint")
model += (x1  + 4 * x2 <= 6, "second_constraint")
model += (-0.5 * x2 + 2 * x3 <= 1, "third_constraint")

#записываем целевую функцию
obj_func = 7 * x1 + 3 * x2 + 4 * x3
model += obj_func


#вызываем метод для решения
status = model.solve()

#вывод в консоль: статус модели (1 означает, что решение
#найдено.
print(f"status: {model.status}, {LpStatus[model.status]}")

#model.objective.value() выводит objective - значение целевой функции
print(f"objective: {model.objective.value()}")

#вывод значений переменных решения
for var in model.variables():
    print(f"{var.name}: {var.value()}")
    
#вывод значений ограничений
for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")


'''вывод:
status: 1, Optimal
objective: 10.75
x1: 1.25
x2: 0.0
x3: 0.5
first_constraint: 0.0
second_constraint: -4.75
third_constraint: 0.0
'''