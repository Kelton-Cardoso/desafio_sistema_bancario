class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.limite_diario = 500
        self.num_saques = 0
        self.limite_saques = 3
        self.extrato = []

    def depositar(self, valor):
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        else:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif valor > self.saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > self.limite_diario:
            print("Operação falhou! O valor do saque excede o limite diário.")
        elif self.num_saques >= self.limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.num_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def visualizar_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("==========================================")


conta = ContaBancaria()

while True:
    opcao = input("""
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        conta.depositar(valor)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        conta.sacar(valor)

    elif opcao == "e":
        conta.visualizar_extrato()

    elif opcao == "q":
        print("Saindo do sistema bancário. Obrigado!")
        break

    else:
        print("Opção inválida. Por favor, selecione novamente.")
