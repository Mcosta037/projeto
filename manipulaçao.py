with open('manipulaçao.txt','w') as file4:
    file4.write('file\n')
with open('manipulaçao.txt','a') as arquivo:
    arquivo.write("linha 4\n")
with open('manipulaçao.txt','r') as file:

    manipulaçao = file.read()
    print(manipulaçao)

    manipulaçao2 = file.readline()
    print(manipulaçao2)

    manipulaçao3 = file.readline()
    print(manipulaçao3)

    manipulaçao4 = file.readlines()
    for linha in manipulaçao4:
        print(linha)
