#1 
l = int(input())

termo1 = 1
termo2 = 1
termo = 0

if termo1 < l:
     print(termo1)

if termo2 < l:
     print(termo2)

while termo1 + termo2 <= l:
    termo = termo1 + termo2
    print(termo)
    termo1 = termo2
    termo2 = termo

#2
#)a
soma = 0 
multi = 1


n = int(input())
for i in range(n):
    num = int(input())
    soma = soma + num
    multi = multi * num
    menor = num
    maior = num
    if num < menor:
        menor = num
    if num > maior:
        maior = num


media = soma // n

print(f"Soma:{soma}")
print(f"Produto:{multi}")
print(f"Menor:{menor}")
print(f"Maior:{maior}")
print(f"Media:{media}")

#)b
num = int(input())
limite = num > 0 and num <= 10

if limite:
    print(num * 1)
    print(num * 2)
    print(num * 3)
    print(num * 4)
    print(num * 5)
    print(num * 6)
    print(num * 7)
    print(num * 8)
    print(num * 9)
    print(num * 10)

#)c
N = int(input("Digite um valor para N: "))

base = 1

for i in range(1, 51):
    
    if i % 2 != 0:
        resultado = base + N
        print(f"{i}º termo: {base} + {N} = {resultado}")
        
    else:
        resultado = base * N
        print(f"{i}º termo: {base} * {N} = {resultado}")

    base += 4
    
#)d
for i in range(100, 1000):
    i = str(i)
    a = (int(i[0])**3)
    b = (int(i[1])**3)
    c = (int(i[2])**3)
    soma = a + b + c

    if soma == int(i):
        print(i)

#)e
n = int(input())
k = 1 

triangular = False

while k * (k + 1) * (k + 2) <= n:
    if k * (k + 1) * (k + 2) == n:
        triangular = True
        break
    k += 1

if triangular:
    print(f"O {n} eh Triangular")
else:
    print(f"O {n} nao eh Triangular")

#)f
n = int(input())
encontrados = 0
num = 1

while encontrados < n:
    soma = 0
    for d in range(1, num):
        if num % d == 0:
            soma += d
    
    if soma == num:
        print(num)
        encontrados += 1
    
    num += 1

