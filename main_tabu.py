from algorithm.tabu import tabu_search
from utils.tools import Construcao 
from utils.data import Data
from utils.knapsack import Knapsack
import numpy as np
import os
from dotenv import load_dotenv
import time
from utils.logFiles import ExecutionLog
from utils.openFiles import get_file_path

load_dotenv(dotenv_path=".env") 
INSTANCES_PATH = os.getenv('INSTANCES')

file_path = get_file_path(1)
data = Data(file_path)
execution_log = ExecutionLog(file_path, '1')
m = Knapsack(data)
c = Construcao(1)
initial_items = c.LCR(m)
m.replace_items(initial_items)
tabu_search(m, 1000, 10)
execution_log.log_execution(m.get_profit(), m.get_items())

