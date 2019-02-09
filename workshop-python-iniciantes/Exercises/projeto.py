lista_contas = []

def cadastrar(lista_contas):
    conta = {}
    num_conta = input("Digite a conta: ")
    senha = input("Digite a senha: ")
    saldo = float(input("Digite o saldo: "))
    conta["conta"] = num_conta
    conta["senha"] = senha
    conta["saldo"] = saldo
    lista_contas.append(conta)
    print(conta)
    return lista_contas

def sacar(lista_contas):
    num_conta = input("Digite o numero da conta que deseja sacar: ")
    senha = input("Digite a senha da conta que deseja sacar: ")
    for conta in lista_contas:
        if conta["conta"] == num_conta and conta["senha"] == senha:
            saque = float(input("Digite a quantia que deseja sacar: "))
            if (conta["saldo"] - saque) >= 0:
                conta["saldo"] -= saque
                print("Saque realizado com sucesso! Novo saldo: " + str(conta["saldo"]))
            else:
                print("Saldo insuficiente!")

def depositar(lista_contas):
    num_conta = input("Digite o numero da conta que deseja depositar: ")
    for conta in lista_contas:
        if conta["conta"] == num_conta:
            deposito = float(input("Digite a quantia que deseja depositar: "))
            conta["saldo"] += deposito
            print("Depósito realizado com sucesso! Novo saldo: " + str(conta["saldo"]))

def transferir(lista_contas):
    num_conta = input("Digite o numero da sua conta: ")
    senha = input("Digite a senha da sua conta: ")
    for conta in lista_contas:
        if conta["conta"] == num_conta and conta["senha"] == senha:
            saque = float(input("Digite a quantia que deseja transferir: "))
            conta_trans = input("Digite o número da conta que deseja transferir dinheiro: ")
            for conta2 in lista_contas:
                if conta2["conta"] == conta_trans:
                    if (conta["saldo"] - saque) >= 0:
                        conta["saldo"] -= saque
                        print(conta2)
                        conta2["saldo"] += saque
                        print("Transferência realizada com sucesso! Novo saldo: " + str(conta["saldo"]) + ". Transferido: " + str(saque))
                    else:
                        print("Saldo insuficiente!")
                    
def imprimir(lista_contas):
    num_conta = input("Digite o numero da sua conta: ")
    senha = input("Digite a senha da sua conta: ")
    for conta in lista_contas:
        if conta["conta"] == num_conta and conta["senha"] == senha:
            print("Conta: " + str(conta["conta"]) + " Saldo: " + str(conta["saldo"]))

def menu():
    while(True):
        print("------ MENU ------")
        print("1 - Cadastrar")
        print("2 - Sacar")
        print("3 - Depositar")
        print("4 - Transferir")
        print("5 - Imprimir")
        print("0 - Sair")
        print("-------------------")
        opcao = int(input("Digite a operação que você deseja executar: "))
        if opcao == 1:
            cadastrar(lista_contas)
        elif opcao == 2:
            sacar(lista_contas)
        elif opcao == 3:
            depositar(lista_contas)
        elif opcao == 4:
            transferir(lista_contas)
        elif opcao == 5:
            imprimir(lista_contas)
        else:
            break

menu()
