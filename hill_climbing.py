import random


valoresFuncaoHeuristicaPrimeiraEscolha = []
valoresFuncaoHeuristicaMelhorEscolha = []

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
	numAtaqtc = numeroAtaques(tc)
	while True:
		ts = umVizinho(tc)
		numAtaqts = numeroAtaques(ts)
		if(len(lista) == tamanhoMaximo):
			#print("minimo local: " + str(numeroAtaques(tc)))
			#print("Configuração: " + str(tc))
			par = [tc, numAtaqtc]
			valoresFuncaoHeuristicaPrimeiraEscolha.append(numAtaqtc)
			return par
		if ts in lista:
			continue
		if numAtaqts >= numAtaqtc:
			#print("numero de ataques do vizinho: " + str(numeroAtaques(ts)))
			lista.append(ts)
			#print("lista de vizinhos descobertos: " + str(lista))
		if numAtaqts < numAtaqtc:
			#print("pulei para vizinho: " + str(ts))
			valoresFuncaoHeuristicaPrimeiraEscolha.append(numAtaqtc)
			return hillClimbingPrimeiraEscolha(ts)
	
	

def hillClimbingMelhorEscolha(tabuleiro):
	tc = tabuleiro.copy()
	vizinhos = todosVizinhos(tc)
	avaliação = []
	minvizinhos = []
	for i in vizinhos:
		avaliação.append([i,numeroAtaques(i)])
	low = numeroAtaques(tc)
	for i in avaliação:
		temp = i[1]
		if temp < low:
			low = temp
	#print("low: " + str(low))
	if low == numeroAtaques(tc):
		numAtaq = numeroAtaques(tc)
		#print("minimo local: " + str(numAtaq))
		#print("Configuração: " + str(tc))
		par = [tc, numAtaq]
		#print("par: " + str(par))
		#valoresFuncaoHeuristicaMelhorEscolha.append(numAtaqtc)
		return par
	for i in avaliação:
		if i[1] == low:
			minvizinhos.append(i[0])
	#print("vizinhos minimos: " + str(minvizinhos))
	sorteado = random.sample(minvizinhos, 1)
	escolhido = sorteado[0]
	#print("escolhido: " + str(escolhido))
	#valoresFuncaoHeuristicaMelhorEscolha.append(numAtaqtc)
	return hillClimbingMelhorEscolha(escolhido)

	
def mainPrimeiraEscolha(n,q):
	EstadosFinais = []
	tabuleiros = tabuleiro(n, q)
	for i in tabuleiros:
		temp = hillClimbingPrimeiraEscolha(i)
		EstadosFinais.append(temp)
	return EstadosFinais


def mainMelhorEscolha(n,q):
	EstadosFinais = []
	tabuleiros = tabuleiro(n, q)
	for i in tabuleiros:
		temp = hillClimbingMelhorEscolha(i)
		EstadosFinais.append(temp)
	return EstadosFinais

print(mainPrimeiraEscolha(4,50))
print(mainMelhorEscolha(4,50))

#def analise(tamanhoTabuleiro, numeroSimulacoes):
#	amostraPrimeiraEscolha = mainPrimeiraEscolha(tamanhoTabuleiro, numeroSimulacoes)
#	amostraMelhorEscolha = mainPrimeiraEscolha(tamanhoTabuleiro, numeroSimulacoes)
#	for i in amostraPrimeiraEscolha

	

#hillClimbingPrimeiraEscolha([4,4,4,4])
#hillClimbingMelhorEscolha([1,2,3,4])