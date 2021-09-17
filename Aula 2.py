a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subitracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('soma: {soma}. \nsubtração: {subitracao}. '
      '\nmultiplicação: {multiplicacao}. '
      '\ndivisão: {divisao}. '
      '\nresto: {resto}'.format(soma=soma,
                                subitracao=subitracao,
                                multiplicacao=multiplicacao,
                                divisao=divisao,
                                resto=resto))
print(resultado)