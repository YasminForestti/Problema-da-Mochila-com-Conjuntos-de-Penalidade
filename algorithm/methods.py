import utils.tools as tools
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed

class model():
    def __init__(self, mochila):
        self.mochila = mochila
        self._itens = mochila.get_items()
        self.s_star = None
        self.f_s_star = -np.inf

    def GRASP(self, alfa, criterio_parada, verbose=False):
        """
        Perform the GRASP algorithm.

        Args:
            alfa (float): The alpha parameter for the GRASP algorithm.
            criterio_parada (int): The stopping criterion for the GRASP algorithm.
        """
        buscalocal = tools.BuscaLocal()
        construcao = tools.Construcao(alfa)

        for _ in range(criterio_parada):
            self.mochila.replace_items(self._itens)
            new_items = construcao.LCR(self.mochila)
            self.mochila.replace_items(new_items)

            melhor_items  = buscalocal.melhor_aprimorante(self.mochila)
            self.mochila.replace_items(melhor_items)
            profit_s = self.mochila.get_profit()

            if profit_s > self.f_s_star:
                self.f_s_star = profit_s
                self.s_star = self.mochila.get_items().copy()
                if verbose:
                    print(f'New best solution found with profit: {self.f_s_star}')

        return self.s_star