from tkinter import constants
import tkinter as tk
from tkinter import ttk
from .header import HeaderView

class HomeView(HeaderView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)	