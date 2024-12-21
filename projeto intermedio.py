#jogo da forca
from time import sleep
from random import randint
letras =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nomes_animais=["tubarao","gato","hipopotamo","raposa","flamingo","lobo","rato",]
nomes_jogos=["fallout","valorant","minecraft","roblox","brawlstars","fortnite","cuphead","counter strike global offensive"]
nomes_filmes=["Starwars","Harry Potter","Amazing Spiderman","BadBoys","",""]

print("Bem-vindo ao Jogo da Forca")
n1=1
n2=2
n3=int(input("Deseja jogar pressione 1 se quer jogar, pressione 2 para sair:",))
if n3 == 2:
    print("vai-te embora")
elif n3<1:
    print("não é uma opção")
elif n3>2:
    print("não é uma opção")
else:
    print("que letra deseja introduzir {letras}")
