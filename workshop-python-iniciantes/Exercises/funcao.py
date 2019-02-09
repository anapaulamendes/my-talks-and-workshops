lista_num = []

for i in range(10):
    num = int(input("Digite o número para adicionar na lista:"))
    lista_num.append(num)

def sumAll(lista):
    soma = 0
    for i in lista:
        soma += i
    print(soma)

sumAll(lista_num)
