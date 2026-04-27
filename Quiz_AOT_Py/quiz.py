print("BEM VINDO AO QUIZ")

resp_user = input("Você quer prosseguir com o quiz? [S/N] ").upper()
print(resp_user)
cont = 0
if resp_user != "S":
    quit()
print("Começando...")
print("1) Quem roubou o Titã Original da familia Fritz em Attack on Titan? \n (A)Eren Yeger \n (B)Mikasa Ackerman \n (C)Grisha Yeger \n (D)Zeke Yeager \n")
resp_1 = input("Resposta: ").upper()

if resp_1 != "C":
    print("Incorreto")
else:
    print("Correto!")
    cont += 1 
    
print("2) Qual foi o primeiro Titã apresentado em Attack on Titan? \n (A)Titã Carroça \n (B)Titã Femea \n (C)Titã Sorridente \n (D)Titã Colossal \n")
resp_1 = input("Resposta: ").upper()

if resp_1 != "D":
    print("Incorreto")
else:
    print("Correto!")
    cont += 1 
    
print("3) Qual Titã derrubou a muralha onde o Eren Yeger morava e qual era essa muralha? \n (A)Titã Colossal / Muralha Maria \n (B)Titã Blindado / Muralha de Shinganshina \n (C)Titã Colossal / Muralha de Shiganshina \n (D)Titã Blindado / Muralha Maria \n")
resp_1 = input("Resposta: ").upper()

if resp_1 != "C":
    print("Incorreto")
else:
    print("Correto!")
    cont += 1 

print("4) Quem descobriu a verdadeira identidade da Titã Femêa? \n (A)Armin Arleot \n (B)Erwin Smith \n (C)Levi Ackerman \n (D)Hange Zoe \n")
resp_1 = input("Resposta: ").upper()

if resp_1 != "A":
    print("Incorreto")
else:
    print("Correto!")
    cont += 1 

print("5) Quais foram os nomes dos primeiros Titãns capiturado pela Hange Zoe? \n (A)Sawney e Bean \n (B)Sawney e Chikachironi \n (C)Chikachironi e Albert \n (D)Bean e Albert \n")

resp_1 = input("Resposta: ").upper()

if resp_1 != "A":
    print("Incorreto")
else:
    print("Correto!")
    cont += 1 

print(f"Pontuação Final: {cont}/5")
