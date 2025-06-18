import time
import os
import pandas as pd
import numpy as np

class ExecutionLog:
    def __init__(self, file_path, run_count, method, hyperparams):
        self.file_path = file_path
        self.run_count = run_count # pode ser por ex o numero da iteracao da execucao do algoritmo (se essa é a quinta rodada)
        self.start_time = time.time() 
        self.hyperparams = hyperparams # pode ser algum valor usado no algoritmo. ex do tabu search: {tabu_size: 10, max_iter: 100}
        self.log_file = f"{self.file_path.split('.txt')[0]}_{method}_exec_log.csv"
    
    def log_execution(self, best_profit, best_items):
        end_time = time.time()
        time_taken = end_time - self.start_time
        best_items = [str(item//1) for item in best_items]
        # Create new row data
        new_row = {
            'run_count': self.run_count,
            'hyperparams': self.hyperparams,
            'best_profit': best_profit,
            'best_items': f"[{';'.join(best_items)}]",
            'time_taken': time_taken
        }
        
        # Convert to DataFrame
        new_df = pd.DataFrame([new_row])
        
        # Append to existing file or create new one
        if os.path.exists(self.log_file):
            new_df.to_csv(self.log_file, mode='a', header=False, index=False)
        else:
            new_df.to_csv(self.log_file, index=False)

