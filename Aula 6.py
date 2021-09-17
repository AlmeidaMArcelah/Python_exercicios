conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8, 9}

conjunto_uniao = conjunto.union(conjunto2)
print('Uniao: {}'.format(conjunto_uniao))

conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))

conjunto_diferenca1 = conjunto.difference(conjunto2)
print('Diferença 1: {}'.format(conjunto_diferenca1))

conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença 2: {}'.format(conjunto_diferenca2))

con_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Dieferença simétrica: {}'.format(con_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}'.format(conjunto_superset))

lista = ['cachorro', 'gato', 'gato', 'cachorro', 'elefante', 'macaco']
print(lista)
conjunto_animal = set(lista)
print(conjunto_animal)
lista_animais = list(conjunto_animal)
print(lista_animais)
# conjunto = {1, 3, 4, 4, 2}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)