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