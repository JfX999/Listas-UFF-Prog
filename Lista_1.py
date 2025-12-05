#Area do Cubo - 1

aresta = float(input("Digite o valor da aresta do cubo: "))
face = aresta * aresta
area_do_cubo = face * 6

print(area_do_cubo)

#Escreva um programa que recebe três inteiros como entrada do teclado e escreva na
#tela a média, a soma, o produto, o menor valor e o maior valor, usando uma linha para
#cada resultado.

a = int(input())
b = int(input())
c = int(input())

if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c

if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
    maior = c

soma = a + b + c
media = a + b + c // 3
produto = a * b * c
menorvalor = menor
maiorvalor = maior

print(f"Soma: {soma}")
print(f"Media: {media}")
print(f"Produto: {produto}")
print(f"Menor Valor {menorvalor}")
print(f"Maior Valor {maiorvalor}")

# Em uma loja e CD ́s existem apenas quatro tipos de preços que estão associados a
# cores. Assim os CD ́s que ficam na loja não são marcados por preços e sim por cores.
# Desenvolva o algoritmo que a partir a entrada da cor o software mostre o preço. A loja
# está atualmente com a seguinte tabela de preços.

cor = str(input("Digite a Cor do CD:"))

if cor == "Verde":
    print("R$ 10.00")
elif cor == "Azul":
    print("R$ 20.00")
elif cor == "Amarelo":
    print("R$ 30.00")
elif cor == "Vermelho":
    print("R$ 40.00")

# Escreva um programa que recebe três números e retorna a soma deles, porém se
# houver números repetidos o valor deles não é contabilizado. Por exemplo, na entrada
# (1,2,3) a resposta é 6, na entrada (3,2,3) a resposta é 2 e na entrada (3,3,3) a resposta
# é 0.    

a = int(input())
b = int(input())
c = int(input())

soma = 0

if a != b and a != c:
    soma = soma + a

if b != a and b != c:
    soma = soma + b

if c != a and c != b:
    soma = soma + c

print(soma)

# Escreva um programa que receba três números. O programa deve imprimir a palavra
# “soma” se a soma de dois deles for igual ao outro número, caso contrário, o programa
# deve imprimir a palavra “multi” se a multiplicação de dois deles for igual ao outro
# número. Caso nenhuma das duas possibilidades for verdade, então imprimir a palavra
# “par” se a soma dos três números for par, e imprimir a palavra “impar” caso contrário.
# Por exemplo, na entrada (8,3,5) a resposta é “soma”, na entrada (3,3,1) a resposta é
# “multi”, na entrada (8,4,9) a resposta é “impar”.

a = int(input())
b = int(input())
c = int(input())

aux = a + b + c

if a + b == c or a + c == b or b + c == a:
    print("Soma")

elif a * b == c or a * c == b or b * c == a:
    print("Multi")

elif aux % 2 == 0:
    print("Par")

else:
    print("Impar")

# indique se formam um
# triângulo, juntamente com o seu tipo (equilátero, isósceles e escaleno):

# i. Equilátero: todos os lados iguais
# ii. Isósceles: dois lados iguais
# iii. Escaleno: todos os lados diferentes

a = int(input("Num1:"))
b = int(input("Num2:"))
c = int(input("Num3:"))

cond_exist = a + b > c and b + c > a and a + c > b

if cond_exist == False:
    print("Sem Triangulo")

else:

    if a != b and a != c and b != c:
        print("Triangulo Escaleno")

    elif a == b and a == c:
        print("Triangulo Equilátero")

    else:
        print("Triangulo Isósceles")

# Faça um programa que a partir de um número informado em centavos (inteiro), indique
# a menor quantidade de moedas que representa esse valor. Considere moedas de 1,25
# e 50 centavos e 1 real (100 centavos). Exemplo: 290 centavos é representado por 2
# moedas de 1 real, 1 de 50c, 1 de 25c, 15 de 1c.
# Dica) Podemos usar as operações de divisão inteira (//) e resto da divisão (%) para
# saber quantas moedas de um tipo podem ser usadas no troco.
# Ex: Para um valor de 142 centavos e a moeda de 25 centavos, temos que 142//25=5,
# logo podemos dar 5 moedas de 25 centavos no troco. Além disso, veja que
# 142%25=17, logo depois de dar o troco de 5 moedas de 25 centavos, ainda restaria 17
# centavos para dar de troco em moedas de valor menor.

valor_total = int(input("Digite o valor em centavos: "))

moedas_100 = valor_total // 100
resto = valor_total % 100

moedas_50 = resto // 50
resto = resto % 50

moedas_25 = resto // 25
resto = resto % 25

moedas_1 = resto


print("--- Resultado ---")
print(f"Moedas de 1 real: {moedas_100}")
print(f"Moedas de 50 centavos: {moedas_50}")
print(f"Moedas de 25 centavos: {moedas_25}")
print(f"Moedas de 1 centavo: {moedas_1}")
