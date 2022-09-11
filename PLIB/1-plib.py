from mip import Model, xsum, maximize, BINARY, LinExpr

#ENTRADA
objetos = [1,2,3,4,5]
peso = [52,23,35,15,7]
valor = [100,60,70,15,15]
limite_mochila = 60

m = Model("Ex1 PLIB - Mochila")

x = [m.add_var(var_type=BINARY) for i in range(len(objetos))]

m.objective = maximize(xsum(valor[i]*x[i] for i in range(len(objetos))))

m += xsum(peso[i]*x[i] for i in range(len(objetos))) <= limite_mochila

m.optimize() #Branch & Bound

for i in range(len(objetos)):
  print("X[{}]: {}".format(i, x[i].x)) #imprimindo os valores da variaveis

print("Valor otimo: {}".format(m.objective_value)) #valor otimo da funcao objetivo