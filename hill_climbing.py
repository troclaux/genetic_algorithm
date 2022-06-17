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
	for k in range(0,len(tabuleiro)):
		novoTabuleiro = tabuleiro.copy()
		temp = tabuleiro[k]
		j = 1
		while(j <= len(tabuleiro)):
			if(j == temp):
				j +=1
				continue
			novoTabuleiro[k] = j
			vizinhos.append(novoTabuleiro.copy())
			j += 1
	return vizinhos

def umVizinho(tabuleiro):
	vizinhos = todosVizinhos(tabuleiro)
	sorteado = random.sample(vizinhos, 1)
	escolhido = sorteado[0]
	return escolhido

def numeroAtaques(node):
	conflict = []
	for i in range(0,len(node)):
		for j in range(0,len(node)):
			if (i == j):
				continue
			if (node[i] == node[j]):
				if ([i, j] in conflict or [j, i] in conflict):
					continue
				#print("rainha " + str(i) + " ataca rainha " + str(j))
				conflict.append([i, j])
				continue
			if (node[i] != node[j]):
				d = abs(i-j)
				if (node[i] == node[j] + d or node[i] == node[j] - d):
					if ([i, j] in conflict or [j, i] in conflict):
						continue
					#print("rainha " + str(i) + " ataca rainha " + str(j))
					conflict.append([i, j])
					continue
	c = len(conflict)
	#print("numero de ataques: " + str(c))
	return c

def hillClimbingPrimeiraEscolha(tabuleiro):
	tc = tabuleiro.copy()
	tamanhoTabuleiro = len(tabuleiro)
	tamanhoMaximo = (tamanhoTabuleiro**2 - tamanhoTabuleiro)
	lista = []
	while True:
		ts = umVizinho(tc)
		if(len(lista) == tamanhoMaximo):
			print("minimo local: " + str(numeroAtaques(tc)))
			print("Configuração: " + str(tc))
			break
		if ts in lista:
			continue
		if numeroAtaques(ts) >= numeroAtaques(tc):
			print("numero de ataques do vizinho: " + str(numeroAtaques(ts)))
			lista.append(ts)
			print("lista de vizinhos descobertos: " + str(lista))
		if numeroAtaques(ts) < numeroAtaques(tc):
			print("pulei para vizinho: " + str(ts))
			hillClimbingPrimeiraEscolha(ts)
			break

def hillClimbingMelhorEscolha(tabuleiro):
	tc = tabuleiro.copy()
	vizinhos = todosVizinhos(tc)
	avaliação = []
	for i in vizinhos:
		avaliação.append([i,numeroAtaques(i)])
	for j in avaliação:
		
	

print(hillClimbingPrimeiraEscolha([4,4,4,4]))
#print(todosVizinhos([3,2,1,4]))
#umVizinho([1,2,3,4])
#print(numeroAtaques([4,4,4,4]))