from config import ESPECIES

def criar_tamagotchis_teste():
    luna = {
        "nome": "Luna",
        "especie": ESPECIES[1],
        "nivel": 3,
        "experiencia": 250,
        "saude": 80,
        "fome": 70,
        "felicidade": 75,
        "energia": 80
    }

    thor = {
        "nome": "Thor",
        "especie": ESPECIES[2],
        "nivel": 3,
        "experiencia": 250,
        "saude": 85,
        "fome": 80,
        "felicidade": 80,
        "energia": 90
    }

    return [luna, thor]
