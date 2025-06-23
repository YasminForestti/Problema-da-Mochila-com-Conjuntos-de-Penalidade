import os
from typing import Literal
from dotenv import load_dotenv

def save_file_paths(filename='file_paths.txt'):
    """ Função que escreve os caminhos de arquivos em um arquivo de texto de forma sequencial
        Começando pelos arquivos de 300 itens para todos os cenários possíveis.
    """
    load_dotenv(dotenv_path=".env") 
    INSTANCES_PATH = os.getenv('INSTANCES')
    scenarios = [f'scenario{i}' for i in range(1,5)]
    types = [[f'correlated_sc{i}',f'fully_correlated_sc{i}',f'not_correlated_sc{i}'] for i in range(1,5)]
    sizes = ['300','500','700','800','1000']
    
    with open('file_paths.txt', 'w') as f:
        for scenario in scenarios:
            scenario_i = int(scenario.split('scenario')[1])
            for type in types[scenario_i-1]:
                for size in sizes:
                    for i in range(1,11):
                        file_path = f'{INSTANCES_PATH}/{scenario}/{type}/{size}/kpfs_{i}.txt'
                        f.write(file_path + '\n')

def get_file_path(i, mode:Literal['scenario','size']='scenario'):
    """ Função que lê a linha i do arquivo file_paths.txt.
        Começa em 1.
    """
    file_path = 'file_paths_by_scenario.txt' if mode == 'scenario' else 'file_paths_by_size.txt'
    try:
        with open(file_path, 'r') as f:
            for line_num, line in enumerate(f, 1):
                if line_num == i:
                    return line.strip()
        return None
    except: 
        return None


# Use example
save_file_paths('file_paths_by_scenario.txt') # uma vez no seu repositório
# current_file = get_file_path(55) # para cada vez que quiser abrir um arquivo novo


