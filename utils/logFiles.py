import time

class ExecutionLog:
    def __init__(self, file_path, instance_name):
        self.file_path = file_path
        self.instance_name = instance_name
        self.start_time = time.time()

    def log_execution(self, best_profit, best_items):
        end_time = time.time()
        time_taken = end_time - self.start_time
        with open(f"{self.file_path.split('.txt')[0]}_exec_log.csv", 'w') as f:
            f.write(f"instance_name,best_profit,best_items,time_taken\n")
            f.write(f"{self.instance_name},{best_profit},{best_items},{time_taken}\n")

