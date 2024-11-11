import customtkinter as ctk

typeusuoutfunc = 0

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

def veri01():
    usuario_input = entrusu.get()
    senha_input = entrpass.get()
    if usuario_input != "" or senha_input != "":
        try:
            with open('usuarios.txt','r') as arquivo_usuarios,\
                 open('senhas.txt','r') as arquivos_senhas,\
                 open('admin.txt','r') as arquivo_permissões:
                usuarios = arquivo_usuarios.readlines()
                senhas = arquivos_senhas.readlines()
                typeusu = arquivo_permissões.readlines()

                if len(usuarios) != len(senhas) or len(usuarios) != len(typeusu):
                    return False, None

                for i in range(len(usuarios)):
                    usuario = usuarios[i].strip()
                    senha = senhas[i].strip()

                    if usuario == usuario_input and senha == senha_input:
                        return True, typeusu
                        
            return False
        except FileNotFoundError:
            return False
    veri_typeusu(typeusuoutfunc)

def veri_typeusu(typeusuvarinfunc):
    autentic, permissao = veri01()
    if autentic:
        if permissao == 'admin':
            typeusuvarinfunc = 1
        else:
            typeusuvarinfunc = 0

def veri02():
    if veri01():
        scr.destroy()
        #Janela Principal
        mainjnl = ctk.CTk()
        mainjnl.title("Página Principal")
        mainjnl.geometry("500x500")
        mainjnl.resizable(False,False)

        mainjnl.mainloop()

def switchpass():
    if entrpass.cget('show') == '*':
        entrpass.configure(show='')
        mudarmodopassbtn.configure(text='Ocultar Senha')
    else:
        entrpass.configure(show='*')
        mudarmodopassbtn.configure(text='Mostrar Senha')

def funcriarconta():
    def criarcontaint():
        usuario = criarcontausu.get()
        senha = criarcontapass.get()
        
        if usuario != "" or senha != "":
            with open("usuarios.txt","r") as arquivo_usuarios:
                for linha in arquivo_usuarios:
                    usuario_existente = linha.strip()
                    if usuario == usuario_existente:
                        return
        
            with open('usuarios.txt',"a") as arquivo_usuarios,\
                 open('senhas.txt','a') as arquivo_senhas,\
                 open('admin.txt','a') as arquivo_permissoes:
                arquivo_usuarios.write(f"\n{usuario}")
                arquivo_senhas.write(f"\n{senha}")
                arquivo_permissoes.write(f"\nusuario")
            scrcreateaccont.destroy()
        
        else:
            pass

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