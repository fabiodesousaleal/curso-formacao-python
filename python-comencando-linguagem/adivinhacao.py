print("**********Bem vindo ao jogo de adivinhação *************")

numero_secreto=42
total_tentativa=3
rodada=1

while (rodada <= total_tentativa):
    print("Tentativa {} de {}".format(rodada, total_tentativa))
    chute_str=input("Digite o seu número: ")

    print("Você digitou: ", chute_str)

    chute=int(chute_str)

    acertou = chute==numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!")

    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou! Seu chute foi menor que o número secreto")

    rodada = rodada+1

print("Fim de Jogo")