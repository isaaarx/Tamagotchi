from config import ESPECIES, ALIMENTOS, BRINCADEIRAS

from tamagotchi import (
    criar_tamagotchi,
    alimentar,
    brincar,
    dormir,
    cuidar_da_saude,
    mostrar_status
)

from reproducao import (
    pode_procriar,
    criar_filhote
)

from dados_teste import (
    criar_tamagotchis_teste
)


def pausar():
    input("\nPressione ENTER para continuar...")


def escolher_especie():
    print("\n===== ESCOLHA A ESPÉCIE =====")

    print("1 - Gato")
    print("2 - Cachorro")
    print("3 - Coelho")
    print("4 - Dragão")

    while True:
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            return ESPECIES[1]

        elif opcao == "2":
            return ESPECIES[2]

        elif opcao == "3":
            return ESPECIES[3]

        elif opcao == "4":
            return ESPECIES[4]

        else:
            print("Opção inválida.")


def menu_alimentar(tamagotchi):
    print("\n===== ALIMENTAR =====")

    for numero, alimento in ALIMENTOS.items():

        nome = alimento[0]
        fome = alimento[1]
        felicidade = alimento[2]
        energia = alimento[3]
        experiencia = alimento[4]

        print(
            f"{numero} - {nome} | "
            f"Fome {fome:+} | "
            f"Felicidade {felicidade:+} | "
            f"Energia {energia:+} | "
            f"Experiência {experiencia:+}"
        )

    print("7 - Voltar")

    while True:
        opcao = input("Escolha: ").strip()

        if opcao == "7":
            break

        elif opcao.isdigit() and 1 <= int(opcao) <= 6:

            numero = int(opcao)

            alimentar(
                tamagotchi,
                ALIMENTOS[numero]
            )

            pausar()
            break

        else:
            print("Opção inválida.")


def menu_brincar(tamagotchi):
    print("\n===== BRINCAR =====")

    for numero, brincadeira in BRINCADEIRAS.items():

        nome = brincadeira[0]
        felicidade = brincadeira[1]
        energia = brincadeira[2]
        fome = brincadeira[3]
        experiencia = brincadeira[4]

        print(
            f"{numero} - {nome} | "
            f"Felicidade {felicidade:+} | "
            f"Energia {energia:+} | "
            f"Fome {fome:+} | "
            f"Experiência {experiencia:+}"
        )

    print("6 - Voltar")

    while True:
        opcao = input("Escolha: ").strip()

        if opcao == "6":
            break

        elif opcao.isdigit() and 1 <= int(opcao) <= 5:

            numero = int(opcao)

            brincar(
                tamagotchi,
                BRINCADEIRAS[numero]
            )

            pausar()
            break

        else:
            print("Opção inválida.")


def menu_procriar(tamagotchi, tamagotchis):
    print("\n===== PROCRIAÇÃO =====")

    if not pode_procriar(tamagotchi):

        print(
            "\nEste Tamagotchi não pode procriar."
        )

        print("\nRequisitos:")
        print("- Nível 3 ou superior")
        print("- Saúde acima de 50")
        print("- Fome acima de 50")

        pausar()
        return

    outros = []

    for outro in tamagotchis:

        if outro is not tamagotchi:
            outros.append(outro)

    if len(outros) == 0:

        print(
            "\nNão existe outro Tamagotchi "
            "disponível."
        )

        pausar()
        return

    print(
        f"\nEscolha o parceiro "
        f"de {tamagotchi['nome']}:"
    )

    for numero, outro in enumerate(outros):

        print(
            f"{numero + 1} - "
            f"{outro['nome']} "
            f"({outro['especie']['nome']})"
        )

    while True:

        opcao = input(
            "\nEscolha o parceiro: "
        ).strip()

        if opcao.isdigit():

            numero = int(opcao)

            if 1 <= numero <= len(outros):

                parceiro = outros[numero - 1]

                break

        print("Opção inválida.")

    if not pode_procriar(parceiro):

        print(
            f"\n{parceiro['nome']} "
            "não pode procriar."
        )

        print("\nRequisitos:")
        print("- Nível 3 ou superior")
        print("- Saúde acima de 50")
        print("- Fome acima de 50")

        pausar()
        return

    print(
        f"\nPais escolhidos:"
    )

    print(
        f"{tamagotchi['nome']} "
        f"e {parceiro['nome']}"
    )

    nome = input(
        "\nDigite o nome do filhote: "
    ).strip()

    if nome == "":

        print(
            "O nome não pode ficar vazio."
        )

        pausar()
        return

    filhote = criar_filhote(
        tamagotchi,
        parceiro,
        nome
    )

    tamagotchis.append(filhote)

    print("\n🎉 FILHOTE NASCEU!")

    print(
        f"Nome: {filhote['nome']}"
    )

    print(
        f"Espécie: "
        f"{filhote['especie']['nome']}"
    )

    print(
        f"Saúde: "
        f"{filhote['saude']}"
    )

    print(
        f"Fome: "
        f"{filhote['fome']}"
    )

    print(
        f"Nível: "
        f"{filhote['nivel']}"
    )

    print(
        "\nO filhote foi adicionado "
        "aos Tamagotchis."
    )

    pausar()


def salvar_jogo(tamagotchi):
    print(
        f"\n{tamagotchi['nome']} foi salvo!"
    )

    print(
        "O jogo ficará salvo enquanto "
        "o programa estiver aberto."
    )

    pausar()


def menu_tamagotchi(tamagotchi, tamagotchis):

    while True:

        print("\n===== MENU DO TAMAGOTCHI =====")

        print("1 - Ver status")
        print("2 - Alimentar")
        print("3 - Brincar")
        print("4 - Dormir")
        print("5 - Cuidar da saúde")
        print("6 - Procriar")
        print("7 - Salvar Jogo")
        print("8 - Voltar ao menu inicial")
        print("9 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":

            mostrar_status(tamagotchi)
            pausar()

        elif opcao == "2":

            menu_alimentar(tamagotchi)

        elif opcao == "3":

            menu_brincar(tamagotchi)

        elif opcao == "4":

            dormir(tamagotchi)
            pausar()

        elif opcao == "5":

            cuidar_da_saude(tamagotchi)
            pausar()

        elif opcao == "6":

            menu_procriar(
                tamagotchi,
                tamagotchis
            )

        elif opcao == "7":

            salvar_jogo(tamagotchi)

        elif opcao == "8":

            return "voltar"

        elif opcao == "9":

            return "sair"

        else:

            print("Opção inválida.")
            pausar()


def novo_jogo(tamagotchis):

    print("\n========== NOVO JOGO ==========")

    nome = input("Nome: ").strip()

    if nome == "":

        print(
            "O nome não pode ficar vazio."
        )

        pausar()
        return

    especie = escolher_especie()

    tamagotchi = criar_tamagotchi(
        nome,
        especie
    )

    tamagotchis.append(tamagotchi)

    print(
        f"\n{nome} foi criado!"
    )

    pausar()

    return menu_tamagotchi(
        tamagotchi,
        tamagotchis
    )


def carregar_jogo(tamagotchis):

    if len(tamagotchis) == 0:

        print(
            "\nVocê ainda não possui "
            "Tamagotchis salvos."
        )

        pausar()
        return

    print("\n===== TAMAGOTCHIS =====")

    for numero, tamagotchi in enumerate(tamagotchis):

        print(
            f"{numero + 1} - "
            f"{tamagotchi['nome']} "
            f"({tamagotchi['especie']['nome']})"
        )

    print("0 - Voltar")

    while True:

        opcao = input(
            "Escolha: "
        ).strip()

        if opcao == "0":
            return

        if opcao.isdigit():

            numero = int(opcao)

            if 1 <= numero <= len(tamagotchis):

                resultado = menu_tamagotchi(
                    tamagotchis[numero - 1],
                    tamagotchis
                )

                return resultado

        print("Opção inválida.")

def menu_principal():

    tamagotchis = criar_tamagotchis_teste()

    while True:

        print("\n========== MENU INICIAL ==========")

        print("1 - Novo Jogo")
        print("2 - Carregar Jogo")
        print("3 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":

            resultado = novo_jogo(
                tamagotchis
            )

            if resultado == "sair":
                break

        elif opcao == "2":

            resultado = carregar_jogo(
                tamagotchis
            )

            if resultado == "sair":
                break

        elif opcao == "3":

            print(
                "\nJogo encerrado."
            )

            break

        else:

            print("Opção inválida.")
            pausar()
