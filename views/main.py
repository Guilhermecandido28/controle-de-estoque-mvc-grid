from tkinter import Button
from typing import TypedDict

from views.client_register import ClienteRegisterView
from views.home import HomeView
from .root import Root
from .clientehome import ClienteHomeView
from views.header import HeaderView


class Frames(TypedDict):
   # signup: SignUpView
    client_register: ClienteRegisterView
    home: HomeView
    client_home: ClienteHomeView


class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}  # type: ignore
        self._add_frame(ClienteHomeView, "client_home")
        self._add_frame(ClienteRegisterView, "client_register")
      #  self._add_frame(SignInView, "signin")
        self._add_frame(HomeView, "home")
       
   

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] =Frame(self.root)
        
        # Os frames na coluna 0 devem preencher a largura
        # completa ao serem expandidos até o final.
        self.frames[name].columnconfigure(0, weight=1)

        # Na linha 4, 'frame_content' deve preencher a altura
        # ao ser expandido.
        self.frames[name].rowconfigure(4, weight=1)

        self.frames[name].configure(bg='#8A8A8A')

        self.frames[name].grid(row=0, column=0, sticky="news")
        
    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()
