# atributos publicos e privados

class ContaBancaria:
    def __init__(self, titular, agencia, conta, saldo=0):
        self.titular = titular
        self.agencia = agencia
        self.conta = conta
        self.__saldo = saldo  # atributo privado da classe

    def ver_saldo(self):
        print(f'saldo da conta: {self.__saldo}')

    def depositar(self, valor):
        if valor > 0:
            print(f'depositando {valor}')
            self.__saldo += valor
        else:
            print('valor de deposito deve ser maior que 0')


conta1 = ContaBancaria('marcos', '000', '000-1', saldo=200)
conta2 = ContaBancaria('ze', '000', '000-2', 40000)

conta1.ver_saldo()
conta1.depositar(100)
conta1.ver_saldo()
conta1.depositar(-100)  # erro
