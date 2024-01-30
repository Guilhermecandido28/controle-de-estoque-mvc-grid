from tkinter import constants
import tkinter as tk
from tkinter import ttk
from .header import HeaderView
from .functions_view.functions import OndeEstou

class ClienteHomeView(HeaderView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #widgets frame_header_menu

        self.titulo = OndeEstou(self.frame_header_menu, 'VENDAS', 'location.png')
        self.titulo.localizador()

        #widgets frame_menuoptions

        self.frame_menuoptions.rowconfigure(0, weight=1)
        self.frame_menuoptions.columnconfigure(0, weight=10)
        self.frame_menuoptions.columnconfigure(1, weight=1)
        self.frame_menuoptions.columnconfigure(2, weight=1)
        self.frame_menuoptions.columnconfigure(3, weight=1)
        self.frame_menuoptions.columnconfigure(4, weight=1)
        self.frame_menuoptions.columnconfigure(5, weight=1)


        self.entry_pesquisa = tk.Entry(self.frame_menuoptions, font=('arial 14'), bg="#8A8A8A", bd=0,width=29)
        self.entry_pesquisa.grid(column=0,row=0,sticky='ew',padx=10)
        self.entry_pesquisa.insert(0, "Procure por cliente...")

        #Botao pesquisa
        self.btn_search = tk.Button(self.frame_menuoptions, text='search', bg="#8A8A8A", bd=0, cursor='hand2',font=('arial 14 bold'),height=3,width= 8)
        self.btn_search.grid(column=1,row=0,sticky='news')

        #Botão imprimir
        self.btn_print = tk.Button(self.frame_menuoptions,text='print',bg="#8A8A8A", bd=0, cursor='hand2',font=('arial 14 bold'),width= 8)
        self.btn_print.grid(column=2,row=0,sticky='news')

        #excluir cliente        
        self.btn_exclcliente = tk.Button(self.frame_menuoptions, text='EXCLUIR\n Cliente', bg='gray', compound='center',bd=0, font=('arial 14 bold'), foreground='black', cursor='hand2',width= 8)
        self.btn_exclcliente.grid(column=3,row=0,sticky='news')

        #botão de editar cliente
        self.btn_edtcliente = tk.Button(self.frame_menuoptions, text='EDITAR\n Cliente', bg='dark gray', compound='center',bd=0, font=('arial 14 bold'), foreground='black', cursor='hand2',width= 8)
        self.btn_edtcliente.grid(column=4,row=0,sticky='news')

        #Botão_adicionar_cliente        
        self.btn_addcliente = tk.Button(self.frame_menuoptions, text='ADICIONAR\n Cliente', bg='light gray', compound='center',bd=0, font=('arial 14 bold'), foreground='black', cursor='hand2',width= 8)
        self.btn_addcliente.grid(column=5,row=0,sticky='news')



     



        