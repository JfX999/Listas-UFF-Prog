#1 Calculadora
def interface_calculadora(n1, n2):
    resposta = (str(input("Qual Operação: |Soma| |Sub| |Multi| |Div|?").lower()))
    if resposta == "soma":

        def soma(n1, n2):
            return n1 + n2
        print(soma(n1, n2))

    elif resposta == "sub":

        def sub(n1, n2):
            return n1 - n2
        print(sub(n1, n2))
        
    elif resposta == "multi":

        def multi(n1 , n2):
            return n1 * n2
        print(multi(n1, n2))

    elif resposta == "div":

        def div(n1, n2):
            return n1 / n2
        print(div(n1,n2))

    else:
        print("Você não digitou nenhuma operação")

n1 = int(input("Primeiro Numero:"))
n2 = int(input("Segundo Numero:"))

interface_calculadora(n1, n2)

#2 Maior Lista Crescente
lista = [6, 11, 4, 3, 5, 8, 10, 9, 6]
contadores = []
counter = 1
for i in range(len(lista)-1):
    if lista[i] <= lista[i+1]:
        counter += 1
    if lista[i] > lista[i+1]:
        contadores.append(counter)
        counter = 1
rev = sorted(contadores, reverse=True)
print(rev[0])