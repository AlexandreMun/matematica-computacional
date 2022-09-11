from os import system
from mip import Model, minimize, INTEGER, LinExpr, xsum

#ENTRADA
semanas = [1, 2, 3, 4]
camisas_extras = [1, 2]
camisas_estocadas = [1, 2, 3]
demanda_semanal = [5000, 10000, 30000, 60000]
cap_max_prod = 25000

m = Model("Ex3")

x = [m.add_var(var_type=INTEGER) for i in range(len(semanas))]
y = [m.add_var(var_type=INTEGER) for i in range(len(camisas_extras))]
z = [m.add_var(var_type=INTEGER) for i in range(len(camisas_estocadas))]

m.objective = minimize(2 * (x[0] + x[1]) + 2.5 * (x[2] + x[3]) + 2.8 * xsum(y[i] for i in range(len(camisas_extras))) + 0.2 * xsum(z[j] for j in range(len(camisas_estocadas))))

m += x[0] + y[0] - z[0] == demanda_semanal[0]
m += x[1] + y[1] - z[0] - z[1] == demanda_semanal[1]
m += x[2] + z[1] - z[2] == demanda_semanal[2]
m += x[3] + z[2] == demanda_semanal[3]

for i in range(len(semanas)):
  m += x[i] <= cap_max_prod
  m += x[i] >= 0

m.optimize() #aqui ele vai chamar o SIMPLEX
system('cls || clear')

for i in range(len(semanas)):
  print("X[{}]: {}".format(i, x[i].x)) #imprimindo os valores da variaveis

print("Valor otimo: {}".format(m.objective_value)) #valor otimo da funcao objetivo
