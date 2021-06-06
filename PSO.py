import random

class PSO:
  def __init__(self, w, c1, c2, r1, r2, num_part, num_iter, random_create):
    self.w = w
    self.c1 = c1
    self.c2 = c2
    self.r1 = r1
    self.r2 = r2
    self.num_part = num_part
    self.num_iter = num_iter
    self.part = list()
    self.func_part = list()
    self.pbest_list = list()
    self.gbest = 0.0
    self.gbest_fit = 0.0
    self.random_create = random_create
    if random_create == 1:
      self.rand_create()
    else:
      self.create()

  def create(self):
    for i in range(self.num_part):
      x, v = input("Insira a posição e a velocidade do elemento " + str(i) + ": ").split(" ")
      self.part.append({"X":(float(x)-0.5)*10,"V":(float(v)-0.5), "pbest":0.0})
      self.part[i]["pbest"] = self.part[i]["X"]
      self.func_part.append(self.func(self.part[i]["X"]))
      self.pbest_list.append(self.part[i]["pbest"])
    self.gbest_fit = max(self.func_part)
    self.gbest = self.part[self.func_part.index(self.gbest_fit)]["X"]
    #########
    print("\nX = ", end="")
    for k in range(self.num_part):
      print(str(round(self.part[k]["X"], 4)), end = " ")
    print("\nV = ", end="")
    for k in range(self.num_part):
      print(str(round(self.part[k]["V"], 4)), end = " ")
    print("\nF = ", end="")
    for k in range(self.num_part):
        print(str(round(self.func_part[k], 4)), end = " ")
    #########
    print("\nLocal best position – LBP (Pbest) = " + str(self.pbest_list) + "\nGlobal best fitness = " + str(self.gbest_fit) + "\nGlobal best position – GBP (Gbest) = " + str(self.gbest) + "\n")
    self.iter()

  def rand_create(self):
    for i in range(self.num_part):
      self.part.append({"X":(random.uniform(0, 1)-0.5)*10,"V":(random.uniform(0, 1)-0.5), "pbest":0.0})
      self.part[i]["pbest"] = self.part[i]["X"]
      self.func_part.append(self.func(self.part[i]["X"]))
      self.pbest_list.append(self.part[i]["pbest"])
    self.gbest_fit = max(self.func_part)
    self.gbest = self.part[self.func_part.index(self.gbest_fit)]["X"]
    #########
    print("\nX = ", end="")
    for k in range(self.num_part):
      print(str(round(self.part[k]["X"], 4)), end = " ")
    print("\nV = ", end="")
    for k in range(self.num_part):
      print(str(round(self.part[k]["V"], 4)), end = " ")
    print("\nF = ", end="")
    for k in range(self.num_part):
        print(str(round(self.func_part[k], 4)), end = " ")
    #########
    print("\nLocal best position – LBP (Pbest) = " + str(self.pbest_list) + "\nGlobal best fitness = " + str(self.gbest_fit) + "\nGlobal best position – GBP (Gbest) = " + str(self.gbest) + "\n")
    self.iter()

  def iter(self):
    for i in range(self.num_iter-1):
      for j in range(self.num_part):
        self.part[j]["V"], self.part[j]["X"] = self.atualiza(self.part[j])
        self.func_part[j] = self.func(self.part[j]["X"])
        if self.part[j]["X"] > self.part[j]["pbest"]:
          self.part[j]["pbest"] = self.part[j]["X"]
          self.pbest_list[j] = self.part[j]["pbest"] 
          
      self.gbest_fit = max(self.func_part)
      self.gbest = self.part[self.func_part.index(self.gbest_fit)]["X"]
      #########
      print("\nX = ", end="")
      for k in range(self.num_part):
        print(str(round(self.part[k]["X"], 4)), end = " ")
      print("\nV = ", end="")
      for k in range(self.num_part):
        print(str(round(self.part[k]["V"], 4)), end = " ")
      print("\nF = ", end="")
      for k in range(self.num_part):
          print(str(round(self.func_part[k], 4)), end = " ")
      #########
      print("\nLocal best position – LBP (Pbest) = " + str(self.pbest_list) + "\nGlobal best fitness = " + str(self.gbest_fit) + "\nGlobal best position – GBP (Gbest) = " + str(self.gbest) + "\n")
  
  def atualiza(self, X):
    v = self.w * X["V"] + self.c1 * self.r1 * (X["pbest"] - X["X"]) + self.c2 * self.r2 * (self.gbest - X["X"])
    x = X["X"] + v
    return v, x

  def func(self, X):
    return 1 + 2 * X - pow(X, 2)

PSO(0.7, 0.2, 0.6, 0.4657, 0.5319, 5, 3, 0)

"""
Exemplo de Entrada
X = [0.4657, 0.8956, 0.3877, 0.4902, 0.5039]
V = [0.5319, 0.8185, 0.8331, 0.7677, 0.1708]
0.4657 0.5319
0.8956 0.8185
0.3877 0.8331
0.4902 0.7677
0.5039 0.1708
"""