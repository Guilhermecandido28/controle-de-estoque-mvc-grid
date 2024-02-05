from controllers.header import HeaderController
from models.main import Model
from views.main import View

class ClienteHomeController():
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["client_home"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        
        self.frame.btn_addcliente.config(command=self.client_register_screen)


    def client_register_screen(self) -> None:
        
        self.view.switch("client_register")