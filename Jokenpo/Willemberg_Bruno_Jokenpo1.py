nome1 = str(input("Digite o nome do primeiro jogador:"))
nome2 = str(input("Digite o nome do segundo jogador:"))

jogador1 = 0
jogador2 = 0
rodada = 0
c = 0

while c < 3:
    
    print()
    print("1- Pedra")
    print("2- Papel")
    print("3- Tesoura")

    print(nome1,"Digite o numero da sua opção:")
    op1 = int(input())
    print(nome2,"Digite o numero da sua opção:")
    op2 = int(input())

    if ((op1 == 1 and op2 == 1) or (op1 == 2 and op2 == 2) or (op1 == 3 and op2 == 3)):
        print()
        print("Rodada de empate")
        rodada += 1
        c += 1

    if ((op1==1 and op2==3) or (op1==2 and op2==1) or (op1==3 and op2==2)):
        
        print()
        print(nome1, "ganhou essa rodada")
        jogador1 += 1
        rodada += 1
        c += 1

    if ((op2==1 and op1==3) or (op2==2 and op1==1) or (op2==3 and op1==2)):
        print()
        print(nome2,"ganhou essa rodada")
        jogador2 += 1
        rodada += 1
        c += 1

    if ((rodada == 2 and jogador1 == 2) or (rodada == 2 and jogador2 == 2)):
        if(jogador1 > jogador2):
            print()
            print(nome1,"foi o ganhador")
            print("Pontuação:")
            print("{} com {} pontos.".format(nome1,jogador1))
            print(nome2,"com", jogador2, "ponto.")
            print(rodada, "Rodadas jogadas")
            c +=2

        if (jogador2 > jogador1):
            print()
            print(nome2,"foi o ganhador")
            print("Pontuação:")
            print("{} com {} pontos.".format(nome1,jogador1))
            print(nome2,"com", jogador2, "ponto.")
            print(rodada, "Rodadas jogadas")
            c += 2
            
    else:
        if(rodada > 2):
            if (jogador1 > jogador2):
                print()
                print(nome1,"foi o ganhador")
                print("Pontuação:")
                print("{} com {} pontos.".format(nome1,jogador1))
                print(nome2,"com", jogador2, "ponto.")
                print(rodada, "Rodadas jogadas")

            if (jogador2 > jogador1):
                print()
                print(nome2,"foi o ganhador")
                print("Pontuação:")
                print("{} com {} pontos.".format(nome1,jogador1))
                print(nome2,"com", jogador2, "ponto.")
                print(rodada, "Rodadas jogadas")
            
            if (jogador2 == jogador1):
                print()
                print("Houve um empate")
                print("Pontuação:")
                print("{} com {} pontos.".format(nome1,jogador1))
                print(nome2,"com", jogador2, "ponto.")
                print(rodada, "Rodadas jogadas")
