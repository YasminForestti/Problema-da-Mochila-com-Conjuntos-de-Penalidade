import numpy as np

class Contrucao: 
    """"
    Classe que monta a lista de candidatos restritas 
    """
    def __init__(self,alpha, conjunto_penalidade, lista_candidatos_valor, lista_candidatos_peso, max_mochila, estado_penalidade , valor_penalidade):
        self.alpha = alpha  
        self.conjunto_penalidade = conjunto_penalidade # matriz feita de numpy array
        self.lista_valor = lista_candidatos_valor # numpy array
        self.lista_peso = lista_candidatos_peso # numpy array
        self.max_mochila = max_mochila # int 
        self.estado_penalidade = estado_penalidade # numpy array
        self.valor_penalidade = valor_penalidade # numpy array

    def LCR(self):
        """
        Método que monta a lista de candidatos restritas
        """
        itens_selecionados = []
        pass

    def __calculo_lucro__(self):
        return (self.lista_valor  / self.lista_peso).tolist()