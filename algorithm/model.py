from knapsack import Knapsack
from utils.construcao import Contrucao

class model():
    def __init__(self,data):
        self.mochila = Knapsack(data)
        self.construcao = None
        self.s_star = None

    def GRASP(self, alfa , criterio_parada, verbose = False):
        self.construcao = Contrucao(alfa, self.mochila)
        """
        Perform the GRASP algorithm.

        Args:
            alfa (float): The alpha parameter for the GRASP algorithm.
            criterio_parada (int): The stopping criterion for the GRASP algorithm. (to be defined later)
        """

        while criterio_parada > 0: 
            self.construcao.LCR(verbose = verbose)
            print(self.mochila.get_profit())
            
            criterio_parada -= 1

            # self.s_star = self.mochila.get_profit()
            # criterio_deparada -= 1
            # print(f'Profit: {self.s_star}')
            # print(f'Items in knapsack: {self.mochila.get_items()}')
            # print(f'Weights: {self.mochila.get_weights()}')
            # print(f'Penalties: {self.mochila.get_penalties()}')