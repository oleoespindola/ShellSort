import random
import time

class ShellSort:
        
    def sort(unordered_list: list) -> list:
        '''Retorna a lista ordenada e o tempo de execução do código'''

        # Primeiro definimos os intervalos da sequeência Ciura
        ciura_gaps = [1750, 701, 301, 132, 57, 23, 10, 4, 1]
        
        # Obtemos o tamanho da lista
        list_size = len(unordered_list)
        
        # Guarda a hora de INÍCIO da execução da ordenação
        start_time = time.time()
        
        for gap in ciura_gaps:
            for i in range(gap, list_size):
                
                current_element = unordered_list[i]
                element_position = i
                
                while (element_position >= gap) and (unordered_list[element_position - gap] > current_element):
                    unordered_list[element_position] = unordered_list[element_position - gap]
                    element_position -= gap
                    
                unordered_list[element_position] = current_element
               
        # Guarda a hora FINAL da execução da ordenação
        end_time = time.time()
        
        total_time = end_time - start_time

        return unordered_list, total_time
    
    def generate_list(random_end: int, list_range: int) -> list:
        '''Gera uma lista aleatória, em que list_range é o tamanho da lista e random_end é o número aleatório final'''
        
        return random.sample(list(range(list_range)), random_end)

