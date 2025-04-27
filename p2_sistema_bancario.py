def menu():
    menu = """

    [d] depositar
    [s] sacar
    [e] extrato
    [n] nova conta
    [u] novo usuário
    [l] mostrar contas
    [q] sair

    => """
    return input(menu)

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f} \n"
        print("Depósito realizado com sucesso.")
    else:
        print("Depósito não realizado: valor inválido. Tente novamente")
    return saldo, extrato

def saque(*, saldo, valor, extrato, LIMITE, num_saques, LIMITE_SAQUES):
    if valor > saldo:
        print("Saque não realizado: saldo insuficiente para o saque")
    else:
        if valor > 0:
            if valor > LIMITE:
                print("O valor máximo por saque é de R$500,00. Tente novamente")
            else:
                num_saques += 1
                if num_saques > LIMITE_SAQUES:
                    print("Saque não realizado: limite de saques diários atingidos")
                else:
                    saldo -= valor
                    extrato += f"Saque de R$ {valor:.2f} \n"
                    print("Saque realizado com sucesso.")
        else:
            print("Saque não realizado: valor inválido. Tente novamente")
    return saldo, extrato, num_saques

def exibir_extrato(saldo, /, *, extrato):
    if not extrato:
        print("Não foram feitas transações até o momento.")
    else:
        print("----------Extrato----------")
        print(extrato)
        print("---------------------------")
    print(f"Saldo atual: R$ {saldo:.2f} \n")

def criar_usuario(usuarios):
    cpf = input("CPF (somente nº): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado, tente novamente.")
        return
    else:
        nome = input("Nome: ")
        nascimento = input("Data de nascimento (dd-mm-aa): ")
        endereco = input("Endereço (logradouro, nº - bairro - cidade/sigla/estado): ")

        usuario = {
            "nome": nome,
            "nascimento": nascimento,
            "cpf": cpf,
            "endereco": endereco
        }
        usuarios.append(usuario)
        print(f"Usuário {nome} criado.")

def filtrar_usuario(cpf, usuarios):
    fil_usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    if fil_usuario:
        return fil_usuario[0]
    else:
        return None

def criar_conta(agencia, num_conta, usuarios):
    cpf = input("CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso.")
        return {
            "agencia": agencia,
            "num_conta": num_conta,
            "usuario": usuario
        }
    else:
        print("Usuário não encontrado, não foi possível criar sua conta.")
        return None        

def mostrar_contas(contas):
    if contas:
        for conta in contas:
            print(f"Agência: {conta['agencia']} | Conta: {conta['num_conta']} | Usuário: {conta['usuario']['nome']} | CPF: {conta['usuario']['cpf']}")
    else:
        print("Nenhuma conta cadastrada.")    

def main():
    N_AGENCIA = "0001"
    LIMITE_SAQUES = 3
    LIMITE = 500
    saldo = 0
    extrato = " "
    num_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("valor para depositar => R$"))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("valor para sacar => R$"))
            saldo, extrato, num_saques = saque(saldo = saldo, valor = valor, extrato = extrato, LIMITE = LIMITE, num_saques = num_saques, LIMITE_SAQUES = LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "n":
            num_conta = len(contas) + 1
            conta = criar_conta(N_AGENCIA, num_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            mostrar_contas(contas)

        elif opcao == "q":
            break
        else:
            print("opção inválida, selecione novamente")

main()

