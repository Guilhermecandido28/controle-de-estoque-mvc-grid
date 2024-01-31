from tkinter import Tk


class Root(Tk):
    def __init__(self):
        super().__init__()

        #start_width = 1500
        #min_width = 1000

        start_width = 1500
        #min_width = 1000
        
        start_height = 1000
    

        self.geometry(f"{start_width}x{start_height}")
        #self.minsize(width=min_width, height=min_height)
        self.title("Controle fincanceiro")

        self.configure(bg='white')
        
        self.minsize(1500, 1000)

        # O mecanismo adotado para trocar os frames
        # adiciona um frame 0,0, pai dos demais. Esse comando
        # serve para permiti-lo expandir ao redimensionar a janela.
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        
