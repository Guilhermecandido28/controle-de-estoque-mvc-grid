from controllers.header import HeaderController
from models.main import Model
from views.main import View
from tkinter import messagebox
from models.infra.entities.tabelas import Cliente
from models.infra.repository.repository import Repository
import requests
from bs4 import BeautifulSoup
import os
from PIL import Image
import io
from io import BytesIO
from PIL import Image, ImageTk
from tkinter import filedialog
from .helpers.formatadores import *
from datetime import datetime

class ClienteRegisterController(HeaderController):
    def __init__(self, model: Model, view: View) -> None:
        HeaderController.__init__(self, model, view)
        self.model = model
        self.view = view
        self.frame = self.view.frames["client_register"]
        self.repo = Repository(Cliente)
        self._bind()
        super()._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        if isinstance(self.frame, type(self.view.frames["client_register"])):
            '''confirmar a instancia do frame para fazer o bind dos eventos'''
            self.frame.botao_upload.config(command=self.upload)
            self.frame.botao_upload_instagram.config(command=self.upload_instagram)
            self.frame.btn_limpar_cadastro.config(command=self.cleanaddress)
            self.frame.btn_limpar_endereco.config(command=self.cleancadastro)
            self.frame.btn_salvar.config(command=self.salvar)
            self.frame.e_nome.config(vcmd=placeholder_nome(self.frame.e_nome))
            self.frame.e_sobrenome.config(vcmd=placeholder_sobrenome(self.frame.e_sobrenome))
            self.frame.e_cpf.config(vcmd=placeholder_cpf(self.frame.e_cpf))
            self.frame.e_celular.config(vcmd=placeholder_celular(self.frame.e_celular))
            self.frame.e_instagram.config(vcmd=placeholder_instagram(self.frame.e_instagram))
            self.frame.e_cep.config(vcmd=placeholder_cep(self.frame.e_cep))            
            self.valores_treeview()
                
                           

    
    def valores_treeview(self):
        data_atual = datetime.now().strftime('%d/%m/%Y')
        re = self.repo.select_with_columns('nome', 'valor_gasto')
        print(re)
        for valor in re:
            nome = valor[0]
            valor_gasto = valor[1]
            data_formatada = f"{data_atual} {nome} {valor_gasto}"            
            self.frame.tvw_hist.insert("", "end", values=data_formatada)

        
        
    def salvar(self):
        
        self.repo.insert({             
           'nome': self.frame.e_nome.get(),
           'imagem': self.transforma_imagem_BYTES(), 
           'sobrenome': self.frame.e_sobrenome.get(),
           'celular': self.frame.e_celular.get(),
           'cpf': self.frame.e_cpf.get(),
           'instagram': self.frame.e_instagram.get(),
           'OBS' : self.frame.e_comment.get(),
           'CEP': self.frame.e_cep.get(),
           'rua': self.frame.e_rua.get(),
           'numero': self.frame.e_numero.get(),
           'bairro': self.frame.e_bairro.get(),
           'cidade': self.frame.e_cidade.get(),
           'estado': self.frame.e_estados.get()}
           )     
        messagebox.showinfo("showinfo", "Cliente Salvo")

    def cleanaddress(self):
        self.frame.e_rua.delete('0', 'end')
        self.frame.e_numero.delete('0','end')
        self.frame.e_bairro.delete('0','end')
        self.frame.e_cidade.delete('0','end')

    def cleancadastro(self):
        self.frame.e_nome.delete('0','end')
        self.frame.e_sobrenome.delete('0','end')        
        self.frame.e_cpf.delete('0','end')
        self.frame.e_celular.delete('0','end')
        self.frame.e_instagram.delete('0','end')
        
        

    def upload(self):
                        
        self.filename = filedialog.askopenfilename(title="Selecione uma foto", filetypes=[("Imagens", "*.jpg *.png *.bmp")])        
        self.img = Image.open(self.filename)
        largura = self.frame.my_canvas.winfo_width()
        altura = self.frame.my_canvas.winfo_height()
        resized_img2 = self.img.resize((largura, altura))
        self.img_tk = ImageTk.PhotoImage(resized_img2)
        self.img_id = self.frame.my_canvas.create_image(0,0, image=self.img_tk, anchor='nw')
        messagebox.showinfo("showinfo", "Imagem foi colocada")
        return self.img_id
     
    def obter_url_foto_perfil(self, usuario_instagram):
        url = f"https://www.instagram.com/{usuario_instagram}/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            profile_picture_url = soup.find('meta', {'property': 'og:image'})['content']
            return profile_picture_url
        else:
            print('Erro ao acessar o perfil do Instagram')
            return None

    def baixar_foto_perfil(self, url, usuario_instagram):
        response = requests.get(url)
        if response.status_code == 200:           
            
            file_path = os.path.join('../views/functions_view/imagens/fotos_instagram/', f'{usuario_instagram}.jpg')
            with open(file_path, 'wb') as file:
                file.write(response.content)
            return file_path
        else:
            print('Erro ao baixar a foto de perfil')
            return None
        
    def upload_instagram(self):
        usuario_instagram = self.frame.e_instagram.get()
        try:
            url_foto_perfil = self.obter_url_foto_perfil(usuario_instagram)
        except:
            messagebox.showerror('Erro', 'Usuário de instagram não encontrado')
            
        if url_foto_perfil:
            caminho_foto_perfil = self.baixar_foto_perfil(url_foto_perfil, usuario_instagram)
            if caminho_foto_perfil:
                print('Foto de perfil baixada com sucesso:', caminho_foto_perfil)
            else:
                print('Não foi possível baixar a foto de perfil')
        else:
            print('Não foi possível obter a URL da foto de perfil')
        
        self.filename = f'../views/functions_view/imagens/fotos_instagram/{self.frame.e_instagram.get()}.jpg'        
        self.img = Image.open(self.filename)
        largura = self.frame.my_canvas.winfo_width()
        altura = self.frame.my_canvas.winfo_height()
        resized_img2 = self.img.resize((largura, altura))
        self.img_tk = ImageTk.PhotoImage(resized_img2)
        self.img_id = self.frame.my_canvas.create_image(0,0, image=self.img_tk, anchor='nw')

    def transforma_imagem_BYTES(self):
        with open(self.filename, 'rb') as f:
            bytes_io = BytesIO(f.read())
            imagem_bytes = bytes_io.getvalue()
            return imagem_bytes
        
        
        