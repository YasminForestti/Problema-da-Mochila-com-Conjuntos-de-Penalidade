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
            #get min an max cost-benefit ratio with the index position 
            min_index = np.argmin(mochila.get_cost_benefit_ratio())
            max_index = np.argmax(mochila.get_cost_benefit_ratio())

            min_value = mochila.get_cost_benefit_ratio()[min_index]
            max_value = mochila.get_cost_benefit_ratio()[max_index]

            min_candidate = min_value + self.alpha * (max_value - min_value)
            max_candidate = max_value

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
        melhor_mochila = mochila.clone()
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
                    melhor_mochila = vizinho.clone()
                    melhor_valor = melhor_mochila.get_profit()
                    vizinho.remove_item(j)     
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