
import random



def tabuleiro(tamanho):
	tabuleiro = []
	for i in range(0, tamanho):
		numero_aleatorio = random.randint(0, tamanho)
		tabuleiro.append(numero_aleatorio)
	return tabuleiro

print(tabuleiro(5))