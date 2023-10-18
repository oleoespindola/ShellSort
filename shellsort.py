class ShellSort:
    
    def sort(unordered_list: list) -> list:
        '''Ordenação dos dados'''

        # Primeiro definimos os intervalos da sequeência Ciura
        ciura_gaps = [1750, 701, 301, 132, 57, 23, 10, 4, 1]
        
        # Obtemos o tamanho da lista
        list_size = len(unordered_list)
        
        for gap in ciura_gaps:
            for i in range(gap, list_size):
                
                current_element = unordered_list[i]
                element_position = i
                
                while (element_position >= gap) and (unordered_list[element_position - gap] > current_element):
                    unordered_list[element_position] = unordered_list[element_position - gap]
                    element_position -= gap
                    
                unordered_list[element_position] = current_element
                
        return unordered_list