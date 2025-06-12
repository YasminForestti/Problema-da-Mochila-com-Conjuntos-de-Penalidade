import numpy as np

class Contrucao: 
    """"
    Classe que monta a lista de candidatos
    """
    def __init__(self,alpha):
        self.alpha = alpha 

    def LCR(self,mochila, verbose = False):
        """
        Método que monta a lista de candidatos restritas
        """
        inter = 0
        while True:
            min_value = min(mochila.get_cost_benefit_ratio())
            max_value = max(mochila.get_cost_benefit_ratio())

            min_candidate = min_value + self.alpha * (max_value - min_value)
            max_candidate = max_value

            if self.alpha == 1:
                random_index = np.random.choice(np.where(mochila.get_cost_benefit_ratio() >= (min_candidate - 0.0000000000000000000000000001))[0])
            else:
                random_index = np.random.choice(np.where((mochila.get_cost_benefit_ratio() >= min_candidate) & (mochila.get_cost_benefit_ratio() <= max_candidate))[0])

            if mochila.is_future_adding_valid(random_index):
                mochila.add_item(random_index)
            else:
                break
            
            if verbose:
                print(f'-----------Interaction : {inter}-------------\n')
                print(min_candidate, max_candidate)
                print(f'Random index chosen: {random_index}\nValue: {mochila.get_cost_benefit_ratio()[random_index]}')
                print(f'---------------------------------------------\n')
            inter += 1 



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