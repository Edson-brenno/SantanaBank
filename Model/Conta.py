class Conta():

    def __init__(self, numero, titular, saldo):
        
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
    
    def __str__(self):
        
        return f"Conta: {self.__numero}; Saldo: {self.__saldo}; Titular: {self.__titular}"