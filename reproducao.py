import random

def pode_procriar(tamagotchi):
    if tamagotchi["nivel"] < 3:
        return False

    if tamagotchi["saude"] <= 50:
        return False

    if tamagotchi["fome"] <= 50:
        return False

    return True

def criar_filhote(pai, mae, nome):
    especie = random.choice(
        [
            pai["especie"],
            mae["especie"]
        ]
    )

    saude = random.randint(
        min(
            pai["saude"],
            mae["saude"]
        ),
        max(
            pai["saude"],
            mae["saude"]
        )
    )

    filhote = {
        "nome": nome,
        "especie": especie,
        "nivel": 0,
        "experiencia": 0,
        "saude": saude,
        "fome": 20,
        "felicidade": 50,
        "energia": 50
    }

    return filhote
