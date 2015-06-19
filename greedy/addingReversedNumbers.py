#coding: utf-8
#Os Comediantes antigas de Malidinesia preferem comédias a tragédias. Infelizmente, a maioria das peças antigas são tragédias. Portanto, o conselheiro dramático de ACM decidiu transfigurar algumas tragédias em comédias. Obviamente, este trabalho é muito difícil, porque o sentido básico da peça deve ser mantida intacta, apesar de todas as coisas mudam para seus opostos. Por exemplo, os números: se qualquer número aparece na tragédia, ele deve ser convertido na sua forma invertida antes de ser aceito no jogo comédia.
#Número revertida é um número escrito em algarismos árabes, mas a ordem de dígitos é invertida. O primeiro dígito torna-se passado e vice-versa. Por exemplo, se o herói principal teve 1245 morangos na tragédia, ele tem 5421 deles agora. Note-se que todos os zeros são omitidos. Isso significa que, se o número termina com um zero, o zero é perdido por inversão de marcha (por exemplo, 1200 dá 21). Observe também que o número invertido não tem quaisquer zeros finais.
#ACM precisa calcular com números invertidos. Sua tarefa é adicionar dois números invertidos e saída de sua soma invertida. Claro que, o resultado não é único porque qualquer número particular é uma forma invertida de vários números (por exemplo, 21 pode ser de 12, 120 ou 1200 antes de inverter). Assim, temos de assumir que não há zeros foram perdidos, invertendo (por exemplo, assumir que o número original era 12).

#Entrada
#A entrada consiste de N casos (o equivalente a cerca de 10 mil). A primeira linha da entrada contém inteiro único ponto positivo N. 
#Em seguida, siga os casos. Cada caso é composto por exatamente uma linha com dois números inteiros positivos separados por espaço. 
#Estes são os números invertidos que está a adicionar.

#Saída
#Para cada caso, imprima exatamente uma linha contendo apenas um inteiro - a soma de dois números invertidos invertidas. Omitir quaisquer zeros à esquerda na saída.

n = int(raw_input())
listaA = []
listaB = []

def converteParaLista(elemento, lista):
	for i in range(len(elemento)):
		lista.append(int(elemento[i]))

def reverterLista(lista):
	aux = []
	for i in range(len(lista)):
		aux.append(lista[len(lista)-1-i])
	return aux
	
def somarListas(lista1, lista2):
	soma = []
	if (len(lista1) != len(lista2)):
		if len(lista1) > len(lista2):
			for i in range(len(lista1)):
				if i < len(lista1)-1-i:
					soma.append(lista1[len(lista1)-1-i] + lista2[len(lista1)-1-i])
	return soma		

for i in range(n):
	a,b = raw_input().split()
	
	converteParaLista(a, listaA)
	converteParaLista(b, listaB)
	listaA = reverterLista(listaA)
	listaB = reverterLista(listaB)
	
	print listaA
	print listaB
	
	print somarListas(listaA, listaB)
	
