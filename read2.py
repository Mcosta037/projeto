with open('exemplo.txt','r') as file:
    conteudo = file.readline()
    print(conteudo)

    conteudo2 = file.readline()
    print(conteudo2)

    conteudo3 = file.readline()
    print(conteudo3)

    conteudo4 = file.readlines()
    for linha in conteudo4:
        print(linha)