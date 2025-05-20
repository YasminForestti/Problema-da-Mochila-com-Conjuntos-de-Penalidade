from data import Data
import numpy as np

class Knapsack:
    """
    A class representing a Knapsack with penalty sets.
    
    This class implements a knapsack problem variant where items can belong to penalty sets.
    When items are added or removed, the profits of related items in the same penalty sets
    are dynamically updated based on the current state of these sets.
    """
    def __init__(self, data: Data):
        """
        Initialize the Knapsack with data from a Data object.

        Args:
            data (Data): A Data object containing all necessary information about items,
                        their profits, weights, and penalty sets.
        """
        self._max_weight = data.get_knapsack_max_weight()
        self._initial_profits = data.get_initial_profits() # static profits
        self._profits = data.get_initial_profits() # dynamic profits
        self._forfeit_sets = data.get_forfeit_sets() 
        self._forfeit_limits = data.get_forfeit_limits()
        self._forfeit_penalties = data.get_forfeit_penalties()
        self._weights = data.get_weights()

        self._items = set()
        self._forfeit_usages = np.zeros(len(self._forfeit_limits))
        self._weight = 0
        self._profit = 0

    def __repr__(self):
        """
        Return a string representation of the Knapsack.

        Returns:
            str: A string showing the current items, weight, and profit of the knapsack.
        """
        return f'Mochila: {self._items}, Peso: {self._weight}, Lucro: {self._profit}'
    
    def is_valid(self):
        """
        Check if the knapsack is valid.

        Returns:
            bool: True if the knapsack is valid, False otherwise.
        """
        return self._weight <= self._max_weight

    def get_max_weight(self):
        """
        Get the maximum weight capacity of the knapsack.

        Returns:
            int: The maximum weight capacity.
        """
        return self._max_weight
    
    def get_weight(self):
        """
        Get the current weight of the knapsack.

        Returns:
            int: The current total weight of items in the knapsack.
        """
        return self._weight
    
    def get_profit(self):
        """
        Get the current total profit of the knapsack.

        Returns:
            int: The current total profit considering all items and their penalties.
        """
        return self._profit

    def add_item(self, item_id):
        """
        Add an item to the knapsack if possible.

        Args:
            item_id (int): The ID of the item to add.
        """
        if item_id not in self._items:
            self._weight += self._weights[item_id] 
            self._profit += self._profits[item_id]
            self._items.add(item_id)
            self._update_profits(item_id)

    def get_items(self):
        """
        Get the set of items currently in the knapsack.

        Returns:
            set: A set containing the IDs of all items in the knapsack.
        """
        return self._items

    def _update_profits(self, item_id):
        """
        Update the profits of items based on the current state of penalty sets.

        This method is called when an item is added or removed from the knapsack.
        It updates the profits of all items that share penalty sets with the modified item.

        Args:
            item_id (int): The ID of the item that was added or removed.
            remove (bool, optional): If True, the item is being removed. If False, it's being added.
                                    Defaults to False.
        """
        # Vetor com 1 para cada conjunto que o item_id participa
        item_forfeit_sets = self._forfeit_sets[item_id]
        
        # Atualiza o uso de cada conjunto
        for i in range(len(item_forfeit_sets)):
            # Itera pelos conjuntos que o item_id está
            if item_forfeit_sets[i] == 1:
                self._forfeit_usages[i] += 1
        
        # Calcula o valor de penalidades para cada conjunto.
        penalties = (self._forfeit_limits - self._forfeit_usages) * self._forfeit_penalties
        
        for i in range(len(item_forfeit_sets)):
            # Itera pelos conjuntos i que o item_id está
            if item_forfeit_sets[i] == 1:
                # Itera pelos itens j de cada conjunto i
                for j in range(len(self._profits)):
                    if self._forfeit_sets[j, i] == 1 and j not in self._items:
                        # Atualiza o lucro do item j
                        self._profits[j] = self._profits[j] + penalties[i]
                
        # Se o item já está na mochila, seu lucro já está sendo considerado no total.
        self._profits[item_id] = 0
    def get_all_items_profits(self):
        """
        Get the current profits of all items, considering penalties.
        If the item is already in the knapsack, its profit is 0. 

        Returns:
            numpy.ndarray: Array containing the current profit values for all items.
        """
        return self._profits
    
    def get_all_items_weights(self):
        """
        Get the weights of all items.

        Returns:
            numpy.ndarray: Array containing the weight values for all items.
        """
        return self._weights






