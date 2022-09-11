from os import system
from mip import Model, xsum, maximize, CONTINUOUS, LinExpr

#ENTRADA
gasolinas = ['verde', 'azul', 'comum']
qtds = [9000000, 4800000, 2200000]
componentes_verde = [0.22, 0.50, 0.28]
componentes_azul = [0.52, 0.34, 0.14]
componentes_comum = [0.74, 0.20, 0.06]
lucros = [0.30, 0.25, 0.20]

m = Model("EX2 - Gasolina")

x = [m.add_var(var_type=CONTINUOUS) for i in range(len(gasolinas))]

m.objective = maximize(xsum(lucros[i] * x[i] for i in range(len(gasolinas))))

m += (componentes_verde[0] * x[0] + componentes_azul[0] * x[1] + componentes_comum[0] * x[2]) <= qtds[0] # pura
m += (componentes_verde[1] * x[0] + componentes_azul[1] * x[1] + componentes_comum[1] * x[2]) <= qtds[1] # octana
m += (componentes_verde[2] * x[0] + componentes_azul[2] * x[1] + componentes_comum[2] * x[2]) <= qtds[2] # aditiva

m += (x[2]) >= 16 * x[0] # demanda
m += (x[1]) <= 600000 # demanda

for i in range(len(gasolinas)):
  m += x[i] >= 0

m.optimize() #aqui ele vai chamar o SIMPLEX
system('cls || clear')

for i in range(len(gasolinas)):
  print("X[{}]: {}".format(i, x[i].x)) #imprimindo os valores da variaveis

print("Valor otimo: {}".format(m.objective_value)) #valor otimo da funcao objetivo