# <img src="https://i.giphy.com/media/DDGQgJLkOlSKe08e74/giphy.webp" alt="chart" style="height: 50px"/> ShellSort

### Implementação e Uso

O módulo shellsort contém uma única classe de mesmo nome. A classe possui apenas dois métodos: generate_list e sort.

O método **generate_list** requer apenas um argumento, **list_range**, que irá definir o **tamanho da lista** e, ao mesmo tempo, a **quantidade máxima de elementos aleatórios únicos**.

Exemplo de código:

`print(ShellSort.sort(ShellSort.generate_list(10)))`

Exemplo de saída:

`([0, 1, 2, 5, 9, 4, 6, 3, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], '00:00:00:000')`

O passo-a-passo do método de ordenação está comentado no códgio, além disso, termos mnemônicos foram utilizados nos métodos e variáveis para facilitar o entendimento.

**Sinta-se à vontade para fazer Issues e pull requests com dúvidas, feedbacks e sugestões de melhorias**

_Abaixo, você encontra uam breve pesquisa para contextualiza-lo(a) sobre o assunto_
#

### Contexto 

O método de ordenação ShellSort é um algoritmo de ordenação que foi proposto por Donald Shell em 1959. Ele é uma melhoria do algoritmo de ordenação por inserção e pertence à categoria de algoritmos de ordenação por comparação. O ShellSort é conhecido por sua eficiência e é frequentemente utilizado para ordenar arrays de elementos. 

A ideia básica por trás do ShellSort é reduzir a quantidade de desordem (elementos fora de ordem) em um array de forma gradual. Isso é feito dividindo o array em subconjuntos menores, ordenando cada subconjunto com o algoritmo de inserção e, em seguida, mesclando esses subconjuntos ordenados até que o array inteiro esteja ordenado. 

A principal inovação do ShellSort é a escolha dos intervalos entre os elementos que são comparados e trocados. Em vez de usar um único intervalo constante, o algoritmo ShellSort utiliza uma sequência de intervalos decrescentes. Isso permite que elementos distantes sejam comparados e trocados antes que os elementos estejam próximos o suficiente para serem ordenados com eficiência pelo algoritmo de inserção. À medida que o algoritmo progride, os intervalos diminuem até que o array esteja completamente ordenado. 

O desempenho do ShellSort depende da sequência de intervalos escolhida. Diferentes sequências de intervalos podem afetar significativamente a eficiência do algoritmo. Uma das sequências mais comuns é a sequência de intervalos de Ciura, que foi desenvolvida para otimizar o desempenho do ShellSort em uma ampla gama de situações. 

O ShellSort não é um algoritmo de ordenação estável. Isso significa que a ordem relativa de elementos com chaves iguais pode não ser preservada após a ordenação. 

Em resumo, o ShellSort é um algoritmo de ordenação eficiente que se baseia na redução gradual da desordem em um array por meio do uso de intervalos variáveis. Ele é uma melhoria em relação ao algoritmo de ordenação por inserção, embora existam outros algoritmos de ordenação mais eficientes em muitas situações. 

### Sequência de intervalos Ciura  

A sequência de intervalos Ciura, também conhecida como sequência de intervalos de Ciura, é uma sequência de números usada no algoritmo de ordenação ShellSort para determinar os intervalos de comparação e troca entre os elementos do array. Essa sequência foi proposta por Marcin Ciura em seu artigo "Best Increments for the Average Case of Shellsort" em 2001. A sequência de intervalos de Ciura é conhecida por seu desempenho eficiente em uma ampla variedade de casos. 

Os intervalos na sequência de Ciura são escolhidos com base em extensos experimentos e análises de desempenho. Eles são projetados para garantir que o ShellSort funcione bem em muitos cenários diferentes. Aqui está a sequência de intervalos de Ciura: 

`1, 4, 10, 23, 57, 132, 301, 701, 1750`

Essa sequência de intervalos permite que o ShellSort comece com intervalos maiores para realizar comparações amplas entre os elementos e, em seguida, diminua gradualmente esses intervalos à medida que o algoritmo avança. A sequência de Ciura é especialmente eficaz para evitar o pior caso de desempenho, que pode ocorrer com algumas sequências de intervalos. 

#

#### FONTES 

Donald Shell. A High-Speed Sorting Procedure. Communications of the ACM, 2(7):30-32, 1959. 
Robert Sedgewick. Algorithms in Java, Part 1–4. Addison-Wesley, 2011
