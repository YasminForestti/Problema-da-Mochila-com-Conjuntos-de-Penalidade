import os, dotenv
dotenv.load_dotenv()
INSTANCES_PATH = os.getenv('INSTANCES')
from data import Data
from knapsack import Knapsack
import numpy as np


data_1 = Data(f'{INSTANCES_PATH}/scenario1/correlated_sc1/300/kpfs_1.txt')

m = Knapsack(data_1)
m.add_item(0)
print(np.argsort(m.get_cost_benefit_ratio(), kind='heapsort')[::-1])
m.add_item(98)
m.add_item(263)
m.remove_item(98)
print(m.is_valid())
