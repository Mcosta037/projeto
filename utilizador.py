
initial_choice = input("se deseja criar um ficheiro pressione C,se não quer criar nada pressione h: ")
if initial_choice == "c":
        with open('file5.txt', 'w') as file5:
            file5.write("\n")
        while True:
            user_choice = input("se deseja adicionar alguma coisa e apagar o anterior pressione A, se deseja ler o que escreveu pressione r,se deseja escrever e apagar o que estava escrito antes pressione W, se deseja sair pressione L:")
        
            if user_choice == "a":
        
                n3 = input("o que deseja escrever:")

                with open('file5.txt', 'a') as arquivo:
                    arquivo.write(f"{n3}\n")
        
            elif user_choice == "r":

                with open('file5.txt', 'r') as arquivo:
                    print(arquivo.read())

            
            
            
            
            elif user_choice == "w":

                n4 = input("o que deseja escrever:")
                with open('file5.txt', 'w') as arquivo:
                    
                    arquivo.write(f"{n4}\n")
            elif user_choice == "l":
                print("voce saiu")
                break
            else:
                print("that is not an option")
elif initial_choice == "h":
        print("vá embora")
else:
    print("that is not an option")