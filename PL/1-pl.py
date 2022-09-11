from os import system
from mip import Model, xsum, maximize, CONTINUOUS, LinExpr

#ENTRADA
graos = ['trigo', 'arroz', 'milho']
terra = 200 #quantidade de ha disponivel
prod = [1800,2100,2900]
armazenamento = 700000 #limite de armazenamento (Kg)
consumo = [12,16,20] #consumo da fazenda (ha)
lucro = [1.2 * prod[0], 0.6 * prod[1], 0.28 * prod[2]] #lucro da fazenda

m = Model("Ex1 - Fazenda")

x = [m.add_var(var_type=CONTINUOUS) for i in range(len(graos))]

m.objective = maximize(xsum(lucro[i]*x[i] for i in range(len(graos))))

m += xsum(x[i] for i in range(len(graos))) <= terra

m += xsum(prod[i]*x[i] for i in range(len(graos))) <= armazenamento

for i in range(len(graos)):
  m += x[i] >= consumo[i]

m.optimize() #aqui ele vai chamar o SIMPLEX
system('cls || clear')

for i in range(len(graos)):
  print("X[{}]: {}".format(i, x[i].x)) #imprimindo os valores da variaveis

print("Valor otimo: {}".format(m.objective_value)) #valor otimo da funcao objetivo