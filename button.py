import tkinter as tk


root = tk.Tk()
def red():
    root.config(bg='red')

def black():
    root.config(background="black")

def green():
    root.config(background="green")

def blue():
    root.config(bg='blue')

button = tk.Button(root,text = "red",command=red)
button.place(x=200,y=50)


button = tk.Button(root,text = "blue",command=blue)
button.place(x=200,y=100)


button = tk.Button(root,text = "green",command=green)
button.place(x=250,y=50)


button = tk.Button(root,text = "black",command=black )
button.place(x=250,y=100)
button

label =tk.Label(root,text="Color Changer",font=("Arial", 25))
label.pack(padx=100,pady=100,)

root.mainloop()