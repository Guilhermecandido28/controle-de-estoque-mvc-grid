from models.main import Model
from views.main import View


class HeaderController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.btn_clientes.config(command=self.client_home_screen)
   

    def client_home_screen(self) -> None:
        self.view.switch("client_home")
