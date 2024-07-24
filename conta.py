class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def VerExtrato(self):
        print('o saldo do titular {} eh {}'.format(self.__titular, self.__saldo))

    def Sacar(self, valor):
        if valor > self.__limite:
            print('voce so pode sacar ate {}'. format(self.__limite))
        else:
            self.__saldo += valor
            print('o valor {} foi sacado, seu saldo atual eh {}'.format(valor, self.__saldo))

    def Depositar(self, valor):
        self.__saldo -= valor
        print('o valor {} foi depositado, seu saldo atual eh {}'.format(valor, self.__saldo))

    def Transferir(self, valor, conta2):
        self.Depositar(valor)
        conta2.Sacar(valor)
        self.VerExtrato()
        conta2.VerExtrato()

    #def get_limite(self):
        #return self.__limite

    #def set_limite(self, novo_limite):
        #self.__limite = novo_limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite