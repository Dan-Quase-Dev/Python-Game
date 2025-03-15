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
        return {"coins": 5, "fome": 40, "energia": 100, "feliz": 100, "nome": "Pou", "pontuaçãoMaxima": 0, "vermelhoComprado": False, "azulClaroComprado": False, "azulEscuroComprado": False, "verdeComprado": False, "amareloComprado": False, "roxoComprado": False, "Dolf": False, "nessecidades": 0, "banho": 0, "pao": 0, "salada": 0, "pastel": 1, "coxinha": 0, "AmigoDoDolf": False, "Alimentado": False, "GuerreiroMatematico": False, "sortudo": False, "NameTag": False, "rico": False, "nomes": 0, "comidasDadas": 0, "vezes": 0}  


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
vitorias = 0


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
DVezes = 0
DFraseNum = random.randint(0, 2)
 # Frases Dolf
DFrases = [f"{azulEscuro}Dolf:{amarelo}Ei vem que eu tenho umas coisas.", f"{azulEscuro}Dolf:{amarelo}Ae pega esse dinheiro.", f"{azulEscuro}Dolf:{amarelo}Tenho dinheiro e muito mais."]
DFrases2 = [f"{azulEscuro}Dolf:{amarelo}Sabia que você viria. (:", f"{azulEscuro}Dolf:{amarelo}Ae vocé veio!", f"{azulEscuro}Dolf:{amarelo}Vem que tem coisa boa."]
DFrases3 = [f"{azulEscuro}Dolf:{amarelo}Vou me arrepender disso, mas ai eu te ajudei, me dá uma nota boa.", f"{azulEscuro}Dolf:{amarelo}Espero que pelo menos seja uma nota boa", f"{azulEscuro}Dolf:{amarelo}Eu sou nota 10... Né?"]
DFrases4 = [f"{azulEscuro}Dolf:{amarelo}Ei! Já que você já me visitou tantas vezes pega isso de brinde", f"{azulClaroComprado}Dolf:{amarelo}Vem que eu tenho essa conquista pra te dar", f"{azulClaroComprado}Dolf:{amarelo} Você já é meu amigo a bastante tempo, mas agora pegue isso como prova de nossa amizade"]

# Conquistas
AmigoDoDolf = dados["AmigoDoDolf"] # Visite Dolf 100 vezes
Alimentado =  dados["Alimentado"] # Alimente seu pet pela primeira vez
GuerreiroMatematico = dados["GuerreiroMatematico"] # Vença batalha numerosa 1 vez
sortudo = dados["sortudo"] # tenha sorte para que um núnero gerado aleátoriamente seja igual à 123
NameTag = dados["NameTag"] # Dê um novo nome ao seu pet
rico = dados["rico"] # tenha 1000 moedas
# Raridades
# Branco: Comum
# Verde: Incomum
# Amarelo: Raro
# Azul Claro: Épico
# Roxo: Mítico

# Números
sorte = random.randint(0, 10000)
nomes = dados["nome"]
comidasDadas = dados["comidasDadas"]
vezes = dados["vezes"]
# ----------------------------------
# codigos

while True:
    VerificarCor()
    fraseNum = random.randint(0, 4)
    sorte = random.randint(0, 10000)
    energia -= 5
    fome += 5
    nessecidades += 10

    if fome >= 80:
        energia -= 20
    
    elif fome >= 95:
        energia -= 50


    if sorte == 123 and sortudo == False:
        sortudo = True
        print("Conquista desbloqueada")
        print(f"{roxo}-=Sortudo=-")
        VerificarCor()
    elif sorte != 123:
        pass


    if coins >= 1000 and rico == False:
        rico = True
        print("Conquista Desbloqueada")
        print(f"{amarelo}-=Rico=-")
        VerificarCor()
    elif coins < 1000:
        pass

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
                vezes += 1
                while True:
                    print(f"Fome: {fome}")
                    print("Escolha a Comida:")
                    print("[0] < Sair")
                    if pao == 1:
                        print(f"[1] Pão / {pao} Pão")
                    if pao != 1:
                        print(f"[1] Pão / {pao} Pães")

                    if salada != 1:
                        print(f"[2] Salada / {salada} Saladas")
                    if salada == 1:
                        print(f"[2] Salada / {salada} Salada")

                    if pastel != 1:
                        print(f"[3] Pastel / {pastel} Pasteis")
                    if pastel == 1:
                        print(f"[3] Pastel / {pastel} Pastel")

                    if coxinha != 1:
                        print(f"[4] Coxinha / {coxinha} Coxinhas")
                    if coxinha == 1:
                        print(f"[4] Coxinha / {coxinha} Coxinha")

                    resp11 = intup("> ")

                    if resp11 == 1:
                        if pao < 1:
                            print("Sem pão")
                        if fome <= 9:
                            print("Sem fome")
                        if pao >= 1 and fome >= 10:
                            fome -= 10
                            pao -= 1
                            comidasDadas += 1
                            print("Alimentado.")
                    
                    elif resp11 == 2:
                        if salada < 1 :
                            print("Sem salada")
                        if fome <= 9:
                            print("Sem fome")
                        if salada >= 1 and fome >= 10:
                            fome -= 5
                            salada -= 1
                            comidasDadas += 1
                            print('Alimentado')

                    elif resp11 == 3:
                        if pastel < 1 :
                            print("Sem pastel")
                        if fome <= 14:
                            print("Sem fome")
                        if pastel >= 1 and fome >= 15:
                            fome -= 15
                            pastel -= 1
                            comidasDadas += 1
                            print("Alimentado")

                    elif resp11 == 3:
                        if coxinha < 1:
                            print("Sem coxinha")
                        if fome <= 19:
                            print("Sem fome")
                        if coxinha >= 1 and fome >= 20:
                            fome -= 20
                            coxinha -= 1
                            comidasDadas += 1
                            print("Alimentado")

                    

                    elif resp11 == 0:
                        if comidasDadas == 1 and vezes == 1 and Alimentado == False:
                            Alimentado = True
                            print("Conquista Desbloqueda")
                            print(f"{branco}-=Alimentado=-")
                            VerificarCor()
                        comidaNum = pao + salada + coxinha + pastel
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
                        comidaNum = pao + salada + coxinha + pastel
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
                    vidaBot = 50
                    vidaPlater = 50
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
                                vitorias += 1
                                print("Você ganhou")
                                coins += vidaPlater
                                time.sleep(2)
                                if vitorias >= 1 and GuerreiroMatematico == False:
                                    GuerreiroMatematico = True
                                    print("Conquista Debloqueada")
                                    print(f"{verde}-=Guerreiro Matemático=-")
                                    VerificarCor()
                                elif vitorias < 1:
                                    pass
                                time.sleep(2)
                            break
                        resp10 = intup("-> ")

                        if resp10 > itensLista:
                            print("Sem essa carta")
                        
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
            print("[4] Conquistas")

            resp8 = intup("Digite função: ")

            if resp8 == 2:
                print("Digite \'Sair\' para sair")

                while True:
                    fraseNum = random.randint(0, 5)
                    respText = input("-> ")

                    if respText.upper() != "SAIR":
                        print(f"{nome}: {frases[fraseNum]}")

                    elif respText.upper() == "SAIR":
                        print("Saindo...")
                        time.sleep(1.5)
                        break

            elif resp8 == 3:
                print("Qual será o novo nome?")
                nome = input("-> ")

                print(f"Nome alterado para {nome}")
                nomes +=1

                time.sleep(3)
                if nomes == 1 or nomes == 0 and NameTag == False:
                    NameTag = True
                    print("Conquista Desbloqueada")
                    print(f"{branco}-=Name Tag=-")
                    VerificarCor()
                elif nomes > 1:
                    pass

                time.sleep(2)

            elif resp8 == 4:
                while True:
                    print("Conquistas")
                    if rico == False:
                        print("???")
                        print("  ???")
                    elif rico == True:
                        print(f"{amarelo} 1.Rico")
                        print("  Tenha pelo menos 1000 moedas")
                        VerificarCor()

                    if NameTag == False:
                        print("???")
                        print("  ???")
                    elif NameTag == True:
                        print(f"{branco} 2.Name Tag")
                        print("  Dê um novo nome ao seu pet")
                        VerificarCor()

                    if sortudo == False:
                        print("???")
                        print("  ???")
                    elif sortudo == True:
                        print(f"{roxo} 3.Sortudo")
                        print("  Tenha a sorte de um número gerado aleátoriamente entre 1 e 10 mil seja igual à 123")
                        VerificarCor()

                    if GuerreiroMatematico == False:
                        print("???")
                        print("  ???")
                    elif GuerreiroMatematico == True:
                        print(f"{verde} 4.Guerreiro Matemático")
                        print("  Vença pelo menos uma vez o jogo Batalha Númerosa.")
                        VerificarCor()

                    if Alimentado == False:
                        print("???")
                        print("  ???")
                    elif Alimentado == True:
                        print(f"{branco} 5.Alimentado")
                        print(f"  Alimente {nome} pelo menos uma vez.")
                        VerificarCor()

                    print("- Conquistas Especiais")
                    if AmigoDoDolf == False:
                        print(azulEscuro)
                        print("???")
                        print("  ???")
                        VerificarCor()
                    elif AmigoDoDolf == True:
                        print(f"{azulEscuro} 1.Amigo Do Dolf")
                        print("  Visite Dolf 100 vezes")
                        VerificarCor()


                    print("[0] Sair")
                    print("[1] Raridades")
                    resp12 = intup(">")

                    if resp12 == 1:
                        print("Raridades:")
                        print(f"{branco}Branco: Comum")
                        print(f"{verde}Verde: Incomum")
                        print(f"{amarelo}Amarelo: Raro")
                        print(f"{azulClaro}Azul Claro: Épico")
                        print(f"{roxo}Roxo: Mítico")
                        VerificarCor()
                        print("-=" * 40)
                        print("")
                        print(f"{azulEscuro}Azul Escuro: Conquistas Especiais(Grau 2 de raidade)")
                        print(f"{vermelho}Vermelho: Conquistas Especiais (Grau 1 de raridade)")
                        VerificarCor()
                        time.sleep(8)

                    elif resp12 == 0:
                        print("Saindo")
                        time.sleep(0.5)
                        break



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

        if DVezes >= 100:
            AmigoDoDolf = True
            print(f"{DFrases4[DFraseNum]}")
            VerificarCor()
            print("Conquista(Especial) Desbloqueada")
            print(f"{azulEscuro} Amigo Do Dolf")
            VerificarCor()
        elif DVezes < 100:
            pass
        while True:

            VerificarCor()

            print("[0] Voltar | [1] Moedas | [2] Diminuir Fome")
            print("[3] Mais energia | [4] Dar Nota")

            Dresp = intup("-> ")

            if Dresp == 1:
                print(f'{azulEscuro}Dolf:{amarelo}Tá mas, quantas moedas você quer?')
                VerificarCor()

                Dresp2 = intup("-> ")
                coins = Dresp2

                print(f"{azulEscuro}Dolf:{amarelo}Tá. É só eu mudar o valor, e... Pronto!")
                VerificarCor()


            elif Dresp == 2:
                print(f"{azulEscuro}Dolf:{amarelo} fome-= 1000, pronto")

                fome -= 1000
                VerificarCor()


            elif Dresp == 3:
                print(f"{azulEscuro}Dolf:{amarelo} energia infinita? Ok.")
                energia += 1999999999999999999999999999999999999999999999999999
                VerificarCor()

            elif Dresp == 4:
                while True:
                    print(f"{DFrases3[DFraseNum]}")
                    VerificarCor()

                    Dresp = intup("Nota: ")

                    if Dresp == 0:
                        print(f"{fonteAzulEscuro}Dolf:{amarelo});")
                        VerificarCor()

                    elif Dresp >= 5 and Dresp < 10:
                        print(f"{azulEscuro}Dolf:{amarelo} Pra mim isso já é alguma coisa.")
                        print(f"{azulEscuro}Dolf:{amarelo} Mas podia ser melhor.")
                        VerificarCor()

                    elif Dresp >= 10:
                        print(f"{azulEscuro}Dolf:{amarelo} AEEEEEEEE, UMA NOTA BOA. :D")
                        VerificarCor()

                    break
            
            elif Dresp == 0:
                print(f"{azulEscuro}Dolf:{amarelo}Tchau, amigo.")




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
        print("Os números apareçeram no canto da tela assim:")
        time.sleep(0.5)
        print("[0] opção 1")
        print("[1] opção 2")
        print("[2] opção 3")
        time.sleep(0.8)
        print("Digite uma das opções para interagir indo para uma nova área")
        print("Caso você saia do jogo, seu progresso será salvo em um arquivo JSON")
        time.sleep(1)
        print(f"{vermelho}Aviso: As personalizações do jogo são cores de fonte funciona no VsCode")
        print("mas em alguns lugares as cores não funcionam.")
        VerificarCor()
        time.sleep(0.5)
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

dados["nome"] = nome

dados["pao"] = pao
dados["salada"] = salada
dados["pastel"] = pastel
dados["coxinha"] = coxinha



dados["pontuaçãoMaxima"] = pontuaçãoMaxima


dados["vermelhoComprado"] = vermelhoComprado
dados["azulEscuroComprado"] = azulEscuroComprado
dados["azulClaroComprado"] = azulClaroComprado
dados["verdeComprado"] = verdeComprado
dados["amareloComprado"] = amareloComprado
dados["roxoComprado"] = roxoComprado

dados["Dolf"] = Dolf

dados["AmigoDoDolf"] = AmigoDoDolf
dados["Alimentado"] = Alimentado
dados["GuerreiroMatematico"] = GuerreiroMatematico
dados["NameTag"] = NameTag
dados["sortudo"] = sortudo
dados["rico"] = rico

dados["nomes"] = nomes
dados["comidasDadas"] = comidasDadas
dados["vezes"] = vezes

salvar_dados(dados)

print("Você saiu")

time.sleep(2.5)
