lista = [10, 7, 3, 5, 1]
# print(lista)
# print(sum(lista))
# print(max(lista))
# print(min(lista))
lista.sort()
lista_animal = ['dog','wolf', 'cat', 'monkley', 'snake', 'bird']

lista_animal [0]= 'elefant'
print(lista_animal)
print(len(lista_animal))

# print(lista_animal[1])
# print(max(lista_animal))
# print(min(lista_animal))

# nova_lista = lista_animal * 3
# print(nova_lista)

# if 'Wolf' in lista_animal:
#     print('exists one wolf in the list')
# else:
#     print('Don´t exits wolf in the list. Will be included ')
#     lista_animal.append('wolf')
#     print(lista_animal)

# lista_animal.pop(0)
# print(lista_animal)

# lista_animal.remove('monkley')
# print(lista_animal)

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

tupla = (1, 10, 12, 3)
print(len(tupla))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)
