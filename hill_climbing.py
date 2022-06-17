
import random




def tabuleiro(n, q):
	tabuleiros = []
	for q in range(q):
		tabuleiro = []
		for i in range(n):
			tabuleiro.append(random.randint(1, n))
		tabuleiros.append(tabuleiro)
	return tabuleiros

# def todosVizinhos(tabuleiro):
# 	for i in range(1, len(tabuleiro)):


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

print(tabuleiro(4,6))