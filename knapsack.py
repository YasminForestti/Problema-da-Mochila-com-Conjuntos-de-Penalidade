from data import Data
import numpy as np

class Knapsack:
    """
    A class representing a Knapsack with penalty sets.
    
    This class implements a knapsack problem variant where items can belong to penalty sets.
    When items are added the profits of related items in the same penalty sets
    are dynamically updated based on the current state of these sets.
    """
    def __init__(self, data: Data):
        """
        Initialize the Knapsack with data from a Data object.

        Args:
            data (Data): A Data object containing all necessary information about items,
                        their profits, weights, and penalty sets.
        """
        self.__data = data 
        self._max_weight = data.get_knapsack_max_weight()
        self._weights = data.get_weights()
        self._profits = data.get_initial_profits()
        self._forfeit_sets = data.get_forfeit_sets() 
        self._forfeit_limits = data.get_forfeit_limits()
        self._forfeit_penalties = data.get_forfeit_penalties()

        self._items = np.zeros(len(self._profits))
        self._penalties = np.zeros( (len(self._profits), len(self._profits)) )
        self._set_penalties()


    def _set_penalties(self):
        """
        Set the penalties matrix. It's a square matrix where the element (i,j) is the penalty of item i if item j is in the same penalty set.
        """
        for i in range(len(self._forfeit_penalties)):
            squared = np.outer(self._forfeit_sets[:,i], self._forfeit_sets[:,i])
            np.fill_diagonal(squared, 0)
            self._penalties += squared * self._forfeit_penalties[i]

    def get_profit(self):
        """
        Get the profit of the knapsack.
        """
        penalties =  self._items @ (self._penalties @ self._items.T)/2
        profits = self._profits @ self._items.T
        return profits - penalties

    
    def get_potential_profits(self):
        """
        Get the potential profits of the items outside the knapsack.
        """
        current_profits = self._profits * (1 - self._items)
        return current_profits - (self._penalties @ self._items.T)
    
    def get_cost_benefit_ratio(self):
        """
        Get the cost benefit ratio of the items outside the knapsack.
        """
        return self.get_potential_profits() / self._weights

    def add_item(self, item_id):
        """
        Add an item to the knapsack if possible.

        Args:
            item_id (int): The ID of the item to add.
        """
        if self._items[item_id] == 0:
            self._items[item_id] = 1 
    
    def remove_item(self, item_id):
        """
        Remove an item from the knapsack.

        Args:
            item_id (int): The ID of the item to remove.   
        """
        if self._items[item_id] == 1:
            self._items[item_id] = 0

    def is_valid(self):
        """
        Check if the knapsack is valid.

        Returns:
            bool: True if the knapsack is valid, False otherwise.
        """
        weight = self._weights @ self._items.T
        return weight <= self._max_weight

    def is_future_adding_valid(self, item_id):
        """
        Check if adding an item in the future will keep the knapsack valid.

        Args:
            item_id (int): The ID of the item to check.

        Returns:
            bool: True if adding the item will keep the knapsack valid, False otherwise.
        """
        future_items = self._items.copy()
        future_items[item_id] = 1
        future_weight = self._weights @ future_items.T
        return future_weight <= self._max_weight  

    def get_total_weight(self):
        """
        Get the sum of weights of the items in the knapsack.

        Returns:
            np.float64: The total weight of the items in the knapsack.
        """
        return self._weights @ self._items.T

    # def get_weights(self):
    #     """
    #     Get the weights of the items in the knapsack.

    #     Returns:
    #         np.ndarray: An array of weights for the items.
    #     """
    #     return self._weights

    def get_items(self):
        """
        Get the items in the knapsack.

        Returns:
            np.ndarray: A boolean array indicating which items are in the knapsack.
        """
        return self._items

    def clone(self):
        """
        Create a clone of the knapsack.

        Returns:
            Knapsack: A new Knapsack object with the same state.
        """
        clone = Knapsack(self.__data)
        clone._max_weight = self._max_weight
        clone._weights = self._weights.copy()
        clone._profits = self._profits.copy()
        clone._forfeit_sets = self._forfeit_sets.copy()
        clone._forfeit_limits = self._forfeit_limits.copy()
        clone._forfeit_penalties = self._forfeit_penalties.copy()
        clone._items = self._items.copy()
        clone._penalties = self._penalties.copy()
        return clone