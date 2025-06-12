import numpy as np
from utils.knapsack import Knapsack
class Construcao: 
    """"
    Classe que monta a lista de candidatos
    """
    def __init__(self,alpha):
        self.alpha = alpha 

    def LCR(self, mochila:Knapsack, verbose = False):
        """
        Método que monta a lista de candidatos restritas
        """
        while mochila.is_valid():
            current_items = mochila.get_items()
            min_value = min(mochila.get_cost_benefit_ratio())
            max_value = max(mochila.get_cost_benefit_ratio())

            min_candidate = min_value + self.alpha * (max_value - min_value)
            max_candidate = max_value

            if self.alpha == 1:
                random_index = np.random.choice(np.where(mochila.get_cost_benefit_ratio() >= (min_candidate - 0.0000000000001))[0])
            else:
                random_index = np.random.choice(np.where((mochila.get_cost_benefit_ratio() >= min_candidate) & (mochila.get_cost_benefit_ratio() <= max_candidate))[0])

            new_items = current_items.copy()
            new_items[random_index] = 1
            mochila.replace_items(new_items)
        return current_items
            



class BuscaLocal:
       
    def melhor_aprimorante(self, mochila):
        """
        Método que encontra o melhor aprimorante para a mochila percorrendo
        toda vizinhança da mochila. A vizinhança é explorada pelo método SWAP.

        Retorna: nova mochila com melhor solução encontrada ou a própria mochila se não houver melhoria.
        """
        # melhor_mochila_itens = mochila.get_items().copy()
        melhor_valor = mochila.get_profit()
        # print(f"Profit inicial : {melhor_valor}")
        itens = mochila.get_items()

        dentro = np.where(itens == 1)[0]
        fora = np.where(itens == 0)[0]

        for i in dentro:
            vizinho_itens = itens.copy()
            vizinho_itens[i] = 0
            mochila.replace_items(vizinho_itens) 

            potencial_profit = mochila.get_potential_profits()
            profit = mochila.get_profit() 
            for j in fora:
                if mochila.is_future_adding_valid(j) and potencial_profit[j] + profit > melhor_valor:
                    mochila.add_item(j)
                    melhor_mochila_itens = mochila.get_items().copy()
                    melhor_valor = mochila.get_profit()
                    mochila.remove_item(j)     
        melhor_mochila = mochila.replace_items(melhor_mochila_itens)
        return melhor_mochila
    
    def primeiro_aprimorante(self, mochila):
        """
        Método que encontra o melhor aprimorante para a mochila percorrendo
        toda vizinhança da mochila. A vizinhança é explorada pelo método SWAP.

        Retorna: nova mochila com melhor solução encontrada ou a própria mochila se não houver melhoria.
        """
        melhor_valor = mochila.get_profit()
        print(f"Profit inicial : {melhor_valor}")
        itens = mochila.get_items()

        dentro = np.where(itens == 1)[0]
        fora = np.where(itens == 0)[0]

        for i in dentro:
            vizinho = mochila.clone()
            
            vizinho.remove_item(i)
            potencial_profit = vizinho.get_potential_profits()
            profit = vizinho.get_profit() 
            for j in fora:
                if vizinho.is_future_adding_valid(j) and potencial_profit[j] + profit > melhor_valor:
                    vizinho.add_item(j)
                    return vizinho   