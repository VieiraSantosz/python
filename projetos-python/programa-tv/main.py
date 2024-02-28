from programas import Playlist


promagras = Playlist()

promagras.adicionar_programa('Big Brother Brasil')
promagras.adicionar_programa('Jornal Nacional')
promagras.adicionar_programa('Globo Esporte')
promagras.adicionar_programa('De Placa')
promagras.adicionar_programa('Tnt Sports')


def main():
    print(f'\nQuantidades de Programas: {len(promagras)}\n')
    print(f'Sessão da Tarde está na Lista: {"Sessão da Tarde" in promagras}\n')
    
    print('Lista de Porgramas de TV:')
    for item in promagras:
        print('*',item)
        
    print()
        
        
if __name__ == '__main__':
    main()