print("**********Bem vindo ao jogo de adivinhação *************")

numero_secreto=42
total_tentativa=3

for rodada in range(1, total_tentativa+1):
    print("Tentativa {} de {:07d}".format(rodada, total_tentativa))
    chute_str=input("Digite um número entre 1 e 100: ")

    print("Você digitou: ", chute_str)

    chute=int(chute_str)
    if(chute < 1 or chute >100):
        print("Número inválido!")
        continue


    acertou = chute==numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print(f"Você acertou! {numero_secreto} é seu número da sorte!'")
        break

    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou! Seu chute foi menor que o número secreto")

print("Fim de Jogo")