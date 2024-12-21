'''#opcao 1
num1=input('Diz me um numero')
num1=int(num1)
print(num1)

#opcao 2
num1=int(input('Diz me um numero'))
print(num1)

#pergunta1 : perguntar à consola o que voces gostam 
#pergunta2 : perguntar à consola/python o que nao gostem
#print len(pergunta1)+len(pergunta2)
gostas=input('o que gostas: ')
nao_gostas=input('o que n gostas: ')
print('numero de letras total',len(gostas)+len(nao_gostas))'''

esta_chover=False

resposta=input('Esta a chover hoje.Responde com Y ou N ')
if resposta.lower()=='y':
    print('Esta a chover')
if resposta.lower()=='n':
    print('Nao esta a chover')

resposta=input('Esta a chover hoje.Responde com Y ou N ')
if resposta.upper()=='Y':
    print('Esta a chover')
if resposta.upper()=='N':
    print('Nao esta a chover')