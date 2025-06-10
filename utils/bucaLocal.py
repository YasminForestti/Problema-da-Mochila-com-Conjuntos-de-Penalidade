class BuscaLocal:
    def __init__(self, mochila):
        self.mochila = mochila
        
    def melhor_aprimorante(self):
        """
        Método que encontra o melhor aprimorante para a mochila.
        Retorna o índice do item a ser adicionado ou removido.
        """
        melhor_valor = 0
        melhor_indice = -1
        
        for i in range(len(self.mochila.get_items())):
            if self.mochila.is_valid(i):
                valor_atual = self.mochila.get_profit() + self.mochila.get_value(i)
                if valor_atual > melhor_valor:
                    melhor_valor = valor_atual
                    melhor_indice = i
        
        return melhor_indice if melhor_indice != -1 else None
    
    def swap(self):
        mochila_swap = self.mochila.clone()

        for i in range(len(self.mochila.get_items())):
            for j in range(len(self.mochila.get_items())):
                if i != j: 
                    if self.mochila.get_items()[i] == 1 and self.mochila.get_items()[j] == 0:
                        mochila_swap.remove_item(i)
                        mochila_swap.add_item(j)
                        if mochila_swap.is_valid():
                            print(f"Item {i} removed and item {j} added")
                            if mochila_swap.get_profit() > self.mochila.get_profit():
                                break
                    elif self.mochila.get_items()[i] == 0 and self.mochila.get_items()[j] == 1:
                        mochila_swap.remove_item(j)
                        mochila_swap.add_item(i)
                        if mochila_swap.is_valid():
                            print(f"Item {j} removed and item {i} added")
                            if mochila_swap.get_profit() > self.mochila.get_profit():
                                break
        
