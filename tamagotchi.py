import random
from config import NIVEIS


def criar_tamagotchi(nome, especie):
    tamagotchi = {
        "nome": nome,
        "especie": especie,
        "nivel": 1,
        "experiencia": 0,
        "saude": especie["saude"],
        "fome": especie["fome"],
        "felicidade": especie["felicidade"],
        "energia": especie["energia"]
    }

    return tamagotchi


def limitar_atributo(valor):
    if valor < 0:
        return 0

    if valor > 100:
        return 100

    return valor


def ganhar_experiencia(tamagotchi, experiencia):
    tamagotchi["experiencia"] += experiencia

    atualizar_nivel(tamagotchi)


def atualizar_nivel(tamagotchi):
    experiencia = tamagotchi["experiencia"]
    nivel_anterior = tamagotchi["nivel"]

    if experiencia >= 700:
        tamagotchi["nivel"] = 5

    elif experiencia >= 450:
        tamagotchi["nivel"] = 4

    elif experiencia >= 250:
        tamagotchi["nivel"] = 3

    elif experiencia >= 100:
        tamagotchi["nivel"] = 2

    else:
        tamagotchi["nivel"] = 1

    if tamagotchi["nivel"] > nivel_anterior:
        nome_nivel = NIVEIS[tamagotchi["nivel"]][0]

        print("\nEVOLUÇÃO!")
        print(f"{tamagotchi['nome']} evoluiu para {nome_nivel}!")


def alimentar(tamagotchi, alimento):
    nome, fome, felicidade, energia, experiencia = alimento

    tamagotchi["fome"] = limitar_atributo(
        tamagotchi["fome"] + fome
    )

    tamagotchi["felicidade"] = limitar_atributo(
        tamagotchi["felicidade"] + felicidade
    )

    tamagotchi["energia"] = limitar_atributo(
        tamagotchi["energia"] + energia
    )

    ganhar_experiencia(
        tamagotchi,
        experiencia
    )

    print(f"\nVocê deu {nome} para {tamagotchi['nome']}.")

    numero = random.randint(1, 100)

    if numero <= 30:
        tamagotchi["saude"] = limitar_atributo(
            tamagotchi["saude"] - 5
        )

        print("Parece que a comida não fez muito bem...")
        print("Saúde -5")


def brincar(tamagotchi, brincadeira):
    nome, felicidade, energia, fome, experiencia = brincadeira

    tamagotchi["felicidade"] = limitar_atributo(
        tamagotchi["felicidade"] + felicidade
    )

    tamagotchi["energia"] = limitar_atributo(
        tamagotchi["energia"] + energia
    )

    tamagotchi["fome"] = limitar_atributo(
        tamagotchi["fome"] + fome
    )

    ganhar_experiencia(
        tamagotchi,
        experiencia
    )

    print(f"\nVocê brincou com {tamagotchi['nome']} usando {nome}.")

    numero = random.randint(1, 100)

    if numero <= 25:
        tamagotchi["saude"] = limitar_atributo(
            tamagotchi["saude"] - 10
        )

        print(f"{tamagotchi['nome']} se machucou...")
        print("Saúde -10")


def dormir(tamagotchi):
    tamagotchi["energia"] = limitar_atributo(
        tamagotchi["energia"] + 45
    )

    tamagotchi["fome"] = limitar_atributo(
        tamagotchi["fome"] - 10
    )

    print(f"\n{tamagotchi['nome']} dormiu.")

    numero = random.randint(1, 100)

    if numero <= 20:
        tamagotchi["saude"] = limitar_atributo(
            tamagotchi["saude"] - 15
        )

        print(f"{tamagotchi['nome']} acordou doente...")
        print("Saúde -15")


def cuidar_da_saude(tamagotchi):
    tamagotchi["saude"] = limitar_atributo(
        tamagotchi["saude"] + 45
    )

    print(f"\n{tamagotchi['nome']} foi ao médico.")
    print("Saúde +45")


def mostrar_status(tamagotchi):
    nivel = tamagotchi["nivel"]

    if nivel == 0:
        nome_nivel = "Filhote"
        limite = 100
    else:
        nome_nivel, inicio, limite = NIVEIS[nivel]

    print("\n========== STATUS ==========")
    print(f"Nome: {tamagotchi['nome']}")
    print(f"Espécie: {tamagotchi['especie']['nome']}")
    print(f"Nível: {nivel} - {nome_nivel}")
    print(f"Experiência: {tamagotchi['experiencia']}/{limite}")
    print(f"Saúde: {tamagotchi['saude']}/100")
    print(f"Fome: {tamagotchi['fome']}/100")
    print(f"Felicidade: {tamagotchi['felicidade']}/100")
    print(f"Energia: {tamagotchi['energia']}/100")
    print("============================")
