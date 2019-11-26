import random
from random import randrange

# Exercício 01
"""
Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado dos componetes deste vetor,
armazenando os valores em outro vetor. Os conjuntos tem 10 elementos cada. Imprima os dois.
"""
vet = [1, 10, 20, 30, 40, 50, 100, 200, 300, 1000]
resultado = []

def quadrado(a):
    num = a ** 2
    return num


for n in vet:
    resultado.append(quadrado(n))

print(vet)
print(resultado)

# Exercício 02
"""
Leia um vetor de 10 posições e verifica quantos numeros pares ele possui.
"""
vet = [1, 25, 86, 12, 13, 8411, 3, 9, 111, 53741]
pares = []
impares = []


for n in vet:
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)


print(f'Possui {len(pares)} números pares e {len(impares)} números impares!')


# Exercício 03
"""
Receba do usuário um vetor de 5 posições, e imprima o maior número e o menor número deles.
"""

tela = True
vet = []


while tela == True:
    num = input("informe um número ou digite 'sair' para sair: ")
    if num == 'sair':
        print(f'O maior número é: {max(vet)}')
        print(f'O menor número é: {min(vet)}')
        tela = False
    else:
        vet.append(int(num))

# Exercício 04
"""
Faça um programa que tenha uma lista contendo números inteiros, e imprima o maior número e a posição que se encontra.
"""

vet = [1, 25, 86, 12, 13, 8411, 3, 9, 111, 3]
num = 0


for n in vet:
    if n == max(vet):
        break
    else:
        num = num + 1

print(f'O maior número é: {max(vet)}')
print(f'E está na posição: {num} do vetor.')

# Exercício 05

"""
Faça um programa que peça nomes de pessoas, armazene em uma lista e sorteie um dos nomes.
"""
tela = True
vet = []


while tela == True:
    nomes = str(input('Digite um nome ou digite "sair" para sair: '))
    if nomes == 'sair':
        tela = False
    else:
        vet.append(nomes)

sorteio = random.choice(vet)
print(f'A Pessoa sorteada foi: {sorteio}')

# Exercício 06
"""
Faça um programa que analise o nome completo de uma pessoa, informando a quantidade de letras,
a quantidade de letras do primeiro nome, informando o nome completo com letras maiúsculas e minúsculas.
"""

nome = input("Digite seu nome completo: ").strip()
print(f'Seu nome em letras maiúsculas é {nome.upper()}')
print(f'Seu nome em letras minúsculas é {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')

separador = nome.split()

print(f'Seu primeiro nome é {separador[0]} e contém {nome.find(" ")} letras.')


# Exercício 07
"""
Faça um analisador de dados coletando o nome, idade e sexo de quatro pessoas.
"""
print('---- 1° PESSOA ----')
nome1 = input('Nome: ').strip().lower()
idade1 = float(input('Idade: '))
sexo1 = input('Sexo[m/f]: ').strip().lower()

print('---- 2° PESSOA ----')
nome2 = input('Nome: ').strip().lower()
idade2 = float(input('Idade: '))
sexo2 = input('Sexo[m/f]: ').strip().lower()

print('---- 3° PESSOA ----')
nome3 = input('Nome: ').strip().lower()
idade3 = float(input('Idade: '))
sexo3 = input('Sexo[m/f]: ').strip().lower()

print('---- 4° PESSOA ----')
nome4 = input('Nome: ').strip().lower()
idade4 = float(input('Idade: '))
sexo4 = input('Sexo[m/f]: ').strip().lower()

media = (idade1 + idade2 + idade3 + idade4) / 4
lista = [idade1, idade2, idade3, idade4]
nome = ''
sexo_f = 0
sexo_m = 0


if max(lista) == idade1:
    nome = nome1

elif max(lista) == idade2:
    nome = nome2

elif max(lista) == idade3:
    nome = nome3

elif max(lista) == idade3:
    nome = nome3

if sexo1 == 'f':
    sexo_f = sexo_f + 1
if sexo1 == 'm':
    sexo_m = sexo_m + 1

if sexo2 == 'f':
    sexo_f = sexo_f + 1
if sexo2 == 'm':
    sexo_m = sexo_m + 1

if sexo3 == 'f':
    sexo_f = sexo_f + 1
if sexo3 == 'm':
    sexo_m = sexo_m + 1

if sexo4 == 'f':
    sexo_f = sexo_f + 1
if sexo4 == 'm':
    sexo_m = sexo_m + 1

print(f'A média de idade do grupo é de: {media} anos')
print(f'A pessoa mais velha do grupo é o(a) {nome} com {max(lista)} anos.')
print(f'Mulheres: {sexo_f}')
print(f'Homens: {sexo_m}')
sexo_outros = 4 - (sexo_f + sexo_m)
print(f'Outros: {sexo_outros}')

# Exercício 08
"""
Faça um jogo que o usuário tenta adivinhar o número de 0 à 10 que o computador escolheu.
"""
num = randrange(10)
tela = True
tentativas = 1

print('Tente adivinhar o número de 0 à 10 que o computador pensou!')

while tela == True:
    numero = int(input('Digite um número: '))
    if numero > num:
        print('MENOS...')
    if numero < num:
        print('MAIS...')
    if numero == num:
        print(f'Parabéns você ganhou na {tentativas}° tentativa e acertou o número que era {num}.')
        tela = False
    else:
        tentativas += 1
