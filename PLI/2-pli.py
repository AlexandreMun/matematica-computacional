from os import system
from mip import Model, minimize, INTEGER, LinExpr

#ENTRADA
turnos = [1, 2, 3, 4, 5, 6]
qtd_de_enfermeiros = [51, 58, 62, 41, 32, 19]

m = Model("Ex2")

x = [m.add_var(var_type=INTEGER) for i in range(len(turnos))]

m.objective = minimize((800 * (x[0] + x[1])) + (1000 * (x[3] + x[4])) + (900 * (x[2] + x[5])))

m += x[0] + x[5] >= qtd_de_enfermeiros[0]
m += x[1] + x[0] >= qtd_de_enfermeiros[1]
m += x[2] + x[1] >= qtd_de_enfermeiros[2]
m += x[3] + x[2] >= qtd_de_enfermeiros[3]
m += x[4] + x[3] >= qtd_de_enfermeiros[4]
m += x[5] + x[4] >= qtd_de_enfermeiros[5]

for i in range(len(turnos)):
  m += x[i] >= 0

m.optimize() #aqui ele vai chamar o SIMPLEX
system('cls || clear')

for i in range(len(turnos)):
  print("X[{}]: {}".format(i, x[i].x)) #imprimindo os valores da variaveis

print("Valor otimo: {}".format(m.objective_value)) #valor otimo da funcao objetivo
