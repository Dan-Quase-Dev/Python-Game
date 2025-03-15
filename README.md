# Pou em Python e Sem Imagens

## Código por trás do jogo:

### Código por IA:

Querido usador desse repositório, primeiro gostaria de falar que as funções: intup, salvar_dados e carregar_dados foram criadas pelo chatGPT, pois não sabia como fazer as funções sozinho.
#### Códigos feitos por IA:
```python
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

        # essas variáveis eu que criei
        # Eu só ajeitei para funcionar no jogo

```

###  Código por mim:

O resto do código alêm do que foi citado em cima é todo criado por mim, o jogo funciona a base de while(loops) e if/elif(condições).
O código que criei tem mais  de 800 linhas, não diria que é otimizado aliás existem formas melhores de fazer os códigos desse jogo, mas ainda não sou muito bom em programação a ponto de criar um jogo ou programa muito milaborante, mas, para mim esse projeto já é o suficiente.


## O Jogo:

### Sobre:
O jogo é tipo um pou sem imagens (tem uma área do jogo que explica sobre o jogo), o objetivo é cuidar de seu pet, você pode mudar o nome do seu pet, alimetar, brincar com ele e mudar a cor da fonte dele(Funcionava no **VsCode**), o jogo pode conter bugs mas eu acho e resolvo depois.

### Mecânicas

Não tem segredo, se jogar esse jogo vai ver opções númerada, por exemplo:

[0] Sair

[1] Ação

[2] Brincar

Então é só digitar 0, 1, 2 e as outras opções que tiver, ou seja se estiver lá [2] Brincar significa que digitando 2 e apertando enter você irá brincar com seu pet.

### Desenvolvedor:

Se de alguma forma você pegou esse código sem ver o desenvolvedor do jogo, bem, o criador desse jogo é @Dan-Quase-Dev


## Atualizações:
###Mudança na ReadMe:
- Nova aba: Atualizações
- Leve mudança na parte do "Código por IA"
- Removido: Aba de agradecimento(pode voltar em breve)
###Mudança no Código:
- Conquistas adicionadas
- Melhoria na aba "Info"
