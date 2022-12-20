import requests
from tkinter import *



janela=Tk()
janela.title("Aplicação CRUD")

text_empresa=Label(janela,text="Nome da Empresa")
text_empresa.grid(column=0,row=0)

botao_criar=Button(janela, text='Adicionar Produto')
botao_criar.grid(column=0,row=1)

botao_visuliazar=Button(janela, text='Visualizar Tabela')
botao_visuliazar.grid(column=0,row=2)

botao_atualizar=Button(janela, text='Atualizar Tabela')
botao_atualizar.grid(column=0,row=3)

botao_deletar=Button(janela, text='Deletar Produto')
botao_deletar.grid(column=0,row=4)

 
janela.mainloop()