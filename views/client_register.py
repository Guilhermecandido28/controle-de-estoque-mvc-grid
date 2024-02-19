from tkinter import CENTER, W, LEFT, PhotoImage, Button, Canvas, Entry, Label, Scrollbar, constants, Frame
import tkinter as tk
from tkinter import ttk
from .header import HeaderView
from controllers.helpers.functions import OndeEstou, Diretorios

class ClienteRegisterView(HeaderView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)	

        #widgets frame_header_menu

        self.titulo = OndeEstou(self.frame_header_menu, 'CLIENTES', 'location.png')
        self.titulo.localizador()
        self.frame_menuoptions.grid_forget()
        #Configuração para permitir expandir linha 
        self.frame_content.rowconfigure(0, weight=1)
        #Configuração para permitir expandir a coluna frame_content_form
        self.frame_content.columnconfigure(0, weight=1)
        #Configuração para permitir expandir a coluna frame_content_table
        self.frame_content.columnconfigure(1, weight=1)
        
        #Criação dos frames
        self.frame_menu.config(bg='red')
        self.frame_content_form = tk.Frame(self.frame_content,height=770, width=1500, background="white")
        self.frame_content_form.grid(column=0,row=0,sticky="news");
        
        self.frame_content_form.columnconfigure(2,weight=1)

        self.frame_content_table = tk.Frame(self.frame_content)
        self.frame_content_table.grid(column=1,row=0,sticky="news");
        
        self.frame_content_table.columnconfigure(0,weight=1)
        self.frame_content_table.rowconfigure(1,weight=1)

        #título 
        self.titulo = Label(
            self.frame_content_form,
            text='Ficha de Cadastro de Clientes',
            bg='white',
            font=('arial 36 bold'))
        self.titulo.place(relx=0.146, rely=0.07, relheight=0.1)

        Frame(
            self.frame_content_form,
            bg='#5f5f5f'
            ).place(relx=0.146, rely=0.17, relwidth=0.525, relheight=0.004)
        
        #imagem
        self.my_canvas = Canvas(
            self.frame_content_form,
            bd=0,
            highlightthickness=0,
            relief='ridge')
        self.my_canvas.place(relx=0, rely=0.1, relheight=.34, relwidth=.14)
        
               
        self.botao_upload = tk.Button(
            self.frame_content_form,            
            text="Upload",
            font=('arial 12 bold'),
            background='green',
            foreground='white',
            cursor='hand2')  #command= self.upload,      
        self.botao_upload.place(relx=0, rely=0.44, relwidth=.14, relheight=0.04)

        self.botao_upload_instagram = tk.Button(
            self.frame_content_form,
            
            text="Mostre foto perfil instagram ",
            font=('arial 12 bold'),
            background='green',
            foreground='white',
            cursor='hand2')#command= self.upload_instagram,
        self.botao_upload_instagram.place(relx=0.49, rely=0.38, relwidth=.18, relheight=0.04)

        # Entrys
            #nome
        self.title_nome = Label(
            self.frame_content_form,
            text='NOME:',
            font=('arial 12'),
            foreground= '#ADADAD',
            bg='white')
        self.title_nome.place(relx=0.148, rely=0.195)

        self.e_nome = Entry(
            self.frame_content_form,
            bg='#ADADAD',
            font=('arial 12'),
            bd=0)
        self.e_nome.place(relx=0.150, rely=0.24, relwidth=0.25, relheight=0.04)
        #placeholder_nome(self.e_nome)
        
            #sobrenome
        self.title_sobrenome = Label(self.frame_content_form, text='SOBRENOME:', font=('arial 12'), foreground= '#ADADAD', bg='white')
        self.title_sobrenome.place(relx=0.416, rely=0.195)
        self.e_sobrenome = Entry(self.frame_content_form, bg='#ADADAD', font=('arial 12'), bd=0)
        self.e_sobrenome.place(relx=0.42, rely=0.24, relwidth=0.25, relheight=0.04)
        #placeholder_sobrenome(self.e_sobrenome)
            #CPF
        self.title_cpf = Label(self.frame_content_form, text='CPF:', font=('arial 12'), foreground= '#ADADAD', bg='white')
        self.title_cpf.place(relx=0.148, rely=0.295)
        self.e_cpf = Entry(self.frame_content_form, bg='#ADADAD', font=('arial 12'), bd=0)
        self.e_cpf.place(relx=0.150, rely=0.34, relwidth=0.15, relheight=0.04)
        #placeholder_cpf(self.e_cpf)
            #celular
        self.title_celular = Label(self.frame_content_form, text="CELULAR:", font=('arial 12'), foreground='#ADADAD', bg='white')
        self.title_celular.place(relx= 0.316 , rely=0.295)
        self.e_celular = Entry(self.frame_content_form, bg='#ADADAD', font=('arial 12'), bd=0)
        self.e_celular.place(relx=0.32, rely=0.34, relwidth=0.15, relheight=0.04)
        #placeholder_celular(self.e_celular)
            #email
        self.title_instagram = Label(self.frame_content_form, text="INSTAGRAM:", font=('arial 12'), foreground='#ADADAD', bg='white')
        self.title_instagram.place(relx= 0.49 , rely=0.295) 
        self.e_instagram = Entry(self.frame_content_form, bg='#ADADAD', font=('arial 12'), bd=0)
        self.e_instagram.place(relx=0.49, rely=0.34, relwidth=0.18, relheight=0.04)
        
        #placeholder_instagram(self.e_instagram)
            #cometário
        self.title_comment = Label(self.frame_content_form, text="OBS:", font=('arial 12'), foreground='#ADADAD', bg='white')
        self.title_comment.place(relx=0.148, rely=0.395)
        self.e_comment = Entry(self.frame_content_form, bg='#ADADAD', font=('arial 12'), bd=0)
        self.e_comment.place(relx=0.150, rely=0.44, relwidth=0.52, relheight=0.04)
        # endereço
        self.linha2 = Frame(self.frame_content_form, bg='#5f5f5f')
        self.linha2.place(relx=0.01, rely=0.56, relwidth=0.66, relheight=0.004)
        self.titulo_endereco = Label(self.frame_content_form, text="ENDEREÇO", font=('arial 14'), foreground='#ADADAD', bg='white')
        self.titulo_endereco.place(relx=0.01, rely=0.51)
            #CEP
        self.title_cep = Label(self.frame_content_form, text="CEP:", font=('arial 12'), foreground='#ADADAD', bg='white')
        self.title_cep.place(relx=0.01, rely=0.605)
        self.e_cep = Entry(self.frame_content_form, bg='#ADADAD', font=('arial 12'), bd=0)
        self.e_cep.place(relx=0.01, rely=0.65, relwidth=0.08, relheight=0.04)  
        #placeholder_cep(self.e_cep)
            #RUA
        self.title_rua = Label(self.frame_content_form, text="RUA:", font=('arial 14'), foreground='#ADADAD', bg='white')
        self.title_rua.place(relx=.125, rely= .605 )
        self.e_rua = Entry(self.frame_content_form, bg='#ADADAD', font=('arial 12'), bd=0)
        self.e_rua.place(relx=0.125, rely=0.65, relwidth=0.38, relheight=0.04)
        #placeholder_endereco(self.e_rua)
            #N°
        self.title_numero = Label(self.frame_content_form, text="NÚMERO:", font=('arial 14'), foreground='#ADADAD', bg='white')
        self.title_numero.place(relx=.545, rely= .605 )
        self.e_numero = Entry(self.frame_content_form, bg='#ADADAD', font=('arial 12'), bd=0)
        self.e_numero.place(relx=0.545, rely=0.65, relwidth=0.124, relheight=0.04)
            #BAIRRO
        self.title_bairro = Label(self.frame_content_form, text="BAIRRO:", font=('arial 14'), foreground='#ADADAD', bg='white')
        self.title_bairro.place(relx=.01, rely= .705 )
        self.e_bairro = Entry(self.frame_content_form, bg='#ADADAD', font=('arial 12'), bd=0)
        self.e_bairro.place(relx=0.01, rely=0.75, relwidth=0.20, relheight=0.04)
        #placeholder_endereco(self.e_bairro) 
            #CIDADE
        self.title_cidade = Label(self.frame_content_form, text="CIDADE:", font=('arial 14'), foreground='#ADADAD', bg='white')
        self.title_cidade.place(relx=.24, rely= .705 )
        self.e_cidade = Entry(self.frame_content_form, bg='#ADADAD', font=('arial 12'), bd=0)
        self.e_cidade.place(relx=0.24, rely=0.75, relwidth=0.263, relheight=0.04)
        #placeholder_endereco(self.e_cidade)
            #ESTADO
        self.e_estados = ttk.Combobox(self.frame_content_form, font=('arial 12'), takefocus=True, state='readonly')
        self.e_estados['values'] = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']
        self.e_estados.current(24)  # Pré-seleciona o estado de São Paulo
        self.e_estados.place(relx=0.545, rely=0.75, relwidth=0.124, relheight=0.04)      
        self.title_estado = Label(self.frame_content_form, text="ESTADO:", font=('arial 14'), foreground='#ADADAD', bg='white')
        self.title_estado.place(relx=.545, rely= .705 )
        #botão limpar
        self.img_limpar = Diretorios('vassoura.png').img
        self.btn_limpar_endereco = Button(self.frame_content_form, text=' Limpar', image=self.img_limpar, compound=LEFT, bg='#ADADAD', font=('arial 12 bold'),  cursor='hand2') #command=lambda: limpar([self.e_cidade, self.e_bairro, self.e_numero, self.e_rua, self.e_cep]),
        self.btn_limpar_endereco.place(relx=.600, rely=.810, relheight=0.05, relwidth= 0.07)        
        self.btn_limpar_cadastro = Button(self.frame_content_form, text=' Limpar', image=self.img_limpar, compound=LEFT, bg='#ADADAD', font=('arial 12 bold'),  cursor='hand2') #command= lambda:limpar([self.e_nome, self.e_sobrenome, self.e_cpf, self.e_celular, self.e_email, self.e_comment]),
        self.btn_limpar_cadastro.place(relx=.600, rely=.505, relheight=0.05, relwidth= 0.07)
        #botão salvar
        self.img_salvar = Diretorios('salvar.png').img
        self.btn_salvar = Button(self.frame_content_form, text='Salvar', image=self.img_salvar, compound=LEFT, bg='#3DB725', font=('arial 22 bold'), cursor='hand2', foreground='white')#command=self.salvar_cliente)
        self.btn_salvar.place(relx=.25, rely=.91, relwidth=.18)
        #botão voltar
        self.img_voltar = Diretorios('voltar.png').img
        self.btn_voltar = Button(self.frame_content_form, image=self.img_voltar, bg='white', cursor='hand2',  relief='flat')#command=self.voltar,
        self.btn_voltar.place(relx=0.962, rely=0)

        self.hist_titulo = Label(self.frame_content_form, text='Histórico Clientes', bg='white', font=('arial 16 bold'), foreground='#5f5f5f')
        self.hist_linha = Frame(self.frame_content_form, bg='#5f5f5f')
        self.hist_linha.place(relx=0.689, rely=0.17, relwidth=0.30, relheight=0.004)
        self.hist_titulo.place(relx=.689, rely=0.125) 
        self.hist_scroll = Scrollbar(self.frame_content_form)
        self.hist_scroll.place(relx=0.985, rely=0.2, relheight=.798, relwidth=.015)              
        self.tvw_hist = ttk.Treeview(self.frame_content_form, yscrollcommand=self.hist_scroll.set, columns=("Data", "Nome", "Valor"), show="headings")
        self.hist_scroll.config(command=self.tvw_hist.yview)       
        self.tvw_hist.column("Data", anchor=W, width=30, minwidth=20)
        self.tvw_hist.column("Nome", anchor=W, width=70, minwidth=120)
        self.tvw_hist.column("Valor", anchor=CENTER, width=70, minwidth=25)
        self.tvw_hist.place(relx=0.689, rely=0.20, relheight=.795, relwidth=.297)
        
        self.tvw_hist.heading("#1", text="DATA", anchor=CENTER)
        self.tvw_hist.heading("#2", text="NOME", anchor=CENTER)
        self.tvw_hist.heading("#3", text="VALOR", anchor=CENTER)
        



