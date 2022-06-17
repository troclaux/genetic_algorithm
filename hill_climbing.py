
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

print(tabuleiro(4,6))