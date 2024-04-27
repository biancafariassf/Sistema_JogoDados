import random 

def jogar_dados():
    dado_um = random.randint(1, 6)
    dado_dois = random.randint(1, 6)

    soma = dado_um + dado_dois

    print(f"Você lançou os dados e o resultado do primeiro dado foi {dado_um} e o do segundo foi {dado_dois}")

    if soma == 7:
        print("Você venceu, a soma das faces do dado foi igual a sete")
    else:
        print("Você perdeu, a soma das faces do dado NÃO foi igual a sete")

    jogar_dados()