# 1. implementar uma classe chamada Playlist que seja iterável e permita adicionar programas de TV. A classe deve ter os seguintes métodos:

# __init__(self): inicializa a playlist vazia.
# adicionar_programa(self, programa): adiciona um programa à playlist.
# __getitem__(self, item): permite acessar um programa específico pelo seu índice.
# __len__(self): retorna o tamanho da playlist.
# __contains__(self, programa): verifica se um programa está contido na playlist.

# Você pode testar sua implementação criando uma instância da classe Playlist, adicionando programas e realizando operações como iterar sobre a playlist, 
# verificar se um programa está contido nela e acessar programas específicos pelo índice.

class Playlist():
    
    def __init__(self):
        self._programa_de_tv = []
        
    def adicionar_programa(self, programa):
        self._programa_de_tv.append(programa)
        
    def __getitem__(self, item):
        return self._programa_de_tv[item]
    
    def __len__(self):
        return len(self._programa_de_tv)
    
    def __contains__(self, programa):
        return programa in self._programa_de_tv