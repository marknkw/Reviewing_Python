"""O método .sort() oferece uma forma de alterar a ordem de uma lista e armazenar os itens, nessa mesma lista,
em ordem alfabética
Ex:"""

list = ['b', 't', 'k', 'l']
list.sort()
print(list)
"""output: ['b', 'k', 'l', 't']"""

"""Também é possível adicionar argumentos ao método .sort(), como o o argumento "reverse=True"
No qual a lista será ordenada de forma inversa
Ex:"""

list = ['b', 't', 'k', 'l']
list.sort(reverse=True)
print(list)

"""output: ['t', 'l', 'k', 'b']"""

"""A função sorted() permite exibir uma lista sem afetar a ordem permanente da variável de lista na memória
Ou seja, os itens são organizados sem alterar, permanentemente, a lista exibida.
O argumento "reverse = True" também é aceito"""
"""O método .reverse() inverte a ordem original de uma lista."""
"""Ex: """

list = ['b', 't', 'k', 'l']
list.reverse()
print(list)
"""output: ['l', 'k', 't', 'b']"""

"""A função len(lista_qualquer) retorna o tamanho do tamanho de uma lista
Ex:"""

list = ['b', 't', 'k', 'l']
print(len(list))
"""output: 4"""

"""3.8"""
lista = ['Paris', 'Nova York', 'Wyoming', 'Seoul', 'Tokyo']
print(lista, '\n')
print(sorted(lista))
print(lista, '\n')
print(sorted(lista, reverse=True))
print(lista, '\n')
lista.reverse()
print(lista)
lista.reverse()
print(lista)
"""Nota-se que o método .reverse() somente inverte a ordem da lista"""
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
"""Nota-se que o método .sort() ordena permanentemente, em ordem alfabética, a lista. Caso queira preservar a lista
 original, é necessário atribuir o valor de uma lista a uma variável cópia"""
