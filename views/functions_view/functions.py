import os
from tkinter import PhotoImage
from tkinter.constants import NW
from PIL import Image, ImageTk

class Diretorios:
    imagens_cache = {}  # Dicionário para armazenar imagens em cache

    def __init__(self, arquivo, diretorio_base='imagens') -> None:
        # Obtém o diretório do script atual
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        
        # Constrói o caminho completo até o diretório base (por padrão, 'imagens')
        diretorio_base = os.path.join(diretorio_atual, diretorio_base)
        
        # Constrói o caminho completo até o arquivo
        self.caminho = os.path.join(diretorio_base, arquivo)
        
        
        try:
            # Verifica se a imagem já está em cache
            if self.caminho not in Diretorios.imagens_cache:
                Diretorios.imagens_cache[self.caminho] = PhotoImage(file=self.caminho)
            
            # Usa a referência armazenada em cache
            self.img = Diretorios.imagens_cache[self.caminho]
        except Exception as e:
            print(f"Erro ao carregar a imagem '{self.caminho}': {e}")
            self.img = None

class Redimensionamento:
    def __init__(self, imagem) -> None:
        self.imagem = imagem    
    
    def resize(self, frame, event):
        nova_imagem = self.imagem.resize((event.width, event.height)) # ajusta a imagem confome necessário
        nova_imagem_tk = ImageTk.PhotoImage(nova_imagem) # transforma em um formato que o tkinter aceita
        frame.create_image(0, 0, anchor=NW, image=nova_imagem_tk) # coloca a imagem no frame
        frame.image = nova_imagem_tk # garante que a imagem permaneça enquando a interface gráfica estiver ativa

class OndeEstou:
    def __init__(self, frame, texto, diretorio) -> None:
        self.frame = frame
        self.texto = texto
        self.diretorio = diretorio

    def localizador(self):
        
        # self.frame.place(
        #     relx=0,
        #     rely=0.14
        #     relwidth=1,
        #     relheight=0.09) # coloca o frame na interface
        
        self.frame.create_text(
        100,
        30,
        text=f'{self.texto}',
        anchor=NW,
        font=('arial 18 bold underline')) # cria o texto que identifica a localização.         
        
        caminho_absoluto = os.path.join(os.path.dirname(__file__), 'imagens', 'location.png') # caminho da imagem
        imagem = Image.open(f'{caminho_absoluto}') # abre a imagem 

        self.obj = Redimensionamento(imagem) # classe reponsavel pelo redimensionamento eventual da imagem
        
        self.frame.bind('<Configure>', lambda event: self.obj.resize(self.frame, event)) # metodo que responsavel por iniciar o processo de redimensionamento.
        


        
    
