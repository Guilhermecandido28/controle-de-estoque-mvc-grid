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

        self.configure(bg='red')

        # Na linha 4, 'frame_content' deve preencher a altura
        # ao ser expandido.
        self.rowconfigure(4, weight=1)

        # Os frames na coluna 0 devem preencher a largura
        # completa ao serem expandidos até o final.
        self.columnconfigure(0, weight=1)
