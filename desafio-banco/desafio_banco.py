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
LIMITE_DE_SAQUE = 3
quantidade_de_saque = 0
while True :

    print(menu)
    opcao = input("\nO que deseja fazer?")
    opcao = opcao.lower()

    
    if(opcao == "d"):

        movimento_de_caixa = float(input("\nValor do Deposito: "))

        if(movimento_de_caixa > 0):
            deposito_total += movimento_de_caixa
            saldo = saldo + movimento_de_caixa
            houve_movimentacao = True

            print(f"\nDeposito de R$:{movimento_de_caixa} REALIZADO.")

        else:
            print("NÃO FOI POSSÍVEL DEPOSITAR.")

    elif(opcao == 's'):

        if(quantidade_de_saque < LIMITE_DE_SAQUE):

            movimento_de_caixa = float(input("\nValor do Saque: "))

            if(movimento_de_caixa <= 500 and movimento_de_caixa <= saldo):
                saque_total = saque_total + movimento_de_caixa
                saldo = saldo - movimento_de_caixa
                quantidade_de_saque += 1
                houve_movimentacao = True

                print(f"\nSaque de R$:{movimento_de_caixa} REALIZADO.")
            else:
                print("NÃO FOI POSSÍVEL SACAR.")

    elif(opcao == "e"):

        if(houve_movimentacao == True):
            print("")
            print(f'''
                            Extrato
                    Valor total de Saque: R$:{saque_total},
                    Valor total de Deposito: R$:{deposito_total},
                        O Saldo é R$:{saldo}.''')
            
        else:
            print("NÃO HOUVE MOVIMENTAÇÕES.")

    elif(opcao == "q"):
        break

    else:
        print("OPÇÃO INFORMADA INVÁLIDA.")
