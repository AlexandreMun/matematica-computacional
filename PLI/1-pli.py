from os import system
from mip import Model, xsum, maximize, INTEGER, LinExpr

#ENTRADA
caminhoes = ['grandes', 'pequenos']
capidades_caminhoes = [40000, 30000]
custos_operacionais = [0.30, 0.25]
transportar = 400000
milhas = 800

m = Model("Ex1")

x = [m.add_var(var_type=INTEGER) for i in range(len(caminhoes))]

m.objective = maximize(xsum(milhas * custos_operacionais[i] * x[i] for i in range(len(caminhoes))))

m += x[0] <= 10
m += x[1] <= 5

m += xsum(capidades_caminhoes[i] * x[i] for i in range(len(caminhoes))) <= transportar
# m += 2 * x[0] + x[1] <= 10
# m += x[0] >= (x[1]/2)
m += x[0] <= 10 - (x[1]/2)

for i in range(len(caminhoes)):
  m += x[i] >= 0

m.optimize() #aqui ele vai chamar o SIMPLEX
system('cls || clear')

for i in range(len(caminhoes)):
  print("X[{}]: {}".format(i, x[i].x)) #imprimindo os valores da variaveis

print("Valor otimo: {}".format(m.objective_value)) #valor otimo da funcao objetivo
