import time

class ExecutionLog:
    def __init__(self, file_path, instance_name):
        self.file_path = file_path
        self.instance_name = instance_name
        self.start_time = time.time()

    def log_execution(self, best_profit, best_items):
        end_time = time.time()
        time_taken = end_time - self.start_time
        with open(f'{self.file_path}/_exec_log.txt', 'a') as f:
            f.write(f"{self.instance_name} - Best Profit: {best_profit} - Best Items: {best_items} - Time Taken: {time_taken}\n")

