from tkinter import *
from tkinter import messagebox

ficheiro_tarefas="files/tarefas.txt"

def contarTarefas(tree, numProvas):
    numProvas.set(len(tree.get_children()))

#Funçao ordenar por ordem alfabetica
def ordenarAlfabetica(tree):
    tree.delete(*tree.get_children())
    ficheiro = open(ficheiro_tarefas, "r")
    linhas = ficheiro.readlines()
    linhas.sort()
    for linha in linhas:
        tree.insert("", END, values=linha.split(";"))
    ficheiro.close()

#Funçao filtar por categorias

def filtrarCategorias(tree, categoria):
    tree.delete(*tree.get_children())
    ficheiro = open(ficheiro_tarefas, "r")
    linhas = ficheiro.readlines()
    for linha in linhas:
        if categoria in linha:
            tree.insert("", END, values=linha.split(";"))
    ficheiro.close()

    


