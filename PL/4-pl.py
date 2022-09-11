from mip import Model, xsum, maximize, CONTINUOUS

#ENTRADA

minerio = 3 #quantidade de minerios
metal = 4 #tipos de metal
liga = 2 #liga
qtd_max = [1000, 2000, 3000]
preco_minerio = [30,40,50]
preco_liga = [200,300]

model = Model('Liga Metalica')

x = [model.add_var(var_type=CONTINUOUS) for i in range(minerio)]
y = [[model.add_var(var_type=CONTINUOUS) for k in range(liga)] for j in range(metal)]


model.objective = maximize(200*xsum(y[j][0] for j in range(metal)) + 300*xsum(y[j][1] for j in range(metal)) - xsum(preco_minerio[i]*x[i] for i in range(minerio)) )

 
#restricao: limite de compra de minerio  
    
#for i in range(minerio):
model +=  x[0] <= qtd_max[0]
model +=  x[1] <= qtd_max[1]
model +=  x[2] <= qtd_max[2]

#restricao de limite de uso de metal    
    
model +=  y[0][0] + y[0][1] <= 0.2*x[0] + 0.1*x[1] + 0.05*x[2]
model +=  y[1][0] + y[1][1] <= 0.1*x[0] + 0.2*x[1] + 0.05*x[2]
model +=  y[2][0] + y[2][1] <= 0.3*x[0] + 0.3*x[1] + 0.7*x[2]
model +=  y[3][0] + y[3][1] <= 0.3*x[0] + 0.3*x[1] + 0.2*x[2]
  
#limite de uso de metais na liga A
model +=  y[0][0] <= 0.8*(y[0][0] + y[1][0] + y[2][0] + y[3][0])
model +=  y[1][0] <= 0.3*(y[0][0] + y[1][0] + y[2][0] + y[3][0])
model +=  y[3][0] >= 0.5*(y[0][0] + y[1][0] + y[2][0] + y[3][0])

#limite de uso de metais na liga B
model +=  y[1][1] >= 0.4*(y[0][1] + y[1][1] + y[2][1] + y[3][1])
model +=  y[1][1] <= 0.6*(y[0][1] + y[1][1] + y[2][1] + y[3][1])
model +=  y[2][1] >= 0.3*(y[0][1] + y[1][1] + y[2][1] + y[3][1])
model +=  y[3][1] >= 0.7*(y[0][1] + y[1][1] + y[2][1] + y[3][1])

#metais que nao sao utilizados
model += y[2][0] == 0
model += y[0][1] == 0

#restricao de nao negatividade
for i in range(minerio):
    model +=  x[i] >= 0
                                    
for j in range(metal):
    for k in range(liga):
        model +=  y[j][k] >= 0
                                    
                                    
model.write('model.lp')

model.optimize() #SIMPLEX
                                       
if model.num_solutions:
    print(model.objective_value)

    for i in range(minerio):            
        print(f'x{i+1} = {x[i].x}')
    
    for j in range(metal):
        for k in range(liga):
            print(f'y{j+1},{k+1} = {y[j][k].x}')
