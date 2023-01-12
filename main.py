# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import ttk          # extensão do tkinter, inclui treeview
from tkinter import filedialog   # filedialog boxes
from PIL import ImageTk,Image    # Imagens .jpg ou .png
from tkinter import messagebox   #  messagebox
from tkinter.ttk import Combobox # combo
from utilizadores import *
from tarefas import *


def containerGerirTarefas():
    panelTarefas = PanedWindow(window, width = 750, height= 450)
    panelTarefas.place(x=250, y= 50)

    lblTarefa = Label(panelTarefas, text = "Tarefa")
    lblTarefa.place(x=30, y=70)

    tarefa = StringVar()
    entryTarefa = Entry(panelTarefas, width=25, textvariable=tarefa)
    entryTarefa.place(x=80, y= 70) 

    lblData = Label(panelTarefas, text = "Data")
    lblData.place(x=30, y=120)

    data = StringVar()
    entryData = Entry(panelTarefas, width=25, textvariable=data)
    entryData.place(x=80, y= 120) 

    lblCategoria = Label(panelTarefas, text = "Categoria")
    lblCategoria.place(x=30, y=170)


   #Como fazer uma combobox com categorias
    CategoriaTarefa = StringVar()
    CategoriaTarefa.set("Atividade Pessoal")
    combos=['Atividade pessoal', 'Trabalhos', 'Escola', 'Ferias', 'Tempo livre', 'Desporto', 'Familia']
    comboExample = ttk.Combobox(panelTarefas, values=combos)
    comboExample.place(x=100, y=170)

    lblEstado= Label(panelTarefas, text = "Estado")
    lblEstado.place(x=30, y=340)

    EstadoTarefa = StringVar()
    EstadoTarefa.set("Por Iniciar")
    rd1 = Radiobutton(panelTarefas, text = "Por Iniciar", value = "Por Iniciar", variable= EstadoTarefa)
    rd2 = Radiobutton(panelTarefas, text = "Em Progresso", value = "Em Progresso", variable= EstadoTarefa)
    rd3 = Radiobutton(panelTarefas, text = "Concluída", value = "Concluída", variable= EstadoTarefa)
    rd1.place(x= 87, y= 340)
    rd2.place(x= 87, y= 370)
    rd3.place(x= 87, y= 400)

    tview = ttk.Treeview(panelTarefas, height=10,  selectmode= "browse", 
            columns = ("Tarefa", "Data", "Categoria", "Estado"), show = "headings")
    
    tview.column("Tarefa", width = 100,   anchor="c")
    tview.column("Data", width = 100,  anchor="c")          # c- center
    tview.column("Categoria", width = 100,   anchor="c")
    tview.column("Estado", width = 140,   anchor="c")
    tview.heading("Tarefa", text = "Tarefa")
    tview.heading("Data", text = "Data")
    tview.heading("Categoria", text = "Categoria")
    tview.heading("Estado", text = "Estado")
    tview.place(x=280, y=70)

   

    listaTarefas= lerTarefas()
    refreshListboxTarefas(listaTarefas, tview)

    global imageAdd, imageRemove
    imageAdd = PhotoImage(file = "imagens\\plus.png" )
    btnAdicionar = Button(panelTarefas, width=20, height=15, text = "Adicionar Tarefa", compound=LEFT,
                command= lambda: adicionarTarefa(tarefa.get(), data.get(), CategoriaTarefa.get(), EstadoTarefa.get(), tview))
    btnAdicionar.place(x=280, y= 320)
    
    imageRemove = PhotoImage(file = "imagens\\remover.png" )
    btnApagar = Button(panelTarefas, width=20, height=15,  text = "Apagar Tarefa", compound=LEFT,
                command= lambda: apagarTarefa(tview))
    btnApagar.place(x=510, y= 320)


def panelAutenticarUser():
#Painel de autenticação

   if userAutenticado.get() != "":     # SE JÁ EXISTE um user autenticado, a ieia é terminar sessão
        userAutenticado.set("")
        btnLogin.config(text = "Iniciar Sessão")
        return
   panelUsers = PanedWindow(window, width = 550, height = 300, relief = "sunken")
   panelUsers.place(x=450, y=100)    # 450, 50
 
# Imagem
   containerImage = Canvas(panelUsers, height = 128, width=128)
   containerImage.place(x=50, y=70) 
   global img
   img = PhotoImage(file = ".\imagens\\entrar.png")
   containerImage.create_image(64, 64, image = img)
  # Username
   labelUsers = Label(panelUsers, text ="Username:")
   labelUsers.place(x=200, y= 100)
   userName = StringVar()
   txtUser = Entry(panelUsers, width=20, textvariable=userName)
   txtUser.place(x=280, y= 100)
