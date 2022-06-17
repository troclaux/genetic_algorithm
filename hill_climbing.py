
import random




def tabuleiro(n, q):
	tabuleiros = []
	for q in range(q):
		tabuleiro = []
		for i in range(n):
			tabuleiro.append(random.randint(1, n))
		tabuleiros.append(tabuleiro)
	return tabuleiros

def todosVizinhos(tabuleiro):
	vizinhos = []
	for i in tabuleiro:
		novoTabuleiro = tabuleiro.copy()
		temp = tabuleiro[i-1]
		j = 1
		while(j <= len(tabuleiro)):
			if(j == temp):
				j +=1
				continue
			novoTabuleiro[i-1] = j
			vizinhos.append(novoTabuleiro.copy())
			j += 1
	return vizinhos

def numeroAtaques(node):
	conflict = []
	for i in node:
		for j in node:
			if (i == j):
				continue
			if (node[i-1] == node[j-1]):
				if ([i, j] in conflict or [j, i] in conflict):
					continue
				print("rainha " + str(i) + " ataca rainha " + str(j))
				conflict.append([i, j])
				continue
			if (node[i-1] != node[j-1]):
				d = abs(i-j)
				if (node[i-1] == node[j-1] + d or node[i-1] == node[j-1] - d):
					if ([i, j] in conflict or [j, i] in conflict):
						continue
					print("rainha " + str(i) + " ataca rainha " + str(j))
					conflict.append([i, j])
					continue
	c = len(conflict)
	print("numero de ataques: " + str(c))
	return c

#print(todosVizinhos([1,2,3,4]))
#print(tabuleiro(4,6))