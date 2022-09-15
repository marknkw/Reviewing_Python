#Posições começam com [índice em 0] e não em [1]
#Exercício 3.1
def tresPontoUm():
    amigos = ['Um', 'Dois', 'Três']
    return amigos
#Exercício 3.2
def tresPontoDois(name):
    return print("Olá " + name)
#Exercício 3.3
def tresPontoTres():
    transportes = ['moto', 'carro', 'bicicleta']
    return transportes
#Print dos exercícios
for i in range(0, len(tresPontoUm()), 1):
    tresPontoDois(tresPontoUm()[i])
    tresPontoDois(tresPontoTres()[i])
