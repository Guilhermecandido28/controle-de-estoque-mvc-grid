from controllers.header import HeaderController
from models.main import Model
from views.main import View
from models.infra.entities.tabelas import Cliente
from models.infra.repository.repository import Repository

class ClienteHomeController():
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["client_home"]
        self.repo = Repository(Cliente)
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        
        self.frame.btn_addcliente.config(command=self.client_register_screen)
        self.valores_treeview()

    def valores_treeview(self):        
        re = self.repo.select_with_columns('id', 'nome','sobrenome', 'celular', 'valor_gasto')
        print(re)
        for valor in re:
            id = valor[0]
            nome = valor[1]
            sobrenome = valor[2]
            contato = valor[3]
            valor_gasto = valor[4]
            valores_formatados = f"{id} {nome} {sobrenome} {contato} {valor_gasto}"
            
            self.frame.ins_treeview.insert("", "end", values=valores_formatados)


    def client_register_screen(self) -> None:
        
        self.view.switch("client_register")