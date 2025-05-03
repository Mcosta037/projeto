import tkinter as tk
def teste():
    global Hello_World
    
    label.config(text=f"Hello world")
def test():
    label.config(text=f"")

root = tk.Tk()
root.title("Aula2")

button = tk.Button(root,text = "Aparecer",command=teste)
button.pack(pady=100,padx=100)

button.place(x=200,y=70)

button = tk.Button(root,text = "Desaparecer",command=test)
button.place(x=200,y=50)

label =tk.Label(root,text="Label",font=("Arial", 25))
label.pack(padx=100,pady=100,)

root.mainloop()