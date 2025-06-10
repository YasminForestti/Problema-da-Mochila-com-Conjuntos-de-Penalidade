import numpy as np

class Contrucao: 
    """"
    Classe que monta a lista de candidatos
    """
    def __init__(self,alpha, mochila):
        self.alpha = alpha 
        self.mochila = mochila 

    def LCR(self, verbose = False):
        """
        Método que monta a lista de candidatos restritas
        """
        inter = 0
        while True:
            #get min an max cost-benefit ratio with the index position 
            min_index = np.argmin(self.mochila.get_cost_benefit_ratio())
            max_index = np.argmax(self.mochila.get_cost_benefit_ratio())

            min_value = self.mochila.get_cost_benefit_ratio()[min_index]
            max_value = self.mochila.get_cost_benefit_ratio()[max_index]

            min_candidate = min_value + self.alpha * (max_value - min_value)
            max_candidate = max_value

            random_index = np.random.choice(np.where((self.mochila.get_cost_benefit_ratio() >= min_candidate) & (self.mochila.get_cost_benefit_ratio() <= max_candidate))[0])

            self.mochila.add_item(random_index)
            if not self.mochila.is_valid():
                self.mochila.remove_item(random_index)
                break
            
            if verbose:
                print(f'-----------Interaction : {inter}-------------\n')
                print(min_candidate, max_candidate)
                print(f'Random index chosen: {random_index}\nValue: {self.mochila.get_cost_benefit_ratio()[random_index]}')
                print(f'---------------------------------------------\n')
            inter += 1 
