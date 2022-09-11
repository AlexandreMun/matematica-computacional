from mip import Model, xsum, minimize, BINARY, LinExpr
import numpy as np

#ENTRADA

G = np.zeros((6,6), dtype=np.int64)
G[0][1] = 41
G[0][2] = 44
G[1][3] = 37
G[3][5] = 45
G[2][4] = 27
G[4][5] = 4
G[0][4] = 500

n = 6 #numero de vertices

m = Model("Ex4 - PLIB")

x = [[m.add_var(var_type=BINARY) for u in range(n)] for v in range(n)]

m.objective = minimize(xsum(G[u][v]*x[u][v] for u in range(n) for v in range(n) if G[u][v] != 0 ))

#conjunto de restrições 1:
for v in range(1,(n-1)):
  m += xsum(x[u][v] for u in range(n) if G[u][v] != 0) -  xsum(x[v][u] for u in range(n) if G[v][u] != 0) == 0  


#restrições 2:
m += xsum(x[0][u] for u in range(n) if G[0][u] != 0) == 1

#restrições 3:
m += xsum(x[u][(n-1)] for u in range(n) if G[u][(n-1)] != 0) == 1

m.optimize() #aqui ele vai chamar o B&B

for u in range(n):
  for v in range(n):
    if G[u][v] != 0:
      print("X[{}{}]: {}".format(u,v, x[u][v].x)) #imprimindo os valores da variaveis

print("Valor otimo: {}".format(m.objective_value)) #valor otimo da funcao objetivo
