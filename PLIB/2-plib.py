from mip import Model, xsum, minimize, BINARY, LinExpr

#ENTRADA
navio = ['A', 'B', 'C']
berco = [1, 2, 3, 4]
navio_berco_1 = [7, 15, 21]
navio_berco_2 = [13, 10, 15]
navio_berco_3 = [12, 13, 28]
navio_berco_4 = [14, 8, 5]

m = Model("Ex1 PLIB - Mochila")

x = [m.add_var(var_type=BINARY) for i in range(len(navio_berco_1))]
y = [m.add_var(var_type=BINARY) for i in range(len(navio_berco_2))]
z = [m.add_var(var_type=BINARY) for i in range(len(navio_berco_3))]
w = [m.add_var(var_type=BINARY) for i in range(len(navio_berco_4))]

m.objective = minimize(7*x[0] + 13*y[0] + 12*z[0] + 14*w[0] + 15*x[1] + 10*y[1] + 15*z[1] + 8*w[1] + 21*x[2] + 15*y[2] + 28*z[2] + 5*w[2])

m += x[0] + x[1] + x[2] <= 1
m += y[0] + y[1] + y[2] <= 1
m += z[0] + z[1] + z[2] <= 1
m += w[0] + w[1] + w[2] <= 1

m += x[0] + y[0] + z[0] + w[0] <= 1
m += x[1] + y[1] + z[1] + w[1] <= 1
m += x[2] + y[2] + z[2] + w[2] <= 1


# for i in 3:
#   m += x[i] <= cap_max_prod
#   m += x[i] >= 0


m.optimize() #Branch & Bound

for i in range(len(navio_berco_1)):
  print("X[{}]: {}".format(i, x[i].x)) #imprimindo os valores da variaveis

print("Valor otimo: {}".format(m.objective_value)) #valor otimo da funcao objetivo