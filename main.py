import customtkinter as ctk
import json
import os

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

def loadusu():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json","r") as arquivo:
            return json.load(arquivo)
    else:
        return []

def salvarusuarios(usuarios):
    with open("usuarios.json","w") as arquivo:
        json.dump(usuarios,arquivo, indent=4)


def veri01():
    usuario = entrusu.get()
    senha = entrpass.get()
    
    usuarios = loadusu()

    for user in usuarios:
        if user["usuario"] == usuario and user["senha"] == senha:
            return user["tipo"]
            
    return None


def veri02():
    if veri01():
        scr.destroy()
        #Janela Principal
        mainjnl = ctk.CTk()
        mainjnl.title("Página Principal")
        mainjnl.geometry("550x550")
        mainjnl.resizable(False,False)

        labelprinc = ctk.CTkLabel(mainjnl,text=f"Bem vindo",font=("Calibri",40),bg_color="#1b69cf",width=2000)
        labelprinc.pack(pady=10)

        label02 = ctk.CTkLabel(mainjnl,text="Este é o Seu Gerenciador",font=("Segoe UI",25),bg_color="#0e4082",width=2000)
        label02.pack(pady=5)

        mainjnl.mainloop()
    else:
        pass

def switchpass():
    if entrpass.cget('show') == '*':
        entrpass.configure(show='')
        mudarmodopassbtn.configure(text='Ocultar Senha')
    else:
        entrpass.configure(show='*')
        mudarmodopassbtn.configure(text='Mostrar Senha')


def funcriarconta():
    def criarcontaint():
        usuarios = loadusu()
    
        usuario  = criarcontausu.get()
        senha = criarcontapass.get()

        for user in usuarios:
            if user["usuario"] == usuario:
                return
        
        tipo = "comum"

        newuser = {
            "usuario": usuario,
            "senha":senha,
            "tipo":tipo
        }

        usuarios.append(newuser)

        salvarusuarios(usuarios)
        scrcreateaccont.destroy()

    scrcreateaccont = ctk.CTk()
    scrcreateaccont.title("Criar Conta")
    scrcreateaccont.geometry("300x150")
    scrcreateaccont.resizable(False,False)
    
    criarcontausu = ctk.CTkEntry(scrcreateaccont,placeholder_text="Usuário",width=200,font=("Consolas",17))
    criarcontausu.pack(pady=5)

    criarcontapass = ctk.CTkEntry(scrcreateaccont,placeholder_text="Senha",width=200,font=("Consolas",17))
    criarcontapass.pack(pady=5)

    btncriarconta = ctk.CTkButton(scrcreateaccont,text="Criar Conta",font=("Calibri",17),command=criarcontaint)
    btncriarconta.pack(pady=5)

    scrcreateaccont.mainloop()

scr = ctk.CTk()
scr.title("Login")
scr.geometry("300x300")
scr.resizable(False,False)

entrusu = ctk.CTkEntry(scr,font=("Consolas",16),placeholder_text="Usuário",width=200)
entrusu.pack(pady=5)

entrpass = ctk.CTkEntry(scr,show='*',font=("Consolas",16),placeholder_text="Senha",width=200)
entrpass.pack(pady=5)

mudarmodopassbtn = ctk.CTkButton(scr,text=("Mostrar Senha"),font=("Calibri",17),command=switchpass)
mudarmodopassbtn.pack(pady=5)

loginbtnobj = ctk.CTkButton(scr,text="Login",font=("Calibri",17),command=veri02)
loginbtnobj.pack(pady=5)

criarcontabtnobj = ctk.CTkButton(scr,text="Criar Conta",font=("Calibri",17),command=funcriarconta)
criarcontabtnobj.pack(pady=5)

scr.mainloop()