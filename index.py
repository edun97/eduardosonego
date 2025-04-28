# Importar bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Criar Nossa Janela
jan = Tk()
jan.title("Brasiliense Odontologia")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)

#====== Carregando Imagens
Logo = PhotoImage(file="icons/logo.png")

#====== Widgtes ====================
LeftFrame = Frame(jan, width=200, height=300, bg="#800000", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="#800000", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=Logo, bg="#800000")
LogoLabel.place(x=0, y=100)

UserLabel = Label(RightFrame, text="Nome de Usuário:", font=("Times New Roman", 12), bg="#800000", fg="white")
UserLabel.place(x=1, y=50)

UserEntry = ttk.Entry(RightFrame, width=20)
UserEntry.place(x=120, y=53)

jan.mainloop()