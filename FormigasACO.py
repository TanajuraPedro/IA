import numpy as np

class Matriz_Caminhos:
  def __init__(self, num_v, tau):
    self.num_v = num_v
    self.tau = tau
    self.M_peso = np.zeros((self.num_v, self.num_v))
    self.M_fero = np.zeros((self.num_v, self.num_v))
    s = input("Digite os pesos da arestas: ").split(" ")
    for i in range(self.num_v):
      for j in range(self.num_v):
        self.M_peso[i][j] = int(s.pop(0))
        self.M_fero[i][j] = self.tau
    self.imprime()
  
  def imprime(self):
    print("\nMatriz de Pesos\n" + str(self.M_peso) + "\n")
    print("Matriz de Feromônios\n" + str(self.M_fero) + "\n")

  def get_peso(self, i, j):
    return self.M_peso[i][j]
  def get_fero(self, i, j):
    return self.M_fero[i][j]
  def set_fero(self, i, j, valor):
    self.M_fero[i][j] = valor

class FormigasACO:
  def __init__(self, num_v, alfa, beta, rho, tau, iter):
    self.M = Matriz_Caminhos(num_v, tau)
    self.num_v = num_v
    self.alfa = alfa
    self.beta = beta
    self.rho = rho
    self.tau = tau
    self.iter = iter

    self.fit()

  def fit(self):
    for j in range(self.iter):
      print("step: " + str(j+1))
      for i in range(self.num_v):
        print(self.caminho_provavel(i))
    self.M.imprime()
      

  def caminho_provavel(self, pos):
    sum = 0
    custo = 0
    visitados = list()
    visitados.append(pos)
    for i in range(self.num_v-1):
      sum = 0
      for j in range(self.num_v):
        if j in visitados:
          continue
        sum = sum + self.prob_aresta(pos, j)
      #print(sum)
    
      prob_list = list()
      index_list = list()
      for j in range(self.num_v):
        if j in visitados:
          continue
        #print("  " + str(pos) + str(j) + " : " + str(self.prob_aresta(pos, j)/sum))
        prob_list.append(self.prob_aresta(pos, j)/sum)
        index_list.append(j)
        self.atualiza_fero(pos, j)
      
      v_provavel = index_list[prob_list.index(max(prob_list))]
      custo = custo + self.M.get_peso(pos, v_provavel)
      visitados.append(v_provavel)
      pos = v_provavel

    return visitados, custo

  def atualiza_fero(self, i, j):
    valor = (1-self.rho) * self.M.get_fero(i,j) + self.rho * (1.0/self.M.get_peso(i,j))
    self.M.set_fero(i, j, valor)

  def prob_aresta(self, i, j):
    return self.alfa * self.M.get_fero(i,j) * self.beta * (1.0/self.M.get_peso(i,j))


FormigasACO(5, 1, 1, 0.5, 2.0, 3)

"""
Exemplo de Entrada

0 2 10 8 3
1 0 2 5 7
9 1 0 3 6
10 4 3 0 2
2 7 5 1 0
"""
