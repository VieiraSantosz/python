from modelos.programa import Filme
from modelos.programa import Serie
from modelos.playlist import Playlist

velozes = Filme('+Velozes e +Furiosos', 2002, 150)
batman  = Filme('Batman e Coringa', 2015, 180)
f1      = Serie('F1 Drive Survive', 2020, 6)
round6  = Serie('Round 6', 2022, 2)

listinha = [velozes, batman, f1, round6]

minha_playlist = Playlist('fim de semana', listinha)


def main():
    print(f'\nLista da Minha Playlist - {len(minha_playlist)}:')
    for programa in minha_playlist:
        print(programa)
        
    print()
        
        
if __name__ == '__main__':
    main()