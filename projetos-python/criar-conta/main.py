from conta    import Conta


wesley   = Conta(11, 'Wesley Vieira', 3000, 4000)
geovanna = Conta(21, 'Geovanna Vieira', 1500, 5000)


def main():
    wesley.depositar(1500)
    geovanna.depositar(1500)
    
    print('\nExtrato após o depósito:')
    wesley.extrato()
    geovanna.extrato()
    
    print('\nSaque de dinheiro:')
    wesley.sacar(2000)
    geovanna.sacar(9000)
    
    print('\nTransferir dinheiro:')
    wesley.transferir(geovanna, 1500)
    wesley.extrato()
    geovanna.extrato()
    print()
    
    
if __name__ == '__main__':
    main()