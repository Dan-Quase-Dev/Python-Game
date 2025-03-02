import time
import random
import json
# Funções

def intup(prompt):
    while True:
        try:
            userINP = int(input(prompt))
            return userINP
        except ValueError:
            print("Escolha uma das opções acima")


def salvar_dados(dados):
    with open("saveJ2.json", "w") as file:
        json.dump(dados, file)
def carregar_dados():
    try:
        with open("saveJ2.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"coins": 5, "fome": 40, "energia": 100, "feliz": 100, "nome": "Pou", "pontuaçãoMaxima": 0, "vermelhoComprado": False, "azulClaroComprado": False, "azulEscuroComprado": False, "verdeComprado": False, "amareloComprado": False, "roxoComprado": False, "Dolf": False, "nessecidades": 0, "banho": 0, "pao": 1, "salada": 0, "pastel": 0, "coxinha": 0}  


def VerificarCor():
    if fonteVermelho == True:
        print(vermelho)

    elif fonteAmarelo == True:
        print(amarelo)

    elif fonteVerde == True:
        print(verde)

    elif fonteAzulEscuro == True:
        print(azulEscuro)

    elif fonteAzulClaro == True:
        print(azulClaro)

    elif fonteRoxo == True:
        print(roxo)

    else:
        print(branco)





dados = carregar_dados()



#-----------------------------------
# variáveis


# Dados Básicos

energia = dados["energia"] # energia do pou
feliz = dados["feliz"] # mostra o quão feliz o pou está
coins = dados["coins"] # dinheiro do plater
# Comidas
fome = dados["fome"] # a fome do pou
pao = dados["pao"]
salada = dados["salada"]
pastel =  dados["pastel"]
coxinha = dados["coxinha"]
comidaNum = pao + salada + pastel + coxinha # quantidade de comidas

# Banheiro
nessecidades = dados["nessecidades"] # vontade de mijar ou cagar
banho = dados["banho"] # o quão sujo o pou está

# Textos
nome = dados["nome"]
fraseNum = random.randint(0, 5)
frases = ["Haha engraçado.", "huuummm, acho que não.", "Eehhhhhhhhhhhh... Talvez...?", "Eu gosto da tua mãe, aquela gostosa.", "Isso é fácil!", "Não entendi o que você quis dizer"]
frasesEspecias = ["NaaaaAAAÂâaãaaãa~~ão cCaaalleEE A bOOOccccÂÂAããÃ", "Porquê quer saber?", "...", "Quee-quem é é ... bo- bo- bot?", "Quem você acha que é?", "@#@$/;.,<><<,.,0,.+-*%¨&&*¨¨&/*+"]

# números do jogo
maxNum = 2
minNum = 0
GameNum = random.randint(minNum, maxNum)
aumento = 0
pontuação = 0
pontuaçãoMaxima = dados["pontuaçãoMaxima"]

# Números do outro jogo:
cartasPlater = [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
cartasBot = [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
vidaPlater = 50
vidaBot = 50
cartasnum = 0
opNum = 1


# Cores:
vermelho = "\033[31m"
azulEscuro = "\033[34m" # Nome Dolf
azulClaro = "\033[36m"
verde = "\033[32m"
amarelo = "\033[33m" # Falas Dolf
roxo = "\033[35m"
branco = "\033[m"

fonteVermelho = False
fonteAzulClaro = False
fonteAzulEscuro = False
fonteVerde = False
fonteAmarelo = False
fonteRoxo = False

vermelhoComprado = dados["vermelhoComprado"]
azulEscuroComprado = dados["azulEscuroComprado"]
azulClaroComprado = dados["azulClaroComprado"]
verdeComprado = dados["verdeComprado"]
amareloComprado = dados["amareloComprado"]
roxoComprado = dados["roxoComprado"]

# Dolf
Dolf = dados["Dolf"]
AmigoDoDolf = False
DVezes = 0
DFraseNum = random.randint(0, 2)
 # Frases Dolf
DFrases = [f"{azulEscuro}Dolf:{amarelo}Ei vem que eu tenho umas coisas.", f"{azulEscuro}Dolf:{amarelo}Ae pega esse dinheiro.", f"{azulEscuro}Dolf:{amarelo}Tenho dinheiro e muito mais."]
DFrases2 = [f"{azulEscuro}Dolf:{amarelo}Sabia que você viria. (:", f"{azulEscuro}Dolf:{amarelo}Ae vocé veio!", f"{azulEscuro}Dolf:{amarelo}Vem que tem coisa boa."]
DFrases3 = [f"{azulEscuro}Dolf:{amarelo}", f"{azulEscuro}Dolf:{amarelo}", f"{azulEscuro}Dolf:{amarelo}"]



# ----------------------------------
# codigos

while True:
    VerificarCor()
    fraseNum = random.randint(0, 4)
    energia -= 5
    fome += 5
    nessecidades += 10

    if fome >= 80:
        energia -= 20
    
    elif fome >= 95:
        energia -= 50

    print(f"Energia: {energia}")
    print(f"Fome: {fome}")
    print(f"Felicdade: {feliz}")
    print(f"Dinheiro: {coins}")
    print(f"Banheiro: {nessecidades}")
    print(f"Banho: {banho}")
    print("Escolha função")
    print("[1] Cozinha | [2] Quintal | [3] Quarto")
    print("[4] Sala de estar | [5] Banheiro | [99] Info")
    if Dolf == True:
        print("[415126] Dolf")

    print("[0] < Sair")


    resp1 = intup("Digite uma das opções acima: ")

    if resp1 == 1:
        while True:
            print(f"Fome: {fome}")
            print(f"Quantidade de Comidas: {comidaNum}")
            print(f"Dinheiro: {coins}")

            if comidaNum >= 1:
                print("[1] Alimentar")

            print("[2] Comprar Comida")
            print("[3] < Voltar")

            resp2 = intup("Digite opção: ")

            if resp2 ==  1 and comidaNum >= 1 and fome >= 10:
                while True:
                    print(f"Fome: {fome}")
                    print("Escolha a Comida:")
                    print("[0] < Sair")
                    print("[1] Pão")
                    print("[2] Salada")
                    print("[3] Pastel")
                    print("[4] Coxinha")

                    resp11 = intup("> ")

                    if resp11 == 1:
                        if pao >= 1 and fome >= 10:
                            fome -= 10
                            pao -= 1
                            print("Alimentado.")
                        if pao < 1 and fome >= 10:
                            print("Sem pão")
                        if fome <= 9:
                            print("Sem fome")
                    
                    elif resp11 == 2:
                        if salada >= 1 and fome >= 10:
                            fome -= 5
                            salada -= 1
                            print('Alimentado')
                        if salada < 1 and fome >= 10:
                            print("Sem salada")
                        if fome <= 9:
                            print("Sem fome")

                    elif resp11 == 3:
                        if pastel >= 1 and fome >= 10:
                            fome -= 15
                            pastel -= 1
                            print("Alimentado")
                        if pastel < 1 and fome >= 10:
                            print("Sem pastel")
                        if fome <= 9:
                            print("Sem fome")

                    elif resp11 == 3:
                        if coxinha >= 1 and fome >= 10:
                            fome -= 20
                            coxinha -= 1
                            print("Alimentado")
                        if coxinha < 1 and fome >= 10:
                            print("Sem coxinha")
                        if fome <= 9:
                            print("Sem fome")

                    elif resp11 == 0:
                        print("Saindo")
                        time.sleep(0.5)
                        break

                    


            elif resp2 == 1 and fome <= 9:
                print("Sem fome")
                time.sleep(1.5)

            elif resp2 == 2:
                while True:
                    print("Comidas:")
                    print("[1] < Sair")
                    print("[2] Pão 5R$")
                    print("[3] Salada 5R$")
                    print("[4] Pastel 7R$")
                    print("[5] Coxinha 7R$")

                    resp3 = intup("Digite opção: ")

                    if resp3 == 2 and coins >= 5:
                        pao +=1
                        coins-=5
                        print("Comprado")
                    
                    elif resp3 == 3 and coins >= 5:
                        salada += 1
                        coins -= 5
                        print("Comprado")

                    elif resp3 == 4 and coins >= 7:
                        pastel += 1
                        coins -= 7
                        print("Comprado")

                    elif resp3 == 5 and coins >= 7:
                        coxinha += 1
                        coins -= 7
                        print("Comprado")

                    elif resp3 == 1:
                        break

            elif resp2 == 3:
                break

    elif resp1 == 2:
        while True:
            print(f"Fome: {fome}\nEnergia: {energia}")
            print("[1] Sair")
            print("[2] brincar")

            resp4 = intup("Escolha opção: ")

            if resp4 == 2 and energia >= 20:
                print("Brincadeiras:")
                print("[1] Sair | [2] Pega-Pega | [3] Xadrez")
                print("[4] Queimada | [5] Uno | [6] Acerte o Número")
                print("[7] Luta Numerosa")


                resp5 = intup("Digite opção: ")

                if resp5 == 2:
                    energia -= 20
                    fome += 5
                    coins += 8
                    feliz += 10
                    print("Vocês brincaram.")
                    
                elif resp5 == 3:
                    energia -= 5
                    coins += 12
                    feliz += 3
                    print("Vocês brincaram")

                elif resp5 == 4:
                    energia -= 20
                    fome += 10
                    coins += 6
                    feliz += 12
                    print("Vocês brincaram.")

                elif resp5 == 5:
                    energia -= 5
                    coins += 5
                    feliz += 5
                    print("Vocês brincaram.")

                elif resp5 ==  6:
                    pontuação = 0
                    maxNum = 2
                    aumento = 0
                    while True:
                        GameNum = random.randint(minNum, maxNum)
                        energia -= 2
                        print(f"Digite um número entre {minNum} e {maxNum}:")


                        gameResp = intup('-> ')

                        if gameResp == GameNum:
                            aumento +=1
                            maxNum += aumento
                            pontuação += 1
                            feliz += 10
                            print("Continue!")

                        elif gameResp == 1612015:
                            coins += 20
                            Dolf = True
                            print("\033[34mDolf:\033[33m Aqui pegue esse dinheiro, mas não conta pra ninguém viu?\033[m")
                            print("\033[34mDolf:\033[33m E também...\033[m")
                            print("Jogo: Nova função adicionada.")
                            VerificarCor()

                            print("Jogo: Nova função adicionada.")

                        elif gameResp != GameNum and gameResp != 1612015:
                            if pontuação >= pontuaçãoMaxima:
                                pontuaçãoMaxima = pontuação

                            if pontuação < pontuaçãoMaxima:
                                pontuaçãoMaxima = pontuaçãoMaxima


                            print("Você Perdeu!")
                            coins += pontuação
                            time.sleep(1)
                            print(f"Pontuação: {pontuação} | Pontuação Maxima: {pontuaçãoMaxima}")
                            print(f"Ganhou {pontuação} Moedas")
                            time.sleep(1.5)
                            break

                elif resp5 == 7:
                    print("Escolha uma carta e torça para que \nela seja maior que a do bot\nQuem tiver a carta menor\nLeva dano somado das suas cartas e do bot")
                    itensLista = 5
                    cartasnum = 0
                    opNum = 1
                    cartasPlater = [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
                    cartasBot = [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
                    while True:
                        print(f"Sua Vida: {vidaPlater} | Vida do Bot: {vidaBot}")
                        print("Escolha uma carta:")
                        while cartasnum != itensLista:
                            print(f"[{opNum}] {cartasPlater[cartasnum]}")
                            cartasnum += 1
                            opNum += 1

                        cartasnum = 0
                        opNum = 1
                        if itensLista == 0 or vidaBot <= 0 or vidaPlater <= 0:
                            if vidaBot > vidaPlater:
                                print("O bot venceu")
                                coins += 5
                            if vidaBot < vidaPlater:
                                print("Você ganhou")
                                coins += vidaPlater
                                time.sleep(2)
                            break
                        resp10 = intup("-> ")


                        
                        if resp10 == 1 and itensLista > 0 and vidaPlater > 0 and vidaBot > 0:
                            print(f"Você escolheu {cartasPlater[0]}")
                            print(f"O Bot escolhe {cartasBot[0]}")
                            if cartasPlater[0] > cartasBot[0]:
                                print("Você Ganha")
                                vidaBot -= cartasPlater[0] + cartasBot[0]
                            if cartasPlater[0] < cartasBot[0]:
                                print("Bot Ganha")
                                vidaPlater -= cartasPlater[0] + cartasBot[0]
                            if cartasPlater[0] == cartasBot[0]:
                                print("Empate")
                            cartasPlater.remove(cartasPlater[0])
                            cartasBot.remove(cartasBot[0])
                            itensLista -= 1
                        

                        elif resp10 == 2 and itensLista > 0 and vidaPlater > 0 and vidaBot > 0:
                            print(f"Você escolheu {cartasPlater[1]}")
                            print(f"O Bot escolhe {cartasBot[1]}")
                            if cartasPlater[1] > cartasBot[1]:
                                print("Você Ganha")
                                vidaBot -= cartasPlater[1] + cartasBot[1]
                            if cartasPlater[1] < cartasBot[1]:
                                print("Bot Ganha")
                                vidaPlater -= cartasPlater[1] + cartasBot[1]
                            if cartasPlater[1] == cartasBot[1]:
                                print("Empate")
                            cartasPlater.remove(cartasPlater[1])
                            cartasBot.remove(cartasBot[1])
                            itensLista -= 1


                        elif resp10 == 3 and itensLista > 0 and vidaPlater > 0 and vidaBot > 0:
                            print(f"Você escolheu {cartasPlater[2]}")
                            print(f"O Bot escolhe {cartasBot[2]}")
                            if cartasPlater[2] > cartasBot[2]:
                                print("Você Ganha")
                                vidaBot -= cartasPlater[2] + cartasBot[2]
                            if cartasPlater[2] < cartasBot[2]:
                                print("Bot Ganha")
                                vidaPlater -= cartasPlater[2] + cartasBot[2]
                            if cartasPlater[2] == cartasBot[2]:
                                print("Empate")
                            cartasPlater.remove(cartasPlater[2])
                            cartasBot.remove(cartasBot[2])
                            itensLista -= 1


                        elif resp10 == 4 and itensLista > 0 and vidaPlater > 0 and vidaBot > 0:
                            print(f"Você escolheu {cartasPlater[3]}")
                            print(f"O Bot escolhe {cartasBot[3]}")
                            if cartasPlater[3] > cartasBot[3]:
                                print("Você Ganha")
                                vidaBot -= cartasPlater[3] + cartasBot[3]
                            if cartasPlater[1] < cartasBot[3]:
                                print("Bot Ganha")
                                vidaPlater -= cartasPlater[3] + cartasBot[3]
                            if cartasPlater[3] == cartasBot[3]:
                                print("Empate")
                            cartasPlater.remove(cartasPlater[3])
                            cartasBot.remove(cartasBot[3])
                            itensLista -= 1
                        

                        elif resp10 == 5 and itensLista > 0 and vidaPlater > 0 and vidaBot > 0:
                            print(f"Você escolheu {cartasPlater[4]}")
                            print(f"O Bot escolhe {cartasBot[4]}")
                            if cartasPlater[4] > cartasBot[4]:
                                print("Você Ganha")
                                vidaBot -= cartasPlater[4] + cartasBot[4]
                            if cartasPlater[4] < cartasBot[4]:
                                print("Bot Ganha")
                                vidaPlater -= cartasPlater[4] + cartasBot[4]
                            if cartasPlater[4] == cartasBot[4]:
                                print("Empate")
                            cartasPlater.remove(cartasPlater[4])
                            cartasBot.remove(cartasBot[4])
                            itensLista -= 1

                        elif resp10 > itensLista:
                            print("Sem essa carta")



                elif resp5 == 1:
                    break

            elif resp4 == 2 and energia < 20:
                print("Muito Cansado para brincar.")

            elif resp4 == 1:
                print("Saindo.")
                time.sleep(1.5)
                break

    elif resp1 == 3:
        while True:
            VerificarCor()


            print("Escolha função")
            print("[1] < Sair")
            print("[2] Dormir")
            print('[3] Personalizar')

            resp6 = intup("Escolher função: ")

            if resp6 == 2:
                print("Dormindo")
                dormir = 30
                while True:
                    print(". . .")
                    time.sleep(1)
                    dormir -=1
                    energia = 105
                    feliz = 10
                    if dormir <= 0:
                        break
            
            elif resp6 == 3:
                while True:
                    print(f"Moedas: {coins}")
                    print("Escolha Cor:")
                    print("[0] < Sair")
                    print("[1] Branco")
                    if vermelhoComprado == False:
                        print("[2] Vermelho / 15 Moedas")
                    elif vermelhoComprado == True:
                        print("[2] Vermelho")

                    if azulClaroComprado == False:
                        print("[3] Azul Claro / 15 Moedas")
                    elif azulClaroComprado == True:
                        print("[3] Azul Claro")

                    if azulEscuroComprado == False:
                        print("[4] Azul Escuro / 15 Moedas")
                    elif azulEscuroComprado == True:
                        print("[4] Azul Escuro")

                    if verdeComprado == False:
                        print("[5] Verde / 15 Moedas")
                    elif verdeComprado == True:
                        print("[5] Verde")

                    if amareloComprado == False:
                        print("[6] Amarelo / 15 Moedas")
                    elif amareloComprado == True:
                        print("[6] Amarelo")

                    if roxoComprado == False:
                        print("[7] Roxo / 15 Moedas")
                    elif roxoComprado == True:
                        print("[7] Roxo")

                    resp7 = intup("Digite função: ")

                    if resp7 == 2 and coins >= 15 and vermelhoComprado == False:
                        print("Comprado.")
                        fonteVermelho = True
                        fonteAzulClaro = False
                        fonteAzulEscuro = False
                        fonteVerde = False
                        fonteAmarelo = False
                        fonteRoxo = False
                        vermelhoComprado = True
                        print(vermelho)
                        coins -= 15

                    elif resp7 == 2 and coins < 15 and vermelhoComprado == False:
                        print("Sem dinheiro.")
                        time.sleep(2.5)

                    elif resp7 == 2 and vermelhoComprado == True:
                        fonteVermelho = True
                        fonteAzulClaro = False
                        fonteAzulEscuro = False
                        fonteVerde = False
                        fonteAmarelo = False
                        fonteRoxo = False
                        print(vermelho)



                    elif resp7 == 3 and coins >= 15 and azulClaroComprado == False:
                        print("Comprado.")
                        fonteVermelho = False
                        fonteAzulClaro = True
                        fonteAzulEscuro = False
                        fonteVerde = False
                        fonteAmarelo = False
                        fonteRoxo = False
                        azulClaroComprado = True
                        print(azulClaro)
                        coins -= 15

                    elif resp7 == 3 and coins < 15 and azulClaroComprado == False:
                        print("Sem dinheiro.")
                        time.sleep(2.5)

                    elif resp7 == 3 and azulClaroComprado == True:
                        fonteVermelho = False
                        fonteAzulClaro = True
                        fonteAzulEscuro = False
                        fonteVerde = False
                        fonteAmarelo = False
                        fonteRoxo = False
                        print(azulClaro)



                    elif resp7 == 4 and coins >= 15 and azulEscuroComprado == False:
                        print("Comprado.")
                        fonteVermelho = False
                        fonteAzulClaro = False
                        fonteAzulEscuro = True
                        fonteVerde = False
                        fonteAmarelo = False
                        fonteRoxo = False
                        azulEscuroComprado = True
                        print(azulEscuro)
                        coins -= 15

                    elif resp7 == 4 and coins < 15 and azulEscuroComprado == False:
                        print("Sem dinheiro.")
                        time.sleep(2.5)

                    elif resp7 == 4 and azulEscuroComprado == True:
                        fonteVermelho = False
                        fonteAzulClaro = False
                        fonteAzulEscuro = True
                        fonteVerde = False
                        fonteAmarelo = False
                        fonteRoxo = False
                        print(azulEscuro)



                    elif resp7 == 5 and coins >= 15 and verdeComprado == False:
                        print("Comprado.")
                        fonteVermelho = False
                        fonteAzulClaro = False
                        fonteAzulEscuro = False
                        fonteVerde = True
                        fonteAmarelo = False
                        fonteRoxo = False
                        verdeComprado = True
                        coins -= 15
                        print(verde)

                    elif resp7 == 5 and coins <= 15 and verdeComprado == False:
                        print("Sem dinheiro.")
                        time.sleep(2.5)

                    elif resp7 == 5 and verdeComprado == True:
                        fonteVermelho = False
                        fonteAzulClaro = False
                        fonteAzulEscuro = False
                        fonteVerde = True
                        fonteAmarelo = False
                        fonteRoxo = False
                        print(verde)



                    elif resp7 == 6 and coins >= 15 and amareloComprado == False:
                        print("Comprado.")
                        fonteVermelho = False
                        fonteAzulClaro = False
                        fonteAzulEscuro = False
                        fonteVerde = False
                        fonteAmarelo = True
                        fonteRoxo = False
                        amareloComprado = True
                        coins -= 15
                        print(amarelo)

                    elif resp7 == 6 and coins <= 15 and amareloComprado == False:
                        print("Sem dinheiro.")
                        time.sleep(2.5)

                    elif resp7 == 6 and amareloComprado == True:
                        fonteVermelho = False
                        fonteAzulClaro = False
                        fonteAzulEscuro = False
                        fonteVerde = False
                        fonteAmarelo = True
                        fonteRoxo = False
                        print(amarelo)



                    elif resp7 == 7 and coins >= 15 and roxoComprado == False:
                        print("Comprado.")
                        fonteVermelho = False
                        fonteAzulClaro = False
                        fonteAzulEscuro = False
                        fonteVerde = False
                        fonteAmarelo = False
                        fonteRoxo = True
                        roxoComprado = True
                        coins -= 15
                        print(roxo)

                    elif resp7 == 7 and coins <= 15 and roxoComprado == False:
                        print("Sem dinheiro.")
                        time.sleep(2.5)

                    elif resp7 == 7 and roxoComprado == True:
                        fonteVermelho = False
                        fonteAzulClaro = False
                        fonteAzulEscuro = False
                        fonteVerde = False
                        fonteAmarelo = False
                        fonteRoxo = True
                        print(roxo)

                    

                    elif resp7 == 1:
                        fonteVermelho = False
                        fonteAzulClaro = False
                        fonteAzulEscuro = False
                        fonteVerde = False
                        fonteAmarelo = False
                        fonteRoxo = False
                        print(branco)



                    elif resp7 == 0:
                        print("Saindo")
                        break


            elif resp6 == 1:
                print("Saindo")
                break


    elif resp1 == 4:
        while True:
            print(f"Energia: {energia}")
            print(f"Fome: {fome}")
            print(f"Felicidade: {feliz}")
            print(f"Dinheiro: {coins}")
            print("Opcões:")
            print("[1] < Sair")
            print("[2] Conversar")
            print("[3] Mudar nome")

            resp8 = intup("Digite função: ")

            if resp8 == 2:
                print("Digite \'Sair\' para sair")

                while True:
                    fraseNum = random.randint(0, 5)
                    respText = input("-> ")

                    if respText.upper() != "SAIR" and respText.upper() != "YOU GHOST THE DAWN O COOL":
                        print(f"{nome}: {frases[fraseNum]}")

                    elif respText.upper() == "YOU GHOST THE DAWN O COOL":
                        print(f'{nome}: Iiihhhhhhhhhhh la ele rapa.')

                    elif respText.upper() == "SAIR":
                        print("Saindo...")
                        time.sleep(1.5)
                        break

            elif resp8 == 3:
                print("Qual será o novo nome?")
                nome = input("-> ")

                print(f"Nome alterado para {nome}")

                time.sleep(3)

            elif resp8 == 1:
                print("Saindo...")
                time.sleep(2)
                break



    
    elif resp1 == 415126 and Dolf == True:
        DVezes += 1
        DFraseNum = random.randint(0, 2)
        print(f"{DFrases2[DFraseNum]}")
        time.sleep(1.5)
        print(f"{azulEscuro}Dolf:{amarelo}Posso te ajudar com muuuuuuuita coisa.")
        time.sleep(0.5)
        print(f"{azulEscuro}Dolf:{amarelo}Pode escolher.")
        time.sleep(1)
        print(f"{azulEscuro}Dolf:{amarelo}Mas tem alguns limites, infelizmente ):")
        while True:

            VerificarCor()

            print("[0] Voltar | [1] Moedas | [2] Diminuir Fome")
            print("[3] Mais energia | [4] Dar Nota")

            Dresp = intup("-> ")

            if Dresp == 1:
                print(f'{azulEscuro}Dolf:{amarelo}Tá mas, quantas moedas você quer?')

                Dresp2 = intup("-> ")
                coins = Dresp2

                print(f"{azulEscuro}Dolf:{amarelo}Tá. É só eu mudar o valor, e... Pronto!")


            elif Dresp == 2:
                print(f"{azulEscuro}Dolf:{amarelo} fome-= 1000, pronto")

                fome -= 1000


            elif Dresp == 3:
                print(f"{azulEscuro}Dolf:{amarelo} energia infinita? Ok.")
                energia += 199999999999999999999999999999999999999999999999990
                break

            elif Dresp == 4:
                print("Não existe ainda")




    elif resp1 == 5:
        while True:
            mijoBosta = random.randint(0, 1)
            print(f"Sujo: {banho}")
            print(f"Nessecidades: {nessecidades}")
            print("Escolha uma Opção")
            print("[0] <- Sair")
            print("[1] Banho")
            print("[2] Vaso sanitário")

            resp9 = intup("Escolha função >")

            if resp9 == 1 and banho <= 20:
                banho = 100
                print("Limpando...")
                time.sleep(2)

            elif resp9  == 2 and nessecidades >= 21:
                nessecidades = 0
                if mijoBosta == 0:
                    print("Cagando...")
                    time.sleep(2)
                if mijoBosta == 1:
                    print("Mijando...")
                    time.sleep(2)

            elif resp9 == 0:
                break


    elif resp1 == 99:
        print("""

| |\\     | |---------  |-----------|
| | \\    | |           |           |
| |  \\   | |_________  |           |
| |   \\  | |           |           |
| |    \\ | |           |           |
| |     \\| |           |___________|
""") 
        print("-" * 50)
        print("O jogo que você está jogando é um pou sem imagens.")
        time.sleep(0.5)
        print("Para \'interagir\' deve digitar 1, 2, 3...")
        time.sleep(0.5)
        print("Apareçera no canto da tela assim:")
        time.sleep(0.5)
        print("[0] opção 1")
        print("[1] opção 2")
        print("[2] opção 3")
        time.sleep(0.8)
        print("Digite uma das opções para interagir indo para uma nova área")
        print("Caso você saia do jogo, seu progresso será salvo em um arquivo JSON")
        print("Atualizações com o tempo.")
        time.sleep(8)



    elif resp1 == 0:
        break


dados["coins"] = coins
dados["fome"] = fome
dados["energia"] = energia
dados["feliz"] = feliz
dados["banho"] = banho
dados["nessecidades"] = nessecidades

dados["pao"] = pao
dados["salada"] = salada
dados["pastel"] = pastel
dados["coxinha"] = coxinha

dados["nome"] = nome


dados["pontuaçãoMaxima"] = pontuaçãoMaxima


dados["vermelhoComprado"] = vermelhoComprado
dados["azulEscuroComprado"] = azulEscuroComprado
dados["azulClaroComprado"] = azulClaroComprado
dados["verdeComprado"] = verdeComprado
dados["amareloComprado"] = amareloComprado
dados["roxoComprado"] = roxoComprado

dados["Dolf"] = Dolf

salvar_dados(dados)

print("Você saiu")

time.sleep(2.5)