#Password
   labelPass = Label(panelUsers, text ="Password:")
   labelPass.place(x=200, y= 150)
   userPass = StringVar()
   txtPass = Entry(panelUsers, width=20, textvariable = userPass, show = "*")
   txtPass.place(x=280, y= 150)

   btnValidar= Button(panelUsers, text = "Validar Conta", width=25, height=3,
                      command = lambda: autenticarUser(userName.get(), userPass.get(), panelUsers))
   btnValidar.place(x=260, y= 200) 
   




def autenticarUser(userName, userPass, panelUsers):
   global userAutenticado
   userAutenticado.set(validaConta(userName, userPass))
   if userAutenticado.get() != "":
      btnLogin.config(text = "Terminar Sessão")
      panelUsers.place_forget()
      containerCasa()



def panelCriarConta():
   panelUsers = PanedWindow(window, width = 550, height = 300, relief = "sunken")
   panelUsers.place(x=450, y=100)
   # Imagem
   containerImage = Canvas(panelUsers, height = 128, width=128)
   containerImage.place(x=50, y=70) 
   global img
   img = PhotoImage(file = ".\imagens\\criar_conta.png")
   containerImage.create_image(64, 64, image = img)
# Username
   labelUsers = Label(panelUsers, text ="Username:")
   labelUsers.place(x=200, y= 50)
   userName = StringVar()
   txtUser = Entry(panelUsers, width=20, textvariable=userName)
   txtUser.place(x=280, y= 50)
#Password
   labelPass = Label(panelUsers, text ="Password:")
   labelPass.place(x=200, y= 100)
   userPass = StringVar()
   txtPass = Entry(panelUsers, width=20, textvariable = userPass, show = "*")
   txtPass.place(x=280, y= 100)
#Password
   labelPass = Label(panelUsers, text ="Confirmar \nPassword:")
   labelPass.place(x=200, y= 150)
   userPassConfirm = StringVar()
   txtPass = Entry(panelUsers, width=20, textvariable = userPassConfirm, show = "*")
   txtPass.place(x=280, y= 150)

   btnValidar= Button(panelUsers, text = "Criar Conta", width=25, height=3,
                      command = lambda: criaConta(userName.get(), userPass.get(), userPassConfirm.get(), panelUsers))
   btnValidar.place(x=260, y= 200) 



def containerCasa():
   #-- Painel com opções de menu
   panel2 = PanedWindow(window, width=750, height=450)
   panel2.place(x=250, y=50)
   #------------- Imagem de entrada da App
   ctnCanvas = Canvas(panel2, width = 750, height= 450)
   ctnCanvas.place(x=0, y= 0)
   global img
   img = PhotoImage(file = "imagens\\fundo1.png")
   ctnCanvas.create_image(750, 400, image = img)




window = Tk()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1000                             # tamanho (pixeis) da window a criar 900 / 500
appHeight = 500 
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.title('To Do List App')

#-- Painel com opções de menu
panel1 = PanedWindow(window, bg = "orange", width=250, height=500)
panel1.place(x=0, y=0)

imageCasa = PhotoImage(file = "imagens\\casa1.png" )
btnCasa = Button(panel1, text = "Início", image = imageCasa, compound=LEFT, relief = "sunken", 
                    width = 230, height = 68, font="calibri, 11",
                    command=containerCasa)
btnCasa.place (x=5, y=50)

imageGerir = PhotoImage(file = "imagens\\gerir_tarefas1.png" )
btnGerir = Button(panel1, text = "Gerir \nTarefas", image = imageGerir, compound=LEFT, relief = "sunken", 
                    width = 230, height = 68, font="calibri, 11",
                    command=containerGerirTarefas)
btnGerir.place (x=5, y=130)

imageSair = PhotoImage(file = "imagens\\sair1.png" )
btnSair = Button(panel1, text = "Sair \nda App", relief = "sunken", image = imageSair, compound=LEFT,
                width = 230, height = 68,  font="calibri, 11", 
                command = window.destroy)
btnSair.place (x=5, y=370)

global userAutenticado
userAutenticado = StringVar()
userAutenticado.set("")
labelHeader = Label(window, textvariable= userAutenticado, fg = "black", font="calibri, 11")
labelHeader.place(x= 300, y= 10)

imageLogin = PhotoImage(file = "imagens\\entrar1.png" )
btnLogin = Button (window, image = imageLogin, relief = "flat",  compound=TOP,
                     width = 78, height=38, text = "Login", command = panelAutenticarUser)
btnLogin.place(x=790, y=5)

imageCriarConta = PhotoImage(file = "imagens\\criar_conta1.png" )
btnCriarConta = Button (window, image = imageCriarConta, width = 64, height=38, relief="flat", text = "Criar Conta",
                  compound = TOP, command=panelCriarConta)
btnCriarConta.place(x=890, y=5)

containerCasa()


window.mainloop()