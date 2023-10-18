import time, random

class ShellSort:
        
    def sort(unordered_list: list) -> (list, list, time):
        '''Retorna a lista ordenada e o tempo de execução do código'''

        # Primeiro definimos os intervalos da sequeência Ciura
        ciura_gaps = [1750, 701, 301, 132, 57, 23, 10, 4, 1]
        
        # Obtemos o tamanho da lista
        list_size = len(unordered_list)
        
        ordered_list = list(unordered_list)
        
        # Guarda a hora de INÍCIO da execução da ordenação
        start_time = time.time()
        
        for gap in ciura_gaps:
            for i in range(gap, list_size):    
            # A verificação começa somente quando um elemento da lista Ciura, maior ou igual ao tamanho da lista desordenada é localizado. 
            
                current_element = ordered_list[i]
                element_position = i
                
                while (element_position >= gap) and (ordered_list[element_position - gap] > current_element):
                    # Verifica se a posição do elemento atual está no subconjunto definido pelo intervalor Ciura
                    # E
                    # Verifica se o elemento na mesma posição, mas no sub conjunto anterior é maior que o elemento atual
                    #
                    # Qaundo as duas condições são verdadeiras, a posição atual da lista recebe o elemento do sujconjuto anterior, ou seja, a posição atual fica com o algarismo de maior valor 
                    
                    ordered_list[element_position] = ordered_list[element_position - gap]
                    element_position -= gap
                
                # Quando a condição anterior é antendida, o algarismo na posição atual, mas no subconjunto anterior, recebe o menor valor. Do contrario, a posição atual recebe o próprio elemento, ou seja, não haverá alteração.   
                ordered_list[element_position] = current_element
               
        # Guarda a hora FINAL da execução da ordenação
        end_time = time.time()
        
        # Calcula o tempo de ordenação
        total_time = end_time - start_time
        
        # Formata o tempo corrido
        hours, time_left = divmod(total_time, 3600)
        minutes, time_left = divmod(time_left, 60)
        seconds, time_left = divmod(time_left, 1)
        miliseconds = int(time_left * 1000)
        total_time = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}:{miliseconds:03d}"
        

        #retorna a lista não ordenada, ordenada e o tempo de execução
        return unordered_list, ordered_list, total_time
    
    def generate_list(list_range: int) -> list:
        '''Gera uma lista aleatória, em que list_range é o tamanho da lista e random_end é o número aleatório final'''
        
        return random.sample(list(range(list_range)), list_range)