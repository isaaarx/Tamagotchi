TAMAGOTCHI EM PYTHON

Projeto de um jogo de Tamagotchi desenvolvido em Python, no qual o jogador cria e cuida de um animal virtual.

FUNCIONALIDADES

- Criar um novo Tamagotchi
- Escolher entre 4 especies: Gato, Cachorro, Coelho e Dragao
- Visualizar status
- Alimentar
- Brincar
- Dormir
- Cuidar da saude
- Procriar
- Ganhar experiencia
- Evoluir de nivel
- Salvar durante a execucao do programa
- Carregar os Tamagotchis disponiveis na sessao
- Voltar aos menus anteriores
- Encerrar o jogo


ESPECIES

Gato:
Fome: 70
Energia: 80
Saude: 80
Felicidade: 75

Cachorro:
Fome: 80
Energia: 90
Saude: 85
Felicidade: 80

Coelho:
Fome: 60
Energia: 70
Saude: 75
Felicidade: 90

Dragao:
Fome: 100
Energia: 100
Saude: 100
Felicidade: 60


SISTEMA DE NIVEIS

Nivel 1 - Filhote: 0 a 99 XP
Nivel 2 - Adolescente: 100 a 249 XP
Nivel 3 - Jovem: 250 a 449 XP
Nivel 4 - Adulto: 450 a 699 XP
Nivel 5 - Lendario: 700 a 1000 XP

A evolucao acontece automaticamente quando o Tamagotchi alcanca a experiencia necessaria.


ALIMENTACAO

Cenoura: Fome +10, Felicidade +5, Energia -5, Experiencia +10
Maca: Fome +5, Felicidade +5, Energia -5, Experiencia +10
Carne: Fome +25, Felicidade +5, Energia -5, Experiencia +10
Bolo: Fome +20, Felicidade +10, Energia -5, Experiencia +1
Pizza: Fome +30, Felicidade +10, Energia -5, Experiencia +10
Sorvete: Fome +10, Felicidade +10, Energia -5, Experiencia +10

Existe uma chance de 30% de o alimento fazer mal ao Tamagotchi, causando -5 de saude.


BRINCADEIRAS

Bola: Felicidade +15, Energia -15, Fome -10, Experiencia +15
Ursinho: Felicidade +10, Energia -5, Fome -5, Experiencia +15
Corda: Felicidade +20, Energia -15, Fome -10, Experiencia +15
Osso: Felicidade +15, Energia -10, Fome -5, Experiencia +15
Quebra-Cabeca: Felicidade +20, Energia -10, Fome -10, Experiencia +15

Existe uma chance de 25% de o Tamagotchi se machucar durante a brincadeira, causando -10 de saude.


DORMIR

Energia +45
Fome -10

Existe uma chance de 20% de o Tamagotchi ficar doente, causando -15 de saude.


CUIDAR DA SAUDE

Ao escolher a opcao de cuidar da saude, o Tamagotchi vai ao medico e recebe:

Saude +45


PROCRIACAO

Requisitos:
- O Tamagotchi precisa estar no nivel 3 ou superior.
- A saude precisa estar acima de 50.
- A fome precisa estar acima de 50.
- E necessario outro Tamagotchi que tambem atenda aos requisitos.

Caracteristicas do filhote:
- A especie e escolhida aleatoriamente entre as especies dos pais.
- A saude e definida aleatoriamente entre os valores de saude dos pais.
- O nivel comeca em 0.
- A experiencia comeca em 0.
- A fome comeca em 20.
- O nome e escolhido pelo jogador.


SALVAMENTO

O projeto utiliza um sistema de salvamento apenas durante a execucao do programa.

Os Tamagotchis permanecem disponiveis enquanto o programa estiver aberto. Ao encerrar o programa, os dados sao perdidos.


ESTRUTURA DO PROJETO

tamagotchi/
|
|-- main.py
|-- config.py
|-- tamagotchi.py
|-- reproducao.py
|-- dados_teste.py
|-- menus.py


ARQUIVOS

main.py
Arquivo responsavel por iniciar o jogo.

config.py
Armazena as configuracoes do jogo:
- Especies
- Alimentos
- Brincadeiras
- Niveis

tamagotchi.py
Contem as principais funcoes do Tamagotchi:
- Criacao
- Alimentacao
- Brincadeiras
- Sono
- Saude
- Experiencia
- Evolucao
- Status

reproducao.py
Contem as regras relacionadas a procriacao e criacao dos filhotes.

dados_teste.py
Contem dois Tamagotchis preparados para testar e demonstrar a funcionalidade de procriacao:
- Luna
- Thor

menus.py
Responsavel pelos menus e pela interacao com o jogador.


TECNOLOGIAS UTILIZADAS

- Python 3
- Estruturas condicionais
- Estruturas de repeticao
- Listas
- Dicionarios
- Tuplas
- Funcoes
- Modulos
- Tratamento de entradas
- Numeros aleatorios com random


COMO EXECUTAR

1. Clone o projeto:

git clone URL_DO_REPOSITORIO

2. Entre na pasta:

cd tamagotchi

3. Execute o programa:

python main.py


TAMAGOTCHIS PARA TESTE

O projeto ja inicia com dois Tamagotchis preparados para testar a procriacao.

Luna:
Especie: Gato
Nivel: 3
Experiencia: 250
Saude: 80
Fome: 70

Thor:
Especie: Cachorro
Nivel: 3
Experiencia: 250
Saude: 85
Fome: 80

Os dois atendem aos requisitos necessarios para realizar a procriacao.
