import tkinter as tk
from tkinter import messagebox

root =tk.Tk()
root.title("Jogo do Galo")

def clica_botao(index):
    global board, buttons, jogadores_atual
    if board[index] == '':
        board[index] = jogador_atual
        buttons[index].config(text = jogador_atual)

    if verifica_vencedor():
        messagebox.showinfo("Game Over",f"Jogador {jogador_atual} Venceu")
        reset()
    elif '' not in board:
        messagebox.showinfo("Fim de Jogo","Empate!")
    else:
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'


def verifica_vencedor():
    combinaçoes = [
        [0,1,2], [3,4,5], [6,7,8],#LINHAS
        [0,3,6], [1,4,7], [2,5,8],#COLUNAS
        [0,4,8], [2,4,6]          #DIAGONAIS
    ]

    for comb in combinaçoes:
        if board[comb[0]] == board[comb[1]] == board[comb[2]] != '':
            return True
        return False    

def reset():
    global board, jogador_atual, buttons
    board =['' for _ in range(9) ]
    for button in buttons:
        button.config(text='')
    jogador_atual ="X"

jogador_atual ="X"
board =['' for _ in range(9) ]
buttons = []

for i in range(9):
    button = tk.Button(root,text="",width=5,height=2)
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

root.mainloop()