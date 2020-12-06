import gurobipy as gp
from gurobipy import GRB

from atividade8_MO824.utils import generate_triples, read_input

size = 20
filename = "instances/qbf0{}.txt".format(size) if size < 100 else "instances/qbf{}.txt".format(size)
coefficients = read_input(filename)
triples = generate_triples(size)

model = gp.Model("max_qbftp quadratic")
x_vars = {}
for i in range(1, size+1):
    x_vars[i] = model.addVar(vtype=GRB.BINARY, name="x_{}".format(i))

objective = 0
for i in range(1, size + 1):
    x_i = x_vars[i]
    for j in range(i, size + 1):
        x_j = x_vars[j]
        objective += coefficients[(i, j)] * x_i * x_j

model.setObjective(objective, GRB.MAXIMIZE)

for index, triple in enumerate(triples):
    i, j, k = triple
    model.addConstr(x_vars[i] + x_vars[j] + x_vars[k] <= 2, "c_{}".format(index))

#set time limit to 5 minutes
model.setParam('TimeLimit', 5*60)
# Optimize model
model.optimize()
print('Objective: {}'.format(model.objVal))