from tkinter import *
import tkinter as tk
from .functions_view.functions import Diretorios


class HeaderView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Definições dos frames
        self.frame_header = Frame(self,height=90,width=1500, background="#000000")
        self.frame_menu = Frame(self,height=50,width=1500)
        self.frame_header_menu = tk.Canvas(self, height=80,width=1500, background="white")
        self.frame_menuoptions = Frame(self,height=50,width=1500, background="#8A8A8A")
        self.frame_content = Frame(self,height=770,width=1500, background="white")

        self.frame_header.grid(column=0,row=0,ipadx=0,ipady=0,padx=0,pady=0,sticky="we")
        self.frame_menu.grid(column=0,row=1,ipadx=0,ipady=0,padx=0,pady=0,sticky="news")
        self.frame_header_menu.grid(column=0,row=2,ipadx=0,ipady=0,padx=0,pady=0,sticky="news")
        self.frame_menuoptions.grid(column=0,row=3,ipadx=0,ipady=0,padx=0,pady=0,sticky="news")
        self.frame_content.grid(column=0,row=4,ipadx=0,ipady=0,padx=10,pady=0,sticky="news")

        #widgets frame_header

        self.btn_home = Button(self.frame_header, image=Diretorios('home.png').img, bg='#000000', bd=0, font=('arial 12 bold'), cursor='hand2', height=90,width=50)
        self.btn_home.grid(column=0,row=0, padx=10)
        
        #widgets frame_menu

        # Configuração de peso para as colunas do frame_menu:
        # Para cada coluna (representada por 'col' no loop),
        # define o peso como 1, permitindo que as colunas se expandam
        # uniformemente ao redimensionar a janela.
        for col in range(7):
            self.frame_menu.columnconfigure(col, weight=1)

        
        self.btn_clientes = Button(self.frame_menu, text='Clientes', image=Diretorios('cliente.png').img, compound=LEFT, bg='#ADADAD', bd=0, font=('arial 12 bold'), cursor='hand2', height=50,width=29) #, command=self.cliente
        self.btn_clientes.grid(column=0,row=0,sticky='ew')

        
        self.btn_venda = Button(self.frame_menu, text='Vendas', image=Diretorios('vendas.png').img, compound=LEFT, bg='#ADADAD', bd=0, font=('arial 12 bold'), cursor='hand2', height=50,width=29) #, command=self.venda
        self.btn_venda.grid(column=1,row=0,sticky='ew')


        self.btn_fornecedor = Button(self.frame_menu, text='Fornecedor', image=Diretorios('fornecedor.png').img, compound=LEFT, bg='#ADADAD', bd=0, font=('arial 12 bold'), cursor='hand2', height=50,width=29) #, command=self.fornecedor
        self.btn_fornecedor.grid(column=2,row=0,sticky='ew')

        
        self.btn_estoque = Button(self.frame_menu, text='Estoque', image=Diretorios('estoque.png').img, compound=LEFT, bg='#ADADAD', bd=0, font=('arial 12 bold'), cursor='hand2', height=50,width=29) #, command=self.estoque
        self.btn_estoque.grid(column=3,row=0,sticky='ew')

        
        self.btn_compra = Button(self.frame_menu, text='Compras', image=Diretorios('compras.png').img, compound=LEFT, bg='#ADADAD', bd=0, font=('arial 12 bold'), cursor='hand2', height=50,width=29)
        self.btn_compra.grid(column=4,row=0,sticky='ew')

        
        self.btn_financeiro = Button(self.frame_menu, text='Financeiro', image=Diretorios('financeiro.png').img, compound=LEFT, bg='#ADADAD', bd=0, font=('arial 12 bold'), cursor='hand2', height=50,width=29)
        self.btn_financeiro.grid(column=5,row=0,sticky='ew')

        
        self.btn_troca = Button(self.frame_menu, text='Trocas', image=Diretorios('troca.png').img, compound=LEFT, bg='#ADADAD', bd=0, font=('arial 12 bold'), cursor='hand2',height=50,width=29)
        self.btn_troca.grid(column=6,row=0,sticky='ew')