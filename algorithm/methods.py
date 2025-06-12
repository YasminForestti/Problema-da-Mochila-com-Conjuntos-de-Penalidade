import utils.tools as tools
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed

class model():
    def __init__(self, mochila):
        self.mochila = mochila
        self.s_star = None
        self.f_s_star = -np.inf

    # def GRASP(self, alfa, criterio_parada, verbose=False):
    #     """
    #     Perform the GRASP algorithm.

    #     Args:
    #         alfa (float): The alpha parameter for the GRASP algorithm.
    #         criterio_parada (int): The stopping criterion for the GRASP algorithm.
    #     """
    #     buscalocal = tools.BuscaLocal()
    #     construcao = tools.Contrucao(alfa)

    #     for _ in range(criterio_parada):
    #         m = self.mochila.clone()
    #         construcao.LCR(m, verbose=verbose)
    #         profit_lcr = m.get_profit()
    #         if verbose:
    #             print(f"Profit of LCR knapsack: {profit_lcr}")
    #         s = buscalocal.melhor_aprimorante(m)
    #         profit_s = s.get_profit()
    #         if verbose:
    #             print(f"Profit of melhor Aprimorante knapsack: {profit_s}")
    #         if profit_s > self.f_s_star:
    #             self.f_s_star = profit_s
    #             self.s_star = s.clone()
    #             if verbose:
    #                 print(f'New best solution found with profit: {self.f_s_star}')

    #     return self.s_star

    def _grasp_iteration(self, alfa, verbose=False):
        """
        Executa uma iteração do GRASP (para uso em paralelo).
        """
        m = self.mochila.clone()
        self.construcao.LCR(m, verbose=verbose)
        profit_lcr = m.get_profit()
        if verbose:
            print(f"Profit of LCR knapsack: {profit_lcr}")
        s = self.buscalocal.melhor_aprimorante(m)
        profit_s = s.get_profit()
        if verbose:
            print(f"Profit of melhor Aprimorante knapsack: {profit_s}")
        return s, profit_s

    def GRASP(self, alfa, criterio_parada, verbose=False, n_jobs=4):
        """
        Executa o algoritmo GRASP com paralelização.

        Args:
            alfa (float): Parâmetro alpha do GRASP.
            criterio_parada (int): Número de iterações.
            n_jobs (int): Número de threads paralelas.
        """
        self.buscalocal = tools.BuscaLocal()
        self.construcao = tools.Construcao(alfa)
        results = []
        with ThreadPoolExecutor(max_workers=n_jobs) as executor:
            futures = [executor.submit(self._grasp_iteration, alfa, verbose) for _ in range(criterio_parada)]
            for future in as_completed(futures):
                s, profit_s = future.result()
                results.append((s, profit_s))
                if profit_s > self.f_s_star:
                    self.f_s_star = profit_s
                    self.s_star = s.clone()
                    if verbose:
                        print(f'New best solution found with profit: {self.f_s_star}')
        return self.s_star