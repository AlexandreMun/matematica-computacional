from mip import Model, xsum, maximize, CONTINUOUS, LinExpr
import numpy as np

#ENTRADA

G = np.zeros((7,7), dtype=np.int64)
G[0][1] = 6
G[0][2] = 7
G[1][2] = 1
G[1][3] = 3
G[1][4] = 4
G[2][4] = 2
G[2][5] = 5
G[3][4] = 3
G[3][5] = 2
G[4][6] = 7
G[5][4] = 2
G[5][6] = 6

n = 7 #numero de vertices

m = Model("Ex5")

x = [[m.add_var(var_type=CONTINUOUS) for u in range(n)] for v in range(n)]

# m.objective = maximize(xsum(x[u][v] for u in range(n) for v in range(n)) == xsum(x[v][u] for u in range(n)  for v in range(n)) )
m.objective = maximize(G[0][1]+G[0][2])

#conjunto de restrições 1:
# for v in range(1,(n-1)):
#   m += xsum(x[u][v] for u in range(n) if G[u][v] != 0) -  xsum(x[v][u] for u in range(n) if G[v][u] != 0) == 0  
# m += x[4][6] + x[5][6] - (x[0][1] + x[0][2]) == 0
# m += x[0][1] - (x[1][2] + x[1][3] + x[1][4]) == 0
# m += x[0][2] + x[1][2] - (x[2][3] + x[2][5]) == 0
# m += x[2][4] + x[3][4] + x[5][4] - x[4][6] == 0
# m += x[2][5] + x[3][5] - (x[5][4] + x[5][6]) == 0

# for v in range(1,(n-1)):
# m += xsum(G[u][v] for u in range(n) for v in range(n)) == xsum(G[v][u] for u in range(n) for v in range(n))


#restrições 2:
# m += xsum(x[0][u] for u in range(n) if G[0][u] != 0) == 1

#restrições 3:
# m += xsum(x[u][(n-1)] for u in range(n) if G[u][(n-1)] != 0) == 1

m.optimize() #aqui ele vai chamar o B&B

for u in range(n):
  for v in range(n):
    if G[u][v] != 0:
      print("X[{}{}]: {}".format(u,v, x[u][v].x)) #imprimindo os valores da variaveis

print("Valor otimo: {}".format(m.objective_value)) #valor otimo da funcao objetivo
