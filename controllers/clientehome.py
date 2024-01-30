from models.main import Model
from views.main import View

class ClienteHomeController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["clientehome"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.btn_clientes.config(command=self.signin)

    def signin(self) -> None:
        self.view.switch("clientehome")
        print("cliente entrou")