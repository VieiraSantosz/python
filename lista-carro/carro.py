# 3. Implementar uma classe chamada MinhaLista que herde da classe MutableSequence 
# do pacote collections.abc

# Em seguida, você pode adicionar métodos específicos na classe MinhaLista para manipular 
# a lista de forma personalizada.

# Lembre-se de implementar todos os métodos abstratos da classe MutableSequence na classe MinhaLista.

from collections.abc import MutableSequence


class MinhaLista(MutableSequence):
    
    def __init__(self):
        self._carro = []
        
    def __str__(self):
        return f'{self._carro}'
    
    def __getitem__(self, index):
        return self._carro[index]
    
    def __setitem__(self, index, item):
        self._carro[index] = item
    
    def __delitem__(self, index):
        del self._carro[index]
    
    def __len__(self):
        return len(self._carro)
    
    def insert(self, index, item):
        self._carro.insert(index, item)
        
    @property
    def listar_carros(self):
        cont = 1
        
        for carro in self._carro:
            print(f'Carro {cont}: {carro}')
            cont += 1