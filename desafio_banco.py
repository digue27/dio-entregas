menu = """
(D) - Depósito.
(S) - Saque.
(E) - Extrato
(Q) - Sair

"""
opcao =''
saldo = 0.0
deposito_total = 0.0
saque_total = 0.0
houve_movimentacao = False
QUANTIDADE_DE_SAQUE = 3

while True :

    opcao = input("O que deseja fazer?\n")
    opcao = opcao.lower()
    print(menu)
    
    if(opcao == "d"):

        movimento_de_caixa = float(input("Valor do Deposito: \n"))

        if(movimento_de_caixa > 0):
            deposito_total += movimento_de_caixa
            saldo = saldo + movimento_de_caixa
            houve_movimentacao = True

            print(f"Deposito de R$: {movimento_de_caixa}")

        else:
            print("Não foi possivel Depositar")

    elif(opcao == 's'):

        if(QUANTIDADE_DE_SAQUE > 0 and saldo >= 0):

            movimento_de_caixa = float(input("Valor do Saque: \n"))

            if(movimento_de_caixa <= 500 and movimento_de_caixa <= saldo):
                saque_total = saque_total + movimento_de_caixa
                saldo = saldo - movimento_de_caixa
                QUANTIDADE_DE_SAQUE -= 1
                houve_movimentacao = True

                print(f"Saque de R$: {movimento_de_caixa}")
            else:
                print("Não foi possivel sacar.")

    elif(opcao == "e"):

        if(houve_movimentacao == True):
            print("Extrato")
            print(f'''
                    Valor total de Saque: R$:{saque_total},
                    Valor total de Deposito: R$:{deposito_total},
                    O Saldo é R$:{saldo}.''')
            
        else:
            print("Não houve movimentações.")

    elif(opcao == "q"):
        break

    else:
        print("Opção informada não valida")
