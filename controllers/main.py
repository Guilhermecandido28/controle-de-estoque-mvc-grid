from controllers.cliente_register import ClienteRegisterController
from models.main import Model
from models.auth import Auth
from views.main import View
from .clientehome import ClienteHomeController
from .header import HeaderController


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model
        self.clienteregister_controller = ClienteRegisterController(model, view)
        self.clientehome_controller = ClienteHomeController(model, view)
        self.home_header_controller = HeaderController(model, view)
        #self.model.auth.add_event_listener("auth_changed", self.auth_state_listener)


    def start(self) -> None:
        # Here, you can do operations required before launching the gui, for example,
        # self.model.auth.load_auth_state()
        self.view.switch("home")

        self.view.start_mainloop()
