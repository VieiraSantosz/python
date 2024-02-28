from datetime import datetime

class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        self._numero  = numero
        self._titular = titular
        self._saldo   = saldo
        self._limite  = limite
        
    def extrato(self):
        data_e_horas_atual = datetime.now()
        data_e_horas_atual_formatada = data_e_horas_atual.strftime('%d/%m/%Y - %H:%M')
        
        print(f'Saldo da Conta do {self._titular}: {self._saldo} | {data_e_horas_atual_formatada}')
        
    def depositar(self, valor):
        self._saldo += valor
        
    def sacar(self, valor):
        if (self._pode_sacar(valor)):
            self._saldo -= valor
            print(f'Saque realizado! Limite ainda disponível: {self._saldo + self._limite }')
        
        else:
            print(f'O valor {valor} ultrapassa seu limite de {self._saldo + self._limite}')
        
        
    def _pode_sacar(self, valor_do_saque):
        return valor_do_saque <= self._saldo + self._limite
        
    def transferir(self, conta_destino, valor):
        self.sacar(valor)
        conta_destino.depositar(valor)
        
    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, titular):
        self._titular = titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo
    
    @property
    def limite(self):
        return self._limite
        
    @limite.setter
    def limite(self, limite):
        self._limite = limite
        
    @staticmethod
    def codigo_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}