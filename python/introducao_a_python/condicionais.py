'''
Arquivo: condicionais.py
Data: 27/07/2021
Descrição: Introdução a condicionais e operadores lógicos com python.
Autor: Marcos Santana
'''

# Criando variáveis

# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor:'))
# c = int(input('Terceiro valor:'))

# Crindo uma condição utilizando operadores lógicos

## Exmplo 1

# if a > b and a > c:
#     print('O maior número é {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é {}'.format(b))

# print('Fim do programa')

## Exemplo 2 - Se o valor for par então faça isso!!

# valor = int(input('Digite uma Valor: '))
# modulo = valor % 2
#
# if modulo == 0:
#     print('Número é Par')
# else:
#     print('Número é Impar')

## Exemplo 3

# valor1 = int(input('Digite um valor: '))
# valor2 = int(input('Digite outro valor: '))
#
# a = valor1 % 2
# b = valor2 % 2
#
# if a == 0 or b == 0:
#     print('Foi digitado um número Par')
# else:
#     print('Nenhum número Par foi digitado!')
#
# print("Fim!")

## Exemplo 4 - Calculando médias de notas e validando

# Variáves que receberam a notas

n1 = int(input('Primeira Nota: '))
if n1 < 0:
    n1 = int((input('ERROR: Digite uma nota válida: ')))
n2 = int(input('Segunda Nota: '))
if n2 < 0:
    n2 = int((input('ERROR: Digite uma nota válida: ')))
n3 = int(input('Terceira Nota: '))
if n3 < 0:
    n3 = int((input('ERROR: Digite uma nota válida: ')))
n4 = int(input('Quarta Nota: '))
if n4 < 0:
    n4 = int((input('ERROR: Digite uma nota válida: ')))

# Calculando média

media = (n1 + n2 + n3 + n4) / 4

# Validando notas: notas > 0 e notas < 10

if n1 <= 10 and n2 <= 10 and n3 <= 10 and n4 <= 10:
    print('A média final é {}'.format(media))
else:
    print('Erro: Valor da nota inválido')



