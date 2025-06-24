import pandas as pd
from utils.knapsack import Knapsack
from utils.data import Data
import numpy as np


base_path = "data/scenario1/correlated_sc1/300/kpfs_1.txt"
result_path = "~/windows/Downloads/kpfs_1_Genetic_exec_log.csv"

data = Data(base_path)
ks = Knapsack(data)

df = pd.read_csv(result_path)

for row in df.iloc:
    items = row["best_items"].replace(";", ", ")
    items = np.array(eval(items))

    ks.replace_items(items)
    print(f"KS {row['run_count']}, profit={ks.get_profit()}, valid={ks.is_valid()}")
