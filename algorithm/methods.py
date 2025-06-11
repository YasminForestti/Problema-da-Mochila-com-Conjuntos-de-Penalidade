import utils.tools as tools
import numpy as np

class model():
    def __init__(self,mochila):
        self.mochila = mochila
        self.s_star = None
        self.f_s_star = - np.inf

    def GRASP(self, alfa , criterio_parada, verbose = False):
        """
        Perform the GRASP algorithm.

        Args:
            alfa (float): The alpha parameter for the GRASP algorithm.
            criterio_parada (int): The stopping criterion for the GRASP algorithm. (to be defined later)
        """
        buscalocal = tools.BuscaLocal()
        construcao = tools.Contrucao(alfa)
        
        while criterio_parada > 0: 
            m = self.mochila.clone() # mochila vazia 
            construcao.LCR(m,verbose = verbose)
            print(f"Profit of LCR knapsack: {m.get_profit()}")
            s = buscalocal.melhor_aprimorante(m)
            print(f"Profit of melhor Aprimorante knapsack: {s.get_profit()}")
            if s.get_profit() > self.f_s_star:
                self.f_s_star = s.get_profit()
                self.s_star = s.clone()
                print(f'New best solution found with profit: {self.f_s_star}')

            criterio_parada -= 1
        
        return self.s_star