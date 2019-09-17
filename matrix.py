#Criação de uma classe 'matrix'
class Matrix:
    #Método inicializador 'def' , vai forçar o usuário a definir as linhas e colunas ao inicializar
    #Todo método começa com (self,)
    #def nomedometodo(self, 'parametro que vai ser passado')
    #"data = []", parametro opicional: se não for declarado, será inicializado como "[]"
    def __init__(self, rows, cols, data = []): # ':', significa que encerrou a definição do método
        if type(rows) != int or type(cols) != int:
            print('O valor passado não é um número!')
            return
        if rows < 0 or cols < 0:
            print('Numero de linhas ou colunas inválido, deve ser positivo.')
            return
        self.rows = rows
        self.cols = cols
        
        if data:
            self.data = data
        else:
            self.data = [0] * (self.rows * self.cols)
        
        
    #Tratar:
    # Não exceder o numero de valores possíveis na matrix na sua definição. OK
    # Permitir somente get e set em espaços possíveis na matrix.
    # Soma com int ou float(Mesmo valor modifica elemento a elemento). OK

    #try:
    #if:
    #...
    #else:
    #raise exception:--



    #Método para retornar o elemento(i,j) da matriz
    def __getitem__(self, key):
        
            i, j = key
            if self.rows < 0:
                raise Exception('Numero de linhas não é compatível')
            if self.cols < 0:
                raise Exception('Numero de colunas não é compatível')
            #print(key)
            return self.data[(j-1) + (i-1) * self.cols]
        

    #Método para definir um dos valores da matriz
    def __setitem__(self, key, value):
        i, j = key
        self.data[(j-1) + (i-1) * self.cols] = value

    def __repr__(self):
        print('')
        for i in range(1, self.rows+1):
            for j in range(1,self.cols+1):
                print("{0:.4f}".format(self[i,j]),end="   ")
            print('')

        return ''


    def __radd__(self,other):

        return self.__add__(other)
        

    #usar 'type()' para adicionar opção elemento a elemento

    def __add__(self,other):
        if type(other) == Matrix:
            res = Matrix(self.rows, self.cols)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i,j] = self[i,j] + other[i,j]

            return res

        elif type(other) == int or type(other) == float:
            res = Matrix(self.rows, self.cols)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i,j] = self[i,j] + other
            return res

        else:
            print('Elemento não compatível para operação!')

            return 
                
    def __sub__(self,other):
        if type(other) == Matrix:
            res = Matrix(self.rows, self.cols)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i,j] = self[i,j] - other[i,j]

            return res

        elif type(other) == int or type(other) == float:
            res = Matrix(self.rows, self.cols)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i,j] = self[i,j] - other
            return res

        else:
            print('Elemento não compatível para operação!')

            return 

                

        return res

    def __mul__(self,other):
        if type(other) == Matrix:
            res = Matrix(self.rows, self.cols)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i,j] = self[i,j] * other[i,j]

            return res

        elif type(other) == int or type(other) == float:
            res = Matrix(self.rows, self.cols)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i,j] = self[i,j] * other
            return res

        else:
            print('Elemento não compatível para operação!')

            return 

    def __truediv__(self,other):
        if type(other) == Matrix:
            res = Matrix(self.rows, self.cols)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    if other[i,j] == 0:
                        print('Valor não pode divir por 0!')
                        return
                    else:
                        res[i,j] = self[i,j] / other[i,j]
            return res

        elif type(other) == int or type(other) == float:
            res = Matrix(self.rows, self.cols)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    if other == 0:
                        print('Valor não pode divir por 0!')
                        return
                    else: 
                        res[i,j] = self[i,j] / other
            return res

        else:
            print('Elemento não compatível para operação!')

            return 

#Cij += Aik * Bkj

    def _dot_(self,other):
        if self.cols != other.rows:
            print('Número de linhas e colunas é incompatível para multiplicação!')
            return
        else:
            res = Matrix(self.rows,other.cols)

            for k in range(1,self.cols + 1):
                for i in range(1, self.rows + 1):
                    for j in range(1,other.cols + 1):
                        res[i,j] += self[i,k] * other[k,j]
            return res


    def solve(self):
        #checa se a matriz tem a ultima coluna "b" para que as operações sejam feitas
        if self.cols == self.rows + 1:
            #Variável recebe a raiz passada na função
            res = self
            
            #Checar se os termos abaixo da diagonal principal estão zerados
            for j in range(1,self.cols): #Colunas menos a ultima (1 a 3)
                print('loop 1')

                for i in range(self.rows,j,-1): #Linhas até antes da diagonal principal (3 a 1)
                    print('loop 2 --- ','i = ',i,' j = ',j)
                    print('res[i,j] = ',res[i,j])

                    # if(res[j,j] == 0):
                    #     aux = res
                    #     for x in range(1, self.cols):
                    #         res[j-1,x] = aux[j,x]
                            
    
                    
                    if res[i,j] != 0: #Se encontrar um que não seja 0 (i = linha, j = coluna)

                        for k in range(1, self.rows + 1): #k = variavel pra checar outras linhas da mesma coluna 'j'
                            print('loop 3 --- k = ',k)
                            print('res[k,j] = ',res[k,j])
                            print(res.data,'\n')

                            al = k

                            if(res[i,j-1] == 0):
                                print('Leu que o antes é zero')
                                while(res[al,j-1] != 0):
                                    al += 1
                                    print(al)

                            print(al)
                            if res[i,j] == res[al,j] and i != al and res[i,j] != 0: #Se for igual e não for a mesma linha
                                print('al = ', al)

                                for s in range (1,self.cols+1): #s = variavel pra pegar cada elemento da linha 'i' e subtrair com a linha 'k' até chegar na diagonal
                                    print('loop 4 == --- s = ',s)
                                    res[i,s] -= res [al,s]
                                    #resultado deve ser zero
                                print('\n')            
                            elif res[i,j] < res[al,j] and res[i,j] != 0: #Se lemento da outra linha for maior
                                print('al = ', al)
                                if res[al,j]%res[i,j] == 0:
                                    div = res[al,j]/res[i,j]
                                    for s in range(1,self.cols+1):
                                        print('loop 4 < --- s = ',s)
                                        res[i,s] -= res[al,s]/div
                                    print('\n')
                            elif res[i,j] > res[al,j]: #Se lemento da outra linha for maior
                                print('al = ', al)
                                if res[i,j]%res[al,j] == 0:
                                    mult = res[i,j]/res[al,j]
                                    for s in range(1,self.cols+1):
                                        print('loop 4 > --- s = ',s)
                                        res[i,s] -= res[al,j]*mult
                                    print('\n')
            for j in range(1,self.cols): #Colunas menos a ultima (1 a 3)
                print('loop 1')

                for i in range(self.rows,j,-1): #Linhas até antes da diagonal principal (3 a 1)
                    print('loop 2 --- ','i = ',i,' j = ',j)
                    print('res[i,j] = ',res[i,j])

                    # if(res[j,j] == 0):
                    #     aux = res
                    #     for x in range(1, self.cols):
                    #         res[j-1,x] = aux[j,x]
                    
                    if res[i,j] != 0: #Se encontrar um que não seja 0 (i = linha, j = coluna)

                        for k in range(1, self.rows + 1): #k = variavel pra checar outras linhas da mesma coluna 'j'
                            print('loop 3 --- k = ',k)
                            print('res[k,j] = ',res[k,j])
                            print(res.data,'\n')

                            al = k

                            if(res[i,j-1] == 0):
                                print('Leu que o antes é zero')
                                while(res[al,j-1] != 0):
                                    al += 1
                                    print(al)

                            print(al)
                            if res[i,j] == res[al,j] and i != al and res[i,j] != 0: #Se for igual e não for a mesma linha
                                print('al = ', al)

                                for s in range (1,self.cols+1): #s = variavel pra pegar cada elemento da linha 'i' e subtrair com a linha 'k' até chegar na diagonal
                                    print('loop 4 == --- s = ',s)
                                    res[i,s] -= res [al,s]
                                    #resultado deve ser zero
                                print('\n')            
                            elif res[i,j] < res[al,j] and res[i,j] != 0: #Se lemento da outra linha for maior
                                print('al = ', al)
                                if res[al,j]%res[i,j] == 0:
                                    div = res[al,j]/res[i,j]
                                    for s in range(1,self.cols+1):
                                        print('loop 4 < --- s = ',s)
                                        res[i,s] -= res[al,s]/div
                                    print('\n')
                            elif res[i,j] > res[al,j]: #Se lemento da outra linha for maior
                                print('al = ', al)
                                if res[i,j]%res[al,j] == 0:
                                    mult = res[i,j]/res[al,j]
                                    for s in range(1,self.cols+1):
                                        print('loop 4 > --- s = ',s)
                                        res[i,s] -= res[al,j]*mult
                                    print('\n')
        return res

            #Zerar termos abaixo da diagonal principal OOOOK

                #sendo 'm' e 'n', respectivamente, os ultimos valores de linhas e colunas OKOOK
                #Zerar primeiro res[m,n] até res[n+1,n] (EXEMPLO: [4,1] até [2,1], depois [4,2] até [3,2]... Sempre da primeira linha da coluna até o 'meio'. OOOKOK

            #Checar se os termos da diagonal principal são '1'

            #Transformar os termos da diagonal principal para '1'

            #Zerar os termos acima da diagonal principal.
# diosaidos
    #self.data[(j-1) + (i-1) * self.cols] = value
    #no prompt: 'python'(na pasta do arquivo), 'from matrix import Matrix', 'exit' , 'exit()'