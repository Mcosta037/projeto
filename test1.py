# jogo da forca
from re import search
from time import sleep
import random

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z"]
nomes_animais = ["tubarao", "gato", "hipopotamo", "raposa", "flamingo", "lobo", "rato"]
nomes_jogos = ["fallout", "valorant", "minecraft", "roblox", "brawlstars", "fortnite", "cuphead"]
nomes_filmes = ["Starwars", "Spiderman", "BadBoys"]

print("Bem-vindo ao Jogo da Forca")
n3 = int(input("Deseja jogar pressione 1 se quer jogar, pressione 2 para sair:", ))
if n3 == 2:
    print("Vai-te embora")
elif n3 < 1:
    print("Não é uma opção")
elif n3 > 2:
    print("Não é uma opção")
else:
    print("Vamos jogar.")
n4 = int(input(
    "Que tema deseja jogar ,se deseja jogar sobre jogos pressione 1,se deseja jogar sobre filmes pressione 2,se deseja jogar sobre animais pressione 3:", ))

if n4 == 1:
    jogos=random.randint(0,6)

    print(nomes_jogos[jogos])

elif n4 ==2:
    animais = random.randint(0, 2)

    print(nomes_animais[animais])