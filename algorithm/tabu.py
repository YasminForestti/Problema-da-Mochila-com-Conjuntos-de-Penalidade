import utils.tools as tools
from utils.knapsack import Knapsack
import numpy as np

def tabu_search(knapsack: Knapsack, max_iter: int, max_tabu_size: int):
    # Inicializa o estado atual com os itens e o lucro do knapsack
    current_items = knapsack.get_items()
    current_profit = knapsack.get_profit()
    
    # Inicializa a melhor solução encontrada com os itens e lucro do estado atual
    best_items = current_items.copy()
    best_profit = current_profit

    # Inicializa a lista tabu com a solução inicial (convertida para inteiro)
    tabu_list = [_convert_to_int(current_items)]  

    for _ in range(max_iter):
        # Gera os vizinhos da solução atual (alternando itens)
        neighbors = _generate_neighbors(current_items)  

        best_candidate = None  
        best_candidate_profit = -1  
        best_candidate_int = None  

        # Avalia cada vizinho
        for neighbor in neighbors:
            knapsack.replace_items(neighbor)  
            if knapsack.is_valid():  
                neighbor_int = _convert_to_int(neighbor)  
                profit = knapsack.get_profit()  
                # Se o vizinho não está na lista tabu e tem lucro maior que o melhor encontrado, atualiza
                if neighbor_int not in tabu_list and profit > best_candidate_profit:
                    best_candidate = neighbor.copy() 
                    best_candidate_profit = profit  
                    best_candidate_int = neighbor_int  
        # Se encontrou um bom candidato, atualiza o estado do knapsack
        if best_candidate is not None:
            knapsack.replace_items(best_candidate) 
            current_items = best_candidate.copy() 
            current_profit = best_candidate_profit

            # Adiciona o novo estado à lista tabu
            tabu_list.append(best_candidate_int)
            if len(tabu_list) > max_tabu_size: 
                tabu_list.pop(0) 

            # Se o lucro atual for melhor que o melhor global, atualiza a melhor solução
            if current_profit > best_profit:
                best_items = current_items.copy() 
                best_profit = current_profit 

    # Retorna a melhor solução encontrada
    return best_items, best_profit



def _generate_neighbors(items: np.ndarray):
    neighbors = []
    for i in range(len(items)):
        neighbor = items.copy()
        neighbor[i] = 1 if neighbor[i] == 0 else 0
        neighbors.append(neighbor)
    return neighbors

def _convert_to_int(items: np.ndarray):
    return int(''.join(str(int(b)) for b in items), 2)