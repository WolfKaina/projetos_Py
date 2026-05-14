print("BEM VINDO AO QUIZ")

resp_user = input("Você quer prosseguir com o quiz? [S/N] ").upper()
if resp_user != "S":
    quit()

print("Começando...\n")

# Criar lista onde cada item é um dicionario contendo a pergunta e a resposta
quiz_dados = [
    {
        "pergunta": "1)Quem roubou o Titã Original da familia Fritz em Attack on Titan? \n (A)Eren Yeger \n (B)Mikasa Ackerman \n (C)Grisha Yeger \n (D)Zeke Yeager \n",
        "gabarito": "C"
    },
    {
        "pergunta": "2) Qual foi o primeiro Titã apresentado em Attack on Titan? \n (A)Titã Carroça \n (B)Titã Femea \n (C)Titã Sorridente \n (D)Titã Colossal \n",
        "gabarito": "D"
    },
    {
        "pergunta": "3) Qual Titã derrubou a muralha onde o Eren Yeger morava e qual era essa muralha? \n (A)Titã Colossal / Muralha Maria \n (B)Titã Blindado / Muralha de Shinganshina \n (C)Titã Colossal / Muralha de Shiganshina \n (D)Titã Blindado / Muralha Maria \n",
        "gabarito": "C"
    }    
]

cont =  0 

#loop percorre por cada pergunta
for item in quiz_dados:
    print(item["pergunta"])
    resposta = input ("Resposta: ").upper()
    
    if resposta == item["gabarito"]:
        print("Correto!\n")
        cont += 1
    else:
        print("Incorreto\n")
print(f"Pontuação Final: {cont}/{len(quiz_dados)}")
    
    