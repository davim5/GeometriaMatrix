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
        try:
            i, j = key
            if self.rows < 0:
                raise Exception('Numero de linhas não é compatível')
            if self.cols < 0:
                raise Exception('Numero de colunas não é compatível')
            #print(key)
            return self.data[(j-1) + (i-1) * self.cols]
        except IndexError:
            print('Não existe a linha/coluna nessa matriz')
        

    #Método para definir um dos valores da matriz
    def __setitem__(self, key, value):
        try:
            i, j = key
            self.data[(j-1) + (i-1) * self.cols] = value
        except IndexError:
            print("Não existe a linha/coluna nessa matriz")


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

    def __rsub__(self, other):
        return self.__sub__(other)

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

    def __rmul__(self, other):
        return self.__mul__(other)        

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

    def __rtruediv__(self, other):
        return self.__truediv__(other)

#Cij += Aik * Bkj

    def dot(self,other):
        try:
            if self.cols != other.rows:
                raise Exception('Número de linhas e colunas é incompatível para multiplicação!')
        except Exception:
            raise

        else:
            res = Matrix(self.rows,other.cols)

            for k in range(1,self.cols + 1):
                for i in range(1, self.rows + 1):
                    for j in range(1,other.cols + 1):
                        res[i,j] += self[i,k] * other[k,j]
            return res

    def transpose(self):

        res = Matrix(self.cols,self.rows)

        for i in range(1, self.rows+1):
            for j in range(1, self.cols+1):
                res[j,i] = self[i,j]

        return res


    def gauss_jordan(self):

        if self.cols == self.rows + 1:
            # print('entrou primeiro if') #teste
            res = self

            for j in range(1,self.cols): #Colunas menos a ultima (1 a 3)
                # print('j = ',j)
                for i in range(1,self.rows+1): #Linhas até a diagonal principal (3 a 1)
                    # print('i = ', i,' j = ',j)
                    if(res[1,1]==0):
                        # print('entrou')
                        g = 2
                        while (res[g,1] == 0):
                            g += 1
                        for s in range(1, self.cols + 1):
                            aux = res[i,s]
                            res[i,s] = res[g,s]
                            res[g,s] = aux  
                        # print(res)          
                    #Diagonal principal
                    if(i==j):
                        # print('entrou if do i==j')
                        if(res[i,j] != 1):
                            # print('entrou if do res[i,j] != 1')
                            div = res[i,j] #Numero valor do numero da posição
                            for s in range(1, self.cols + 1): #Colunas para a conta
                                res[i,s] /= div   
                            # print(res)
                    #Abaixo da Diagonal principal
                    elif(i > j):
                        if(res[i,j] != 0):
                            # print('entrou if do res[i,j] != 0')
                            #CALCULO PRA DEIXAR IGUAL A 0
                            if(j==1):
                                x = 1 #variável para a linha que será utilizada para somar com a linha 'i'
                            else: 
                                x = j
                            mult = (res[i,j] *(-1))/res[x,j] #multiplicador para linha que irá somar e zerar o elemento [i,j]
                            for s in range(1, self.cols + 1): #'s' colunas para somar cada elemento da linha
                                res[i,s] += res[x,s]*mult
                            # print(res)
                            
            # print("Voltando acima da diagonal agora")
            for j in range(self.cols - 1, 1,-1): #Da penultima coluna até a segunda
                # print('j = ',j)
                for i in range(self.rows - 1, 0, -1): #Linhas acima da diagonal principal
                    # print('i = ', i,' j = ',j)
                    
                    #Acima da diagonal principal
                    if(j > i):
                        if(res[i,j] != 0):
                            # print('entrou if do res[i,j] != 0')
                            #CALCULO PRA DEIXAR IGUAL A 0
                            x = j
                            mult = (res[i,j] *(-1))/res[x,j] #multiplicador para linha que irá somar e zerar o elemento [i,j]
                            for s in range(1, self.cols + 1): #'s' colunas para somar cada elemento da linha
                                res[i,s] += res[x,s]*mult
                            # print(res)
        
        if self.cols == self.rows:
            # print('entrou primeiro if') #teste
            res = self

            for j in range(1,self.cols+1): #Colunas menos a ultima (1 a 3)
                # print('j = ',j)
                for i in range(1,self.rows+1): #Linhas até a diagonal principal (3 a 1)
                    # print('i = ', i,' j = ',j)
                    if(res[1,1]==0):
                        # print('entrou')
                        g = 2
                        while (res[g,1] == 0):
                            g += 1
                        for s in range(1, self.cols + 1):
                            aux = res[i,s]
                            res[i,s] = res[g,s]
                            res[g,s] = aux  
                        # print(res)          
                    #Diagonal principal
                    if(i==j):
                        # print('entrou if do i==j')
                        if(res[i,j] != 1):
                            # print('entrou if do res[i,j] != 1')
                            div = res[i,j] #Numero valor do numero da posição
                            for s in range(1, self.cols + 1): #Colunas para a conta
                                res[i,s] /= div   
                            # print(res)
                    #Abaixo da Diagonal principal
                    elif(i > j):
                        if(res[i,j] != 0):
                            # print('entrou if do res[i,j] != 0')
                            #CALCULO PRA DEIXAR IGUAL A 0
                            if(j==1):
                                x = 1 #variável para a linha que será utilizada para somar com a linha 'i'
                            else: 
                                x = j
                            mult = (res[i,j] *(-1))/res[x,j] #multiplicador para linha que irá somar e zerar o elemento [i,j]
                            for s in range(1, self.cols + 1): #'s' colunas para somar cada elemento da linha
                                res[i,s] += res[x,s]*mult
                            # print(res)
                            
            # print("Voltando acima da diagonal agora")
            for j in range(self.cols, 1,-1): #Da penultima coluna até a segunda
                # print('j = ',j)
                for i in range(self.rows - 1, 0, -1): #Linhas acima da diagonal principal
                    # print('i = ', i,' j = ',j)
                    
                    #Acima da diagonal principal
                    if(j > i):
                        if(res[i,j] != 0):
                            # print('entrou if do res[i,j] != 0')
                            #CALCULO PRA DEIXAR IGUAL A 0
                            x = j
                            mult = (res[i,j] *(-1))/res[x,j] #multiplicador para linha que irá somar e zerar o elemento [i,j]
                            for s in range(1, self.cols + 1): #'s' colunas para somar cada elemento da linha
                                res[i,s] += res[x,s]*mult
                            # print(res)
        
        return res

    def inverse(self):

        if self.cols == self.rows:
            
            # Criando matriz com o dobro de colunas para a matriz identidade ficar junta
            res = Matrix(self.rows,2*self.cols)
        
            # Setando os valores da matriz originais com a identidade
            for i in range(1,res.rows+1):
                for j in range(1, res.cols+1):
                    print('i = ',i,'j = ',j)
                    if(j <= self.cols): #Matriz Original (self)
                        res[i,j] = self[i,j]
                    elif(i == j - self.cols): #Diagonal da matriz identidade (1's)
                        res[i,j] = 1
                    else:   #Resto da matriz identidade (0's)
                        res[i,j] = 0

            for j in range(1,self.cols+1): #Colunas com a ultima
                    print('j = ',j)
                    for i in range(1,self.rows+1): #Linhas até a diagonal principal (1 a 3)
                        print('i = ', i,' j = ',j)
                        
                        #Diagonal principal
                        if(i==j):
                            print('entrou if do i==j')
                            if(res[i,j] != 1):
                                print('entrou if do res[i,j] != 1')
                                div = res[i,j] #Numero valor do numero da posição
                                for s in range(1, res.cols + 1): #Colunas para a conta
                                    res[i,s] /= div   
                                print(res)
                        #Abaixo da Diagonal principal
                        elif(i > j):
                            if(res[i,j] != 0):
                                print('entrou if do res[i,j] != 0')
                                #CALCULO PRA DEIXAR IGUAL A 0
                                if(j==1):
                                    x = 1 #variável para a linha que será utilizada para somar com a linha 'i'
                                else: 
                                    x = i - 1
                                mult = (res[i,j] *(-1))/res[x,j] #multiplicador para linha que irá somar e zerar o elemento [i,j]
                                for s in range(1, res.cols + 1): #'s' colunas para somar cada elemento da linha
                                    res[i,s] += res[x,s]*mult
                                print(res)
            print("Voltando acima da diagonal agora")
            for j in range(self.cols, 1,-1): #Da penultima coluna até a segunda
                print('j = ',j)
                for i in range(self.rows - 1, 0, -1): #Linhas acima da diagonal principal
                    print('i = ', i,' j = ',j)
                    
                    #Acima da diagonal principal
                    if(j > i):
                        if(res[i,j] != 0):
                            print('entrou if do res[i,j] != 0')
                            #CALCULO PRA DEIXAR IGUAL A 0
                            x = j
                            mult = (res[i,j] *(-1))/res[x,j] #multiplicador para linha que irá somar e zerar o elemento [i,j]
                            for s in range(1, res.cols + 1): #'s' colunas para somar cada elemento da linha
                                res[i,s] += res[x,s]*mult
                            print(res)
                        
            resreal = Matrix(self.rows,self.cols)
            for i in range(1,self.rows+1):
                for j in range(1,self.cols+1):
                    print('Vai até i = ',i,' j = ',j)
                    resreal[i,j] = res[i,j+self.cols]

            return resreal   

        else:
            print('Matriz inserida não é quadrada')     

    def LU(self):
        
        res = self
        L = Matrix(res.rows,res.cols)
        U = Matrix(res.rows,res.cols)

        if self.cols == self.rows:
            # print('entrou primeiro if') #teste
            res = self

            for j in range(1,self.cols+1): #Colunas menos a ultima (1 a 3)
                # print('j = ',j)
                for i in range(1,self.rows+1): #Linhas até a diagonal principal (3 a 1)
                    # print('i = ', i,' j = ',j)
                    if(res[1,1]==0):
                        # print('entrou')
                        g = 2
                        while (res[g,1] == 0):
                            g += 1
                        for s in range(1, self.cols + 1):
                            aux = res[i,s]
                            res[i,s] = res[g,s]
                            res[g,s] = aux  
                        # print(res)          
                    #Diagonal principal
                    if(i==j):
                        # print('entrou if do i==j')
                        if(res[i,j] != 1):
                            # print('entrou if do res[i,j] != 1')
                            div = res[i,j] #Numero valor do numero da posição
                            L[i,j] = div
                            for s in range(1, self.cols + 1): #Colunas para a conta
                                res[i,s] /= div   
                            # print(res)
                        else:
                            L[i,j] = 1
                    #Abaixo da Diagonal principal
                    elif(i > j):
                        if(res[i,j] != 0):
                            # print('entrou if do res[i,j] != 0')
                            #CALCULO PRA DEIXAR IGUAL A 0
                            if(j==1):
                                x = 1 #variável para a linha que será utilizada para somar com a linha 'i'
                            else: 
                                x = j
                            mult = (res[i,j] *(-1))/res[x,j] #multiplicador para linha que irá somar e zerar o elemento [i,j]
                            L[i,j] = mult*-1
                            for s in range(1, self.cols + 1): #'s' colunas para somar cada elemento da linha
                                res[i,s] += res[x,s]*mult
                            # print(res)
                print(L)
                U = res
            # print("Voltando acima da diagonal agora")
            for j in range(self.cols, 1,-1): #Da penultima coluna até a segunda
                # print('j = ',j)
                for i in range(self.rows - 1, 0, -1): #Linhas acima da diagonal principal
                    # print('i = ', i,' j = ',j)
                    
                    #Acima da diagonal principal
                    if(j > i):
                        if(res[i,j] != 0):
                            # print('entrou if do res[i,j] != 0')
                            #CALCULO PRA DEIXAR IGUAL A 0
                            x = j
                            mult = (res[i,j] *(-1))/res[x,j] #multiplicador para linha que irá somar e zerar o elemento [i,j]
                            U[i,j] = mult*-1
                            for s in range(1, self.cols + 1): #'s' colunas para somar cada elemento da linha
                                res[i,s] += res[x,s]*mult
                            # print(res)
                print(U)
        

        #self.data[(j-1) + (i-1) * self.cols] = valuee=
        #no prompt: 'python'(na pasta do arquivo), 'from matrix import Matrix', 'exit' , 'exit()'


# **** PRINT DOS TEMPOS NA TELA **** 

# import time

# # for q in range(1,21):
#     # nomearquivo = "pack6/packs/pack6/ex0"+str(q)+".m-ext.m"
# nomearquivo = "pack6/packs/pack6/ex020.m-ext.m"

# f = open(nomearquivo,"r") #TIRAR OS COM766                                              y ENTARIOS DO ARQUIVO ANTES DE PASSAR
# x = f.readline().split()
# print('Questão 20 : ',x, 'file: ',nomearquivo)
# i = int(x[0])
# j = int(x[1])

# a = Matrix(i,j)
# # print('i = ', i,' j = ', j)

# for z in range(1,i*j+1):
#     x = f.readline().split()
#     i = int(x[0])
#     j = int(x[1])
#     n = int(x[2])
#     a[i,j] = n
#     # print('i = ', i,' j = ', j)
    
# start_time = time.time()
# # print(a)
# b = a.gauss_jordan()
# # print(b)
# end_time = time.time() - start_time

# if(end_time > 60):
#     end_timem = end_time/60
# else:
#     end_timem = 0

# print(end_time,'Segundos ou ',end_timem,' Minutos')

