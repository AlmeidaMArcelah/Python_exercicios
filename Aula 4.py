a = int(input('Primeiro bimestres: '))
while a > 10:
    a = int(input('Você digitou errado. \nPrimeiro bimestre: '))
b = int(input('Segundo bimestres: '))
while b > 10:
    b = int(input('Você digitou errado. \nSegundo bimestre: '))
c = int(input('Terceito bimestres: '))
while c > 10:
    c = int(input('Você digitou errado. \nTerceiro bimestre: '))
d = int(input('Quarto bimestres: '))
while d > 10:
    d = int(input('Você digitou errado. \nQuarto bimestre: '))
media = (a + b + c + d) / 4
print(' Sua média é: {}'.format(media))

 # nota = int(input('Entre com a nota'))
 # while nota > 10:
 #     nota = int(input('Nota invalida. Entre com a nota correta: '))
 # print(nota)

# a = 0
# while a < 10:
#     print(a)
#     a += 1

# a = int(input('Entre com um velor: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         # print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)


# a = int(input('Entre com o número:' ))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
# if div == 2:
#     print('número {} é primo'.format(a))
# else:
#     print('número {} não é primo'.format(a))