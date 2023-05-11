class Gasto:
    def __init__(self, nome, valor, diaVencimento, pago):
        self.__nome = nome
        self.__valor = valor
        self.__diaVencimento = diaVencimento
        self.__pago = pago
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
        
    @property
    def diaVencimento(self):
        return self.__diaVencimento
    
    @diaVencimento.setter
    def diaVencimento(self, diaVencimento):
        self.__diaVencimento = diaVencimento
    
    @property
    def pago(self):
        return self.__pago
    
    @pago.setter
    def pago(self, pago):
        self.__pago = pago

g1 = Gasto('CB TWISTER 250', 651, '10/06/2023', 1)
print(g1)
print(g1.nome)
print(g1.valor)
print(g1.diaVencimento)
print(g1.pago)


