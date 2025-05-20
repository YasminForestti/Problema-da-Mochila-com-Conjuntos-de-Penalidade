import numpy as np

class Data:
    """
    A class to handle and parse data from input files for the Knapsack problem with penalty sets.
    
    This class reads and processes data from a file containing information about items,
    their profits, weights, and penalty sets. It provides methods to access this data
    in a structured way.
    """
    def __init__(self, file_path):
        """
        Initialize the Data object by reading and parsing the input file.

        Args:
            file_path (str): Path to the input file containing the problem data.
        """
        self.file_path = file_path
        self.raw_data = self._parse_data_from_file()
        self._set_initial_profits()
        self.set_weights()
        self.set_forfeit_set()

    def _parse_data_from_file(self):
        """
        Parse the raw data from the input file.

        Returns:
            list: A list of lists containing the parsed data from the file.
        """
        data = []
        with open(self.file_path, 'r') as file:
            for line in file:
                data.append(line.strip().split())
        return data
    

    def _set_initial_profits(self):
        """
        Set the initial profits for all items from the raw data.
        """
        self._initial_profits = np.array(self.raw_data[1], dtype=int)
    
    def get_initial_profits(self):
        """
        Get a copy of the initial profits array.

        Returns:
            numpy.ndarray: A copy of the array containing initial profits for all items.
        """
        return np.copy(self._initial_profits)

    def set_weights(self):
        """
        Set the weights for all items from the raw data.
        """
        self._weights = np.array(self.raw_data[2], dtype=int)

    def get_weights(self):
        """
        Get the weights array.

        Returns:
            numpy.ndarray: Array containing weights for all items.
        """
        return self._weights

    def set_forfeit_set(self):
        """
        Set up the forfeit sets, their limits, and penalties from the raw data.
        This method processes the penalty set definitions and their contents.
        """
        self._forfeit_sets = np.zeros((int(self.raw_data[0][0]), int(self.raw_data[0][1])), dtype=int)
        self._forfeit_limits = np.ones(int(self.raw_data[0][1]))
        self._forfeit_penalties = np.zeros(int(self.raw_data[0][1]))

        sets_definitions = self.raw_data[3::2]
        sets_content = self.raw_data[4::2]
        id = 0
        for definition, content in zip(sets_definitions, sets_content):
            self._forfeit_limits[id] = int(definition[0]) - 1
            self._forfeit_penalties[id] = int(definition[1]) 

            for item in content:
                self._forfeit_sets[int(item), id] = 1
            id += 1
        
    def get_forfeit_sets(self):
        """
        Get the forfeit sets matrix.

        Returns:
            numpy.ndarray: A binary matrix where each column represents a penalty set
                          and each row represents an item's membership in that set.
        """
        return self._forfeit_sets

    def get_forfeit_limits(self):
        """
        Get the limits of each forfeit set.
        Returns:
            numpy.ndarray: Array containing the current limit of each forfeit set.
        """
        return self._forfeit_limits

    def get_forfeit_penalties(self):
        """
        Get the penalties associated with each forfeit set.

        Returns:
            numpy.ndarray: Array containing the penalty values for each forfeit set.
        """
        return self._forfeit_penalties
    
    def get_knapsack_max_weight(self):
        """
        Get the maximum weight capacity of the knapsack.

        Returns:
            int: The maximum weight capacity of the knapsack.
        """
        return int(self.raw_data[0][2])
