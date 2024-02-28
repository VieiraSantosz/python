# 2. Implementar uma classe chamada "Pilha" que utilize uma lista internamente para armazenar os elementos. 

# A classe deve ter os seguintes métodos mágicos implementados: 
# init()
# str() 
# len()
# getitem()

# Além disso, você pode adicionar outros métodos que achar necessário, como push() para adicionar elementos à pilha e pop() 
# para remover elementos da pilha. Lembre-se de utilizar o conceito de duck typing para que a classe se comporte como uma pilha.

# Alguns atributos que você pode adicionar à classe "Pilha" são:

# _elementos: uma lista que armazena os elementos da pilha.
# _tamanho: um inteiro que guarda o tamanho atual da pilha.
# _capacidade: um inteiro que define a capacidade máxima da pilha (opcional).
# _topo: um inteiro que indica a posição do topo da pilha.


class Pilha():
    
    def __init__(self, capacidade):
        self._capacidade = capacidade
        self._elementos  = []
        self._tamanho    = 0
        self._topo       = 0
        
    def __str__(self):
        if (self._elementos == []):
            return 'Pilha Vazia'
        
        else:
            return f'Pilha: {self._elementos}'
        
    def __getitem__(self, item):
        return self._elementos[::-1][item]
    
    def __len__(self):
        self._tamanho = len(self._elementos)
        return self._tamanho
    
    def push(self, item):
        if (self.tamanho_pilha == self._capacidade):
            print('A pilha está cheia!')
        
        else:
            self._elementos.append(item)
            print(f'Elemento adicionado: {item}')
        
    def pop(self):
        if (len(self._elementos) > 0):
            print(f'Elemento removido: {self.elemento_topo}')
            self._elementos.pop()
        
        else:
            print("A pilha está vazia!")
        
    @property
    def tamanho_pilha(self):
        self._tamanho = len(self._elementos)
        return f'{self._tamanho}'
    
    @property
    def elemento_topo(self):
        self._topo = self._elementos[len(self._elementos) - 1]
        return f'{self._topo}'