from pilha import Pilha


pilha = Pilha(3)


def main():
    print()
    print(pilha)
    print()

    pilha.push(9)
    pilha.push(15)
    pilha.push(78)
    print()

    pilha.pop()
    print()

    print('Elementos na Pilha:')
    for item in pilha:
        print('*', item)
        
    print(f'\nTamanho da Pilha: {pilha.tamanho_pilha}')
    print(f'Elemento do Topo: {pilha.elemento_topo}')
    print()
    
if __name__ == '__main__':
    main()