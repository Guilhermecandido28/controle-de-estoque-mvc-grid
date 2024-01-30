from typing import TypedDict

from .root import Root
from .home import HomeView
from .signin import SignInView
from .signup import SignUpView
from .clientehome import ClienteHomeView


class Frames(TypedDict):
    signup: SignUpView
    signin: SignInView
    home: HomeView
    clientehome: ClienteHomeView


class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}  # type: ignore
        
        self._add_frame(ClienteHomeView, "clientehome")
        self._add_frame(SignUpView, "signup")
        self._add_frame(SignInView, "signin")
        self._add_frame(HomeView, "home")
   

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        
        # Os frames na coluna 0 devem preencher a largura
        # completa ao serem expandidos até o final.
        self.frames[name].columnconfigure(0, weight=1)
        self.frames[name].grid(row=0, column=0, sticky="news")
        

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()
