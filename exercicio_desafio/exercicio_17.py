
# Sistema Bancário Simples


class ContaBancaria:
    """
    Representa uma conta bancária com saldo, número e titular.
    """

    def __init__(self, numero_conta, titular, saldo_inicial=0.0):
        # Atributos da conta
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        """Adiciona um valor ao saldo da conta."""
        if valor <= 0:
            print("Erro: O valor do depósito deve ser maior que zero.")
            return

        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        print(f"Novo saldo: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        """Remove um valor do saldo, se houver saldo suficiente."""
        if valor <= 0:
            print("Erro: O valor do saque deve ser maior que zero.")
            return

        if valor > self.saldo:
            print("Erro: Saldo insuficiente para realizar o saque.")
            print(f"Saldo atual: R$ {self.saldo:.2f}")
            return

        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        print(f"Novo saldo: R$ {self.saldo:.2f}")

    def verificar_saldo(self):
        """Exibe o saldo atual da conta."""
        print(f"Conta {self.numero_conta} | Titular: {self.titular}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def __str__(self):
        # Representação em texto da conta (útil para print())
        return f"Conta {self.numero_conta} - Titular: {self.titular} - Saldo: R$ {self.saldo:.2f}"


# ============================================================


class Cliente:
    """
    Representa um cliente do banco.
    Um cliente pode ter várias contas bancárias.
    """

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []  # Lista de contas do cliente

    def adicionar_conta(self, conta):
        """Vincula uma conta bancária a este cliente."""
        self.contas.append(conta)
        print(f"Conta {conta.numero_conta} adicionada ao cliente {self.nome}.")

    def listar_contas(self):
        """Mostra todas as contas deste cliente."""
        if not self.contas:
            print(f"O cliente {self.nome} não possui contas cadastradas.")
            return

        print(f"\nContas do cliente: {self.nome} (CPF: {self.cpf})")
        print("-" * 45)
        for conta in self.contas:
            print(conta)
        print("-" * 45)

    def __str__(self):
        return f"Cliente: {self.nome} | CPF: {self.cpf} | Contas: {len(self.contas)}"


# ============================================================


class Banco:
    """
    Representa o banco que gerencia todos os clientes.
    """

    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
        self.clientes = []           # Lista de clientes
        self._contador_contas = 1    # Contador para gerar números de conta únicos

    def _gerar_numero_conta(self):
        """Gera um número de conta único automaticamente."""
        numero = f"{self._contador_contas:04d}"  # Ex: 0001, 0002...
        self._contador_contas += 1
        return numero

    def adicionar_cliente(self, nome, cpf):
        """Cadastra um novo cliente no banco."""
        # Verifica se o CPF já existe
        cliente_existente = self.buscar_cliente_por_cpf(cpf)
        if cliente_existente:
            print(f"Erro: Já existe um cliente com o CPF {cpf}.")
            return None

        novo_cliente = Cliente(nome, cpf)
        self.clientes.append(novo_cliente)
        print(f"Cliente '{nome}' cadastrado com sucesso no {self.nome_banco}!")
        return novo_cliente

    def abrir_conta(self, cpf, saldo_inicial=0.0):
        """Abre uma nova conta para um cliente existente."""
        cliente = self.buscar_cliente_por_cpf(cpf)

        if not cliente:
            print(f"Erro: Nenhum cliente encontrado com o CPF {cpf}.")
            return None

        numero_conta = self._gerar_numero_conta()
        nova_conta = ContaBancaria(numero_conta, cliente.nome, saldo_inicial)
        cliente.adicionar_conta(nova_conta)
        return nova_conta

    def buscar_cliente_por_cpf(self, cpf):
        """Procura um cliente pelo CPF. Retorna o cliente ou None."""
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def buscar_conta_por_numero(self, numero_conta):
        """Procura uma conta pelo número dela em todos os clientes."""
        for cliente in self.clientes:
            for conta in cliente.contas:
                if conta.numero_conta == numero_conta:
                    return conta
        return None

    def listar_clientes(self):
        """Exibe todos os clientes cadastrados no banco."""
        if not self.clientes:
            print("Nenhum cliente cadastrado ainda.")
            return

        print(f"\n{'=' * 45}")
        print(f"  Clientes do {self.nome_banco}")
        print(f"{'=' * 45}")
        for cliente in self.clientes:
            print(cliente)
        print(f"{'=' * 45}\n")


# ============================================================
# Programa principal - demonstração do sistema
# ============================================================

if __name__ == "__main__":

    print("\n" + "=" * 45)
    print("   BEM-VINDO AO SISTEMA BANCÁRIO")
    print("=" * 45 + "\n")

    # Criando o banco
    banco = Banco("Banco Python S.A.")

    # Cadastrando clientes
    print(">>> Cadastrando clientes...\n")
    cliente1 = banco.adicionar_cliente("Ana Silva", "111.222.333-44")
    cliente2 = banco.adicionar_cliente("Carlos Souza", "555.666.777-88")

    # Tentando cadastrar um CPF duplicado
    banco.adicionar_cliente("Outro Nome", "111.222.333-44")

    # Abrindo contas para os clientes
    print("\n>>> Abrindo contas...\n")
    conta_ana1 = banco.abrir_conta("111.222.333-44", saldo_inicial=500.0)
    conta_ana2 = banco.abrir_conta("111.222.333-44")
    conta_carlos = banco.abrir_conta("555.666.777-88", saldo_inicial=1000.0)

    # Listando clientes
    banco.listar_clientes()

    # Operações na conta da Ana
    print("\n>>> Operações na conta da Ana...\n")
    conta_ana1.verificar_saldo()
    print()
    conta_ana1.depositar(250.0)
    print()
    conta_ana1.sacar(100.0)
    print()
    conta_ana1.sacar(1000.0)  # Deve dar erro de saldo insuficiente

    # Operações na conta do Carlos
    print("\n>>> Operações na conta do Carlos...\n")
    conta_carlos.verificar_saldo()
    print()
    conta_carlos.depositar(500.0)
    print()
    conta_carlos.sacar(200.0)

    # Listando contas dos clientes
    print()
    cliente1.listar_contas()
    cliente2.listar_contas()

    # Buscando conta por número
    print("\n>>> Buscando conta pelo número '0001'...\n")
    conta_encontrada = banco.buscar_conta_por_numero("0001")
    if conta_encontrada:
        print(f"Conta encontrada: {conta_encontrada}")
    else:
        print("Conta não encontrada.")