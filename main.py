import os, dotenv
dotenv.load_dotenv()
INSTANCES_PATH = os.getenv('INSTANCES')
from data import Data
from knapsack import Knapsack


data_1 = Data(f'{INSTANCES_PATH}/scenario1/correlated_sc1/300/kpfs_1.txt')

m = Knapsack(data_1)
m.add_item(0)
m.add_item(299)
m.add_item(98)
print(m)
print(m.is_valid())
print((m.get_all_items_profits() / m.get_all_items_weights())[0:10])
