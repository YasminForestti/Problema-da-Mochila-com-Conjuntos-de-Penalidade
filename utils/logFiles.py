import time

class ExecutionLog:
    def __init__(self, file_path, run_count, hyperparams):
        self.file_path = file_path
        self.run_count = run_count # pode ser por ex o numero da iteracao da execucao do algoritmo (se essa é a quinta rodada)
        self.start_time = time.time() 
        self.hyperparams = hyperparams # pode ser algum valor usado no algoritmo. ex do tabu search: {tabu_size: 10, max_iter: 100}
    
    def log_execution(self, best_profit, best_items):
        end_time = time.time()
        time_taken = end_time - self.start_time
        # um arquivo de log para cada instância
        # uma linha para cada run_id
        with open(f"{self.file_path.split('.txt')[0]}_exec_log.csv", 'a') as f: 
            f.write(f"run_count,hyperparams,best_profit,best_items,time_taken\n")
            f.write(f"{self.run_count},{self.hyperparams},{best_profit},{best_items},{time_taken}\n")

