from os import system
from mip import Model, xsum, maximize, CONTINUOUS, LinExpr

#ENTRADA
variaveis = ['CP320', 'AF25', 'clinquer']
componentes_CP320 = [0.85, 0.75, 0.03, 0.05]
componentes_AF25 = [0.50, 0.45, 0.02, 0.02]
limite_max = 1100000
venda_clinquer = 200000
compras = [180000, 50000]
contr_marginal = [41.00, 37.80, 34.40]
preco_componentes = [22.10, 34.20, 1.90]

m = Model("EX3 - Cimento")

x = [m.add_var(var_type=CONTINUOUS) for i in range(len(variaveis))]

m.objective = maximize((xsum(contr_marginal[i] * x[i] for i in range(len(variaveis))) - 
  (preco_componentes[0] * (componentes_CP320[1] * x[0] + componentes_AF25[1] * x[1])) - 
  (preco_componentes[1] * (componentes_CP320[2] * x[0] + componentes_AF25[2] * x[1])) -
  (preco_componentes[2] * (componentes_CP320[3] * x[0] + componentes_AF25[3] * x[1]))))

m += (x[0] + x[1]) <= limite_max
m += (componentes_CP320[0] * x[0] + componentes_AF25[0] * x[1] + x[2]) <= limite_max
m += x[2] <= venda_clinquer
m += (componentes_CP320[1] * x[0] + componentes_AF25[1] * x[1]) <= compras[0]
m += ((componentes_CP320[2] * x[0] + componentes_AF25[2] * x[1]) and (componentes_CP320[3] * x[0] + componentes_AF25[3] * x[1])) <= compras[1]

for i in range(len(variaveis)):
  m += x[i] >= 0

m.optimize() #aqui ele vai chamar o SIMPLEX
system('cls || clear')

for i in range(len(variaveis)):
  print("X[{}]: {}".format(i, x[i].x)) #imprimindo os valores da variaveis

print("Valor otimo: {}".format(m.objective_value)) #valor otimo da funcao objetivo