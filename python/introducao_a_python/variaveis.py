'''
Arquivo: variaveis.py
Data: 2/07/2021
Descrição: Manipulando variáveis através de operadores aritmáticos e interação com usuário.
Autor: Marcos Santana
'''

# Variáveis

a = 10
b = 5

# Calculos aritméticos

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

# Imprimindo variáveis

print('Soma: %s' % (soma))
print('Subtração: %s' % (subtracao))
print('Multiplicação: %s' % (multiplicacao))
print('Divisão: %.0f' % (divisao))
print('Resto: %s' % (resto))

# Criando um interção com usuário

numero = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

soma = numero + numero2
subtracao = numero - numero2
multiplicacao = numero * numero2
divisao = numero / numero2
potencia = numero ** numero2
resto = numero % numero2

print(f'Soma: {soma},\n Subtração: {subtracao},\n Multiplicação: {multiplicacao},\n Divisão: {divisao},\n Potência:'
      f' {potencia},\n Resto: {resto}')
