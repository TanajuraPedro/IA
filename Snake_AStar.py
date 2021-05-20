# Aluno: Pedro Tanajura
# RA: 140651

import numpy as np
import math

def CriarMatrizSnake():
  # Criando a matriz do jogo snake
  s = input()
  s = s.split(" ")

  n = int(s.pop(0)) #tamanho da matriz (n,n)
  M = np.zeros((n,n), dtype=object)

  for i in range(0, n):
    for j in range(0, n):
      M[i][j] = np.array([s.pop(0), [i, j]])

  # Imprimindo a matriz
  imprime_Matriz(M, n)
  return M, n

def imprime_Matriz(M, n):
  print("")
  print("  ", end = "")
  for i in range(0, n):
    print(i, end="  ")
  print("")
  for i in range(0, n):
    print(i, end=" ")
    for j in range(0, n):
      a = M[i][j]
      print(a[0], " ", end="")
    print("")
  print("")

def imprime_Caminho(C):
  if C == -1:
    print("Não foi encontrado um caminho.")
  else:
    print("Menor Caminho:")
    for i in C:
      print(i[1],":",i[0])
      if i[0] != '$':
        print("     ↓")

def distancia2pontos(a, b):
  return math.sqrt(math.pow((b[0]-a[0]), 2) + math.pow((b[1]-a[1]), 2))

def CalculaCustosCaminhos(M, fronteira, meta, n):
  custos = []
  
  for i in fronteira:
    custo = 0
    for j in range(0, len(i)):
      if j == len(i)-1 :
        custo += distancia2pontos(i[j][1], meta)
        custos.append(custo)
      else:
        custo += distancia2pontos(i[j][1], i[j+1][1])
  
  return custos

def NaoEstaNoCaminho(novo, caminho):
  for i in caminho:
    if(i[1] == novo[1]):
      return False
  return True

def A_Star_Snake(M, n):
  for i in range(0, n):
    for j in range(0, n):
      pos = M[i][j]
      if pos[0] == 'C': # indica o local da cabeça da cobra
        inicio = pos
      elif pos[0] == '$': # indica o local onde está o alimento
        meta = pos

  fronteira = [[inicio]]

  while fronteira:
    # calcula os custos
    custos = CalculaCustosCaminhos(M, fronteira, meta[1], n)
    # posição de menor custo
    indC = custos.index(min(custos))
    caminho = fronteira.pop(indC)
    # pega o última nó do caminho
    v = caminho[-1]
    # teste de meta
    if v[0] == meta[0]:
      return caminho

    else: 
      # pega nós adjacentes, constroi um caminho e põe na fila
      posV = v[1]
      if posV[0] > 0 : #verifica se da pra ir pra cima
        novoElemento = M[posV[0]-1][posV[1]]
        if (novoElemento[0] == '.' or novoElemento[0] == '$') and NaoEstaNoCaminho(novoElemento, caminho) :
          novoCaminho = list(caminho)
          novoCaminho.append(novoElemento)
          fronteira.append(novoCaminho)
      if posV[1] > 0: #verifica se da pra ir pra esquerda
        novoElemento = M[posV[0]][posV[1]-1]
        if (novoElemento[0] == '.' or novoElemento[0] == '$') and NaoEstaNoCaminho(novoElemento, caminho) :
          novoCaminho = list(caminho)
          novoCaminho.append(novoElemento)
          fronteira.append(novoCaminho)
      if posV[0] < n-1: #verifica se da pra ir pra baixo
        novoElemento = M[posV[0]+1][posV[1]]
        if (novoElemento[0] == '.' or novoElemento[0] == '$') and NaoEstaNoCaminho(novoElemento, caminho) :
          novoCaminho = list(caminho)
          novoCaminho.append(novoElemento)
          fronteira.append(novoCaminho)
      if posV[1] < n-1: #verifica se da pra ir pra direita
        novoElemento = M[posV[0]][posV[1]+1]
        if (novoElemento[0] == '.' or novoElemento[0] == '$') and NaoEstaNoCaminho(novoElemento, caminho) :
          novoCaminho = list(caminho)
          novoCaminho.append(novoElemento)
          fronteira.append(novoCaminho)

  return -1


# Agora vamos calcular o menor caminho entre a cabeça ("C") e a fruta ("$") usando o algoritmo A*
M, n = CriarMatrizSnake()
caminho = A_Star_Snake(M, n)
imprime_Caminho(caminho)

# Exemplos de Entrada:
"""
3
* * .
C . .
. . $

10
C * * . . . . . . .
. . * . . . . . . .
. . * . . . . . . .
. * * . . . . . . .
. * . . . . . . . .
. * . . . . . . . .
. * . . . . $ . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .

10
C * * . . . . . . .
. . * . . . . . . .
. . * . . . . . . .
. * * . . . . . . .
. * . . . . . . . .
. * . . . . . . . .
* * . . . . $ . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
"""