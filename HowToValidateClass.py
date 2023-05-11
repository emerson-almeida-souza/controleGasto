class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        if not isinstance(titular, str):
            raise TypeError("O titular da conta deve ser uma string")
        
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial deve ser um valor positivo")
        
        self.titular = titular
        self.saldo = saldo_inicial
    
    def validar_saque(self, valor):
        if valor < 0:
            raise ValueError("O valor de saque deve ser um valor positivo")
        
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para saque")
    
    def sacar(self, valor):
        self.validar_saque(valor)
        self.saldo -= valor
