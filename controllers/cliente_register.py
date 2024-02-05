from controllers.header import HeaderController
from models.main import Model
from views.main import View
from tkinter import messagebox 

class ClienteRegisterController(HeaderController):
    def __init__(self, model: Model, view: View) -> None:
        HeaderController.__init__(self, model, view)
        self.model = model
        self.view = view
        self.frame = self.view.frames["client_register"]
        self._bind()
        super()._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        if isinstance(self.frame, type(self.view.frames["client_register"])):
            '''confirmar a instancia do frame para fazer o bind dos eventos'''
            self.frame.botao_upload.config(command=self.testupload)
            self.frame.botao_upload_instagram.config(command=self.testinstangram)
            self.frame.btn_limpar_cadastro.config(command=self.testcleanprofile)
            self.frame.btn_limpar_endereco.config(command=self.testcleanaddress)
            self.frame.btn_salvar.config(command=self.testsalvar)

    def testsalvar(self):
        messagebox.showinfo("showinfo", "Information")

    def testcleanaddress(self):
        messagebox.showinfo("showinfo", "Information")

    def testupload(self):
        messagebox.showinfo("showinfo", "Information")
    
    def testcleanprofile(self):
        messagebox.showinfo("showinfo", "Information") 

    def testinstangram(self):
        messagebox.showinfo("showinfo", "Information") 
      

