import random  #https://docs.python.org/pt-br/3/library/random.html

print("SEJA MUITO BEM VINDO A ROLETA RUSSA")

capac_tambor = int(6)
cont = 0
random_cartucho = random.randint(1, capac_tambor)
print(random_cartucho)
while True:
    if cont == capac_tambor -1:
        suicidio = input("Parabens, você venceu! \n Clique [A] para comemorar: ").upper()
        if suicidio ==  "A":
            print("Você cometeu Suicídio!")
        else:
            exit()
    else:
        girar = input ("Gire o Tambor: [G] ").upper()
        if girar == "G":     
            random_tambor = random.randint(1, capac_tambor)
            print(f"{random_tambor} / {random_cartucho}")
            print(cont)
        while True:
            atirar = input ("Atire [A]").upper()
            if atirar != "A":
                print("Engraçadinho, tente novamente")
                continue
            else:
                break
        if random_cartucho == random_tambor:
            print("Você Morreu!\n")
            exit()
        else:
            escolha = input(f"Você passou, deseja continuar? [S/N]\n").upper()
            if escolha == "S":
                cont +=1
                continue
            else:
                print("Devia ter pensado nisso antes de jogar \n Continue...\n")
                cont +=1
                continue
                        

        


