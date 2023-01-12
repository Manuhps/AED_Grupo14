# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import messagebox
from tkinter import ttk          # extensão do tkinter, inclui treeview

fTarefas= "files/tarefas.txt"


def adicionarTarefa(tarefa, data, local, tipoTarefa, tview):
    fileTarefas=open(fTarefas, "a", encoding="utf-8")
    linha = tarefa + ";" + data + ";" + local + ";" + tipoTarefa + "\n" 
    fileTarefas.write(linha)
    fileTarefas.close()
    
    lista = lerTarefas()
    refreshListboxTarefas(lista, tview)
  
def apagarTarefa(tview):    
    tview.delete(tview.selection())

    fileTarefas=open(fTarefas, "w", encoding="utf-8")
    for line in tview.get_children():
           atividade = tview.item(line)["values"][0] + ";" + tview.item(line)["values"][1] + ";"+ tview.item(line)["values"][2] + ";" + tview.item(line)["values"][3]
           fileTarefas.write(atividade)         # Guarda em ficheiro
    fileTarefas.close()

    lista = lerTarefas()
    refreshListboxTarefas(lista, tview)


def lerTarefas():
    fileTarefas=open(fTarefas, "r", encoding="utf-8")
    lista = fileTarefas.readlines()
    fileTarefas.close()
    return lista


def refreshListboxTarefas(listaTarefas, tview):
    tview.delete(*tview.get_children())
    for item in listaTarefas:
        tview.insert("", "end", values = (item.split(";")[0],item.split(";")[1], item.split(";")[2], item.split(";")[3] ))