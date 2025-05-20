class BuscaLocal:
    def __init__(self, configuracao_inicial):
        self.c = configuracao_inicial # indices de itens na mochila 
        
    def __str__(self):
        return f"BuscaLocal({self.local})"

    def __repr__(self):
        return f"BuscaLocal({self.local})"