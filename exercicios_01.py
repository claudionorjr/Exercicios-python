import math


# Exercícios 1
"""
faça um programa que receba dois numeros e diga qual é o maior:
"""
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
soma = num1 + num2

print(f'A soma é de: {soma}')

# Exercícios 2
"""
leia um numero fornecido pelo usuario. Se esse numero por positivo, calcule a raiz quadrada do numero. Se o numero
for negativo informe que o numero é invalido.
"""

num1 = int(input('Digite um numero: '))

if num1 > 0:
    print(math.sqrt(num1))
elif num1 <= 0:
    print("numero invalido!")

# Exercicio 3
"""
Leia um numero e, caso ele seja positivo, calcule e mostre:
O numero ao quadrado
a raiz quadrada do numero
"""

tela = True

while tela == True:
    num1 = int(input('Digite um numero: '))

    if num1 > 0:
        quadrado = num1 * num1
        raiz = math.sqrt(num1)
        print(f'O numero digitado ao quadrado é: {quadrado}')
        print(f'A raiz do numero digitado é: {raiz}')
        tela = False
    elif num1 <= 0:
        print("numero invalido!")
        Tela = True

# exercício 4
"""
Faça um programa que informe para o usuario se o numero é par ou impar!
"""

num = int(input("Imforme um numero: "))
resultado = num % 2

if resultado == 0:
    print("Este numero é par!")
elif resultado == 1:
    print("Este numero é impar!")

# Exercicio 5
"""
Faça um programa que receba 2 numeros e informe qual é o maior!
"""

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o primeiro numero: "))

if num1 > num2:
    print(f'O primeiro numero é maior que o segundo: {num1}')
elif num2 > num1:
    print(f'O segundo numero é maior que o primeiro: {num2}')
else:
    print('Os numeros são iguais!')
    
# exercício 6
"""
Faça um programa que receba 2 numeros e informe qual é o maior entre eles, assim como a diferença nos valores!
"""

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o primeiro numero: "))

if num1 > num2:
    dif = num1 - num2
    print(f'O primeiro numero é maior que o segundo: {num1}')
    print(f'A diferença entre os numeros foram de: {dif}')
elif num2 > num1:
    dif = num2 - num1
    print(f'O segundo numero é maior que o primeiro: {num2}')
    print(f'A diferença entre os numeros foram de: {dif}')
else:
    print('Os numeros são iguais!')

# Exercicio 7
"""
leia o salario de um trabalhador e o valor da parcela de um empréstimo. Se a parcela for maior que 20% do salario
imprima: "empréstimo recusado" se não "empréstimo aprovado".
"""

salario = float(input("Digite o Salário: "))
parcela = float(input("Digite a parcela: "))

valor = salario * 0.20

if valor > parcela:
    print('Empréstimo aceito!')
else:
    print('Empréstimo rescusado!')


# exercício 8
"""
leia um numero. Se esse numero por positivo, calcule o logaritimo, caso for negativo informe que o numero é invalido.
"""

tela = True

while tela == True:
    num1 = int(input('Digite um numero: '))
    log = int(input('Digite o log de "x": '))

    if num1 > 0:
        logaritimo = math.log(num1, log)
        print(f'O o logaritimo é: {logaritimo}')
        tela = False
    elif num1 <= 0:
        print("numero invalido!")
        Tela = True

# Exercício 9
"""
Faça um programa que calcule a media ponderada de um aluno, pedindo a nota e o peso da nota e diga se o aluno
foi aprovado, reprovado ou em recuperação.
"""


def media_ponderada(x1, x2, x3, p1, p2, p3):
    mp1 = (x1 * p1) + (x2 * p2) + (x3 * p3)
    mp2 = p1 + p2 + p3
    resultado = mp1 / mp2
    return resultado


nota1, peso1 = float(input("Digite a primeira nota: ")), int(input("Digite o peso(nota1): "))
nota2, peso2 = float(input("Digite a segunda nota: ")), int(input("Digite o peso(nota2): "))
nota3, peso3 = float(input("Digite a terceira nota: ")), int(input("Digite o peso(nota3): "))

media = media_ponderada(nota1, nota2, nota3, peso1, peso2, peso3)

if media >= 6:
    print('Aluno(a), foi aprovado(a)!')
elif media >= 5 and media < 6:
    print('Aluno(a), está em recuperação!')
else:
    print('Aluno(a), está reprovado(a)!')
# exercicio 10
"""
Usando switch, escreva programa que leia inteiro entre 1 e 7, correspondendo a os dias da semana,
sendo que 1 é domingo.
"""

tela = False

while tela == False:
    data = int(input("Digite um numero entre 1 e 7, sendo 1(domingo), ou 'sair' para sair: "))
    if data == 'sair':
        tela = True
    elif data == 1:
        print('O número "1" corresponde ao domingo')
        tela = False
    elif data == 2:
        print('O número "2" corresponde ao segunda-feira')
        tela = False
    elif data == 3:
        print('O número "3" corresponde ao terça-feira')
        tela = False
    elif data == 4:
        print('O número "4" corresponde ao Quarta-feira')
        tela = False
    elif data == 5:
        print('O número "5" corresponde ao quinta-feira')
        tela = False
    elif data == 6:
        print('O número "6" corresponde ao sexta-feira')
        tela = False
    elif data == 7:
        print('O número "7" corresponde ao sabado')
        tela = False
    else:
        print('Número digitado é inválido!')
        tela = False

# Exercício 11
"""
Faça um programa que calcule a área de um trapézio.
"""


def trapezio(bmaior, bmenor, h):
    a = ((bmaior + bmenor) * h) / 2
    return a


base_maior = float(input('Digite o valor da (base maior(B)): '))
base_menor = float(input('Digite o valor da (base menor(b)): '))
altura = float(input('Digite o valor da (altura(h)): '))

area = trapezio(base_maior, base_menor, altura)
print(f'A área de seu trapézio é de: {area}')

# Exercício 12
"""
Faça um programa que tenha um menu de 4 opções de operações matemáticas(básicas), o usuário escolhe uma delas
e seu programa pede 2 valores numéricos e realiza a operação, mostrando o resultado e saindo.
"""


def multiplicacao(x, y):
    m = x * y
    return m


def divisao(x, y):
    d = x / y
    return d


def subtracao(x, y):
    s = x - y
    return s


def adicao(x, y):
    a = x + y
    return a


opcao = input('Digite a operação desejada,(adição), (subtração), (divisão), (multiplicação): ')

if opcao == 'adição':
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    soma = adicao(num1, num2)
    print(f'O resultado de sua {opcao} é {soma}')
elif opcao == 'subtração':
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    sub = subtracao(num1, num2)
    print(f'O resultado de sua {opcao} é {sub}')
elif opcao == 'divisão':
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    div = divisao(num1, num2)
    print(f'O resultado de sua {opcao} é {div}')
elif opcao == 'multiplicação':
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    mult = multiplicacao(num1, num2)
    print(f'O resultado de sua {opcao} é {mult}')


# Exercício 13
"""
Faça um programa para verificar se um determinado numero inteiro é divisível por 3 ou 5,
ou simultaneamente pelos dois
"""

num = int(input('Informe um numero inteiro: '))

if num % 3 == 0 and num % 5 == 0:
    print('Este número é divisivel por 3 e 5!')
elif num % 3 == 0:
    print('Este número é divisivel por 3!')
elif num % 5 == 0:
    print('Este número é divisivel por 5!')
else:
    print('Este número não é divisivel por 3 e nem 5!')
