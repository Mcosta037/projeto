from tkinter import *
from tkinter import messagebox
window = Tk()
window.title('agenda')
window.geometry('920x600')
window.wm_resizable(width=False,height=False)

label = Label(window, text='Agenda', font=('Arial', 20))
label.place(x=400, y=20)

label = Label(window, text='Nome:')
label.place(x=40, y=120)
input_nome = Entry(window)
input_nome.place(width=500, height=20, x=100, y=120)

label = Label(window, text='Telefone:')
label.place(x=40, y=160)
input_telefone = Entry(window)
input_telefone.place(width=500, height=20, x=100, y=160)

label = Label(window, text='Email:')
label.place(x=40, y=200)
input_email = Entry(window)
input_email.place(width=500, height=20, x=100, y=200)

label = Label(window, text='Endereço:')
label.place(x=40, y=240)
input_endereco = Entry(window)
input_endereco.place(width=500, height=20, x=100, y=240)

label = Label(window, text='Distrito:')
label.place(x=40, y=280)
input_distrito = Entry(window)
input_distrito.place(width=500, height=20, x=100, y=280)

label = Label(window, text='Pais:')
label.place(x=580, y=280)
input_pais = Entry(window)
input_pais.place(width=500, height=20, x=620, y=280)




def adicionar():
 nome =input_nome.get()
 tel = input_telefone.get()
 email = input_email.get()
 end = input_endereco.get()
 dist = input_distrito.get()
 pais = input_pais.get()
with open ('agenda.txt', 'a') as arquivo:
    arquivo.write(nome + '\n' + tel + '\n' + email + '\n' + end + '\n' + dist + '\n' + pais + '\n')
messagebox.showinfo("Agenda", "contacto adicionado com sucesso")