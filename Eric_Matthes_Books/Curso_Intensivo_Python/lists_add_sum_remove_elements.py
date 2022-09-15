#Adicionando elementos a uma lista - método append
#lista".append('elemento')"

#Adicionando elementos ao início da lista - método insert
#lista".insert('elemento')" - insert() aloca espaço para o elemento no índice pretendido seguido do valor pretendido 'insert(índice, 'elemento')', movendo cada um dos valores da lista
#para uma posição posterior ao do elemento inserido

#Removendo elementos de uma lista - instrução del
#del lista[índice] - del pode ser usado quando o índice do índice que se quer remover da lista é conhecido

#Removendo elementos de uma lista - método pop()
#lista.pop() - remove o último elemento da pilha da lista['1','2','3'] -> lista.pop() -> lista['1','2'] e o retorna como valor
#É possível armazenar o valor do retorno em uma variável para uso posterior
#Ex: lista['1','2','3'] -> popped_lista = lista.pop() -> popped_lista == 3

#O método pop pode definir, também, o índice do elemento a ser removido de uma lista
#lista['1','2','3'] -> lista.pop(1) -> lista['1','3']

#Removendo elementos de uma lista - método remove()
#É possível remover o elemento de uma lista sem saber o índice no qual o elemento se encontra. Se você souber qual elemento deve ser removido
#O método lista."remove('elemento')" remove o elemento desejado da lista
#Ex: lista['1','2','3'] -> lista.remove('3') -> lista['1','2']
#O método remove() apaga somente a primeira ocorrência do valor especificado. Será necessário um laço para remover todos os outros valores repetidos
#na lista

#Exercício 3.4
def tresPontoQuatro():
    convidados = ['Feynman', 'Carl Sagan', 'God']
    return convidados

convidados = tresPontoQuatro()
for i in convidados:
    print(i + " você foi convidado para jantar.")

#Exercício 3.5
def tresPontoCinco(lista):

    print(lista[0] + " não poderá comparecer")
    lista.remove('Feynman')
    lista.insert(0, 'Christopher Nolan')
    return lista

convidados = tresPontoCinco(convidados)
for i in convidados:
    print(i + " você foi convidado para jantar.")
