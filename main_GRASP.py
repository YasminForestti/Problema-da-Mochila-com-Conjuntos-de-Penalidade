from algorithm.methods import model
from utils.tools import Construcao 
from utils.data import Data
from utils.knapsack import Knapsack
import numpy as np
from utils.logFiles import ExecutionLog
from utils.openFiles import get_file_path

numb_of_iter = [100, 500, 1000, 2000]
alfas = [0.3,0.5, 0.8,0.95]
busca_local = ['melhor', 'primeiro']

i = 1
while True:
    file_path = get_file_path(i)
    if file_path is None or  'scenario2' in file_path:
        break
    data = Data(file_path)
    for tipo_busca_local in busca_local:
        for alfa in alfas:
            for max_iter in numb_of_iter:
                execution_log = ExecutionLog(file_path, iter, {'max_iter': max_iter, 'alfa': alfa, 'Busca Local': tipo_busca_local})
                
                mochila = Knapsack(data)
                model_method = model(mochila, busca = tipo_busca_local)
                
                melhor_items_mochila = model_method.GRASP(alfa = alfa, criterio_parada=max_iter)

                mochila.replace_items(melhor_items_mochila)
                best_profit = mochila.get_profit()
                best_items = melhor_items_mochila
                execution_log.log_execution(best_profit, best_items)

