import tkinter as tk
def teste():
    global Contador
    
    label.config(text=f"Contador: {contador}")
    
contador=0    

root = tk.Tk()
root.title("Aula2")

button = tk.Button(root,text = "Botão",command=teste)
button.pack(pady=100,padx=100)

button.place(x=200,y=50)
label =tk.Label(root,text="Label",font=("Arial", 25))
label.pack(padx=100,pady=100,)

root.mainloop()