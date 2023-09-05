"""PROGRAM DONE BY RAFAEL ANDANT"""

import sys
sys.path

"""In this sector you need to specify de path of the POLY program"""

path = 'path to POLY'
if not (path in sys.path):
    sys.path.append(path)

import importlib
pl = importlib.import_module(name = "POLY")



class myarray:
    
    def __init__(self, elems, r, c, by_row=True):
        self.elems = elems
        self.r = r
        self.c = c
        self.by_row = by_row
        
    def myprint(self):
        print('\n')
        for k in range(0,self.r):
            print(self.get_row(k))
        print('\n')
        return None

    """The get_pos method takes two arguments: j, which is the row index, and k, which is the column index. Then it returns the position, both columns and Rows start from 0. So the result also starts from 0 """

    def get_pos(self, j, k):
        if self.by_row:
            return j * self.c + k 
        else:
            return k * self.r + j 

#%%
    
    """ __eq__ that defines the behavior of the == operator for objects of the myarray class."""

    def __eq__(self, other):
        return self.elems==other.elems and self.r==other.r and self.c==other.c and self.by_row==other.by_row   

    """ get_coords receives m, an index and returns the coordinates of the index by taking """

    def get_coords(self, m):
        if self.by_row:
            j = m // self.c
            k = m % self.c
        else:
            k = m // self.r
            j = m % self.r
        return (j, k)
    
#%%

    """ switch function alters the list of elems by changing the by_row value"""

    def switch(self):
        new_elems = self.elems[::-1]
        new_by_row = not self.by_row
        return myarray(new_elems, self.c, self.r, new_by_row)
    
#%%
    
    """ get_row , get_col and get_elem work by iterating through the matrix and adding the corresponding elements to the list"""

    def get_row (self, j):
        lista1=[]
        if j <= self.r:
            for k in range(self.c):
                lista1.append(self.elems[self.get_pos(j, k)])
            return lista1 
        else:
            return "Error"
    
    def get_col (self, k):
        lista2=[]
        if k <= self.c:
            for j in range(self.r):
                lista2.append(self.elems[self.get_pos(j,k)])
            return lista2
        
    def get_elem(self, j, k):
        pos1= self.get_pos(j, k)
        elem1= self.elems[pos1]
        return elem1
    
#%%

    """ del_row and col iterate again through the matrix and add the elements not selected to de new elements list"""

    def del_row(self, j):
       new_elems = []
       for i in range(self.r):
           if i != j:
               new_row = []
               for k in range(self.c):
                   new_row.append(self.elems[self.get_pos(i, k)])
               new_elems.extend(new_row)
       return myarray(new_elems, self.r-1, self.c, self.by_row)
    
    def del_col(self, k):
        new_elems = []
        for j in range(self.r):
            for i in range(self.c):
                if i != k:
                    new_elems.append(self.elems[self.get_pos(j, i)])
        return myarray(new_elems, self.r, self.c-1, self.by_row)
    
#%%
    
    """Swap_rows and cols receives the indexes of two rows (or columns) and creates a new_elems list with the rows exchanged. """

    def swap_rows(self, j, k):
        if j < self.r and k < self.r:
            new_elems = self.elems.copy()
            for i in range(self.c):
                pos_j = self.get_pos(j, i)
                pos_k = self.get_pos(k, i)
                new_elems[pos_j], new_elems[pos_k] = new_elems[pos_k], new_elems[pos_j]
            return myarray(new_elems, self.r, self.c, self.by_row)
        else:
            return "Error"
        
    def swap_cols(self, l, m):
        if l < self.r and m < self.r:
            new_elems = self.elems.copy()
            for i in range(self.r):
                pos_l = self.get_pos(i, l)
                pos_m = self.get_pos(i, m)
                new_elems[pos_l], new_elems[pos_m] = new_elems[pos_m], new_elems[pos_l]
            return myarray(new_elems, self.c, self.r, self.by_row)
        else:
            return "Error"
        
#%%
    
    """ Scale functions take a scale factor and multiply it by the corresponding row or col. It works by taking the selected row or column, multiplying it by the factor and adding making a new list with the updated rows and cols"""

    def scale_row(self, k, y):
        new_elems = []
        for j in range(self.r):
            for i in range(self.c):
                if j == k:
                    new_elems.append(y * self.elems[self.get_pos(j, i)])
                else:
                    new_elems.append(self.elems[self.get_pos(j, i)])
        return myarray(new_elems, self.r, self.c, self.by_row)

    
    def scale_col(self, k, y):
        new_elems = []
        for j in range(self.r):
            for i in range(self.c):
                if i == k:
                    new_elems.append(y * self.elems[self.get_pos(j, i)])
                else:
                    new_elems.append(self.elems[self.get_pos(j, i)])
        return myarray(new_elems, self.r, self.c, self.by_row)
    
#%%
    
    """Transpose works in a very similar way with switch, the only difference is that we do not alter the boolean format"""

    def transpose(self):
        new_elems = []
        if self.by_row:
            for j in range(self.c):
                for i in range(self.r):
                    pos = self.get_pos(i, j)
                    new_elems.append(self.elems[pos])
            return myarray(new_elems, self.c, self.r, self.by_row)
        else:
            for j in range(self.r):
                for i in range(self.c):
                    pos = self.get_pos(j, i)
                    new_elems.append(self.elems[pos])
            return myarray(new_elems, self.c, self.r, self.by_row)

#%%
    
    """ The flip function works by flipping the first row with the last one, the second with the third one and so on. It uses the swap functions. """

    def flip_cols(self):
        new_matrix = []
        for j in range(1,self.c+1):
            new_matrix += self.get_col(self.c - j)
        new_matrix1 = myarray(elems=new_matrix,r=self.r,c=self.c,by_row=False)
        if self.by_row: 
            new_matrix1.switch()
        return new_matrix1    
    
    def flip_row(self):
        new_matrix = self
        for j in range(self.r//2):
            k = self.r - 1 - j
            new_matrix = new_matrix.swap_rows(j, k)
        return new_matrix
    
#%%
    
    """The submatrix function deletes the j0 rows and k0 cols and returns a sub matrix that will be used in the det funtion (use un poco de ayuda de Stack Overflow y de Fer para armarlo, pero el codigo es mio)"""

    def submatrix(self, j0, k0):
        elems1 = [self.get_elem(j, k) for j in range(self.r) for k in range(self.c) if j != j0 and k != k0]
        r1 = self.r - 1
        c1 = self.c - 1
        return myarray(elems1, r1, c1, by_row=True)
    
    """ The det funtion iterates over the first row and computes the cofactor of each element that the submatrix returned. Ater that it multiplies it by the corresponding element of the first row and so on."""
    
    def det(self):
        if self.r != self.c:
            return "Error"
        elif self.r == 1:
            return self.elems[0]
        elif self.r == 2:
            return self.elems[0]*self.elems[3] - self.elems[1]*self.elems[2]
        else:
            det = 0
            sign = 1
            for k in range(self.c):
                submatrix = self.submatrix(0, k)
                subdet = submatrix.det()
                det += sign * self.elems[k] * subdet
                sign *= -1
            return det
        
#%%

    """The add function, receives a scalar and sums it to all the elements in the matrix. """

    def __add__(self, B):
        if isinstance(B, myarray):
            if self.r != B.r or self.c != B.c:
                print ("Matrices must have the same dimensions.")
                elems = None
            else:
                elems = [a + b for a, b in zip(self.elems, B.elems)]
        elif isinstance(B, (int, float, pl.poly)):
            elems = [a + B for a in self.elems]
        else:
            print ("Can't multiply this type of object")
            elems = None
        return myarray(elems, self.r, self.c, self.by_row)

#%%
    
    """The substarct function is the same function as the __add__ but basically instead of a+B is a-B"""
    
    def __sub__(self, B):
        if isinstance(B, myarray):
            if self.r != B.r or self.c != B.c:
                print ("Matrices must have the same dimensions.")
                elems = None
            else:
                elems = [a - b for a, b in zip(self.elems, B.elems)]
        elif isinstance(B, (int, float, pl.poly)):
            elems = [a - B for a in self.elems]
        else:
            print ("Can't subtract this type of object")
            elems = None
        return myarray(elems, self.r, self.c, self.by_row)
    
#%%

    """Again the __mul__ function is the same function as the __add__ but basically instead of a+B is a*B"""
    
    def __mul__(self, B):
        if isinstance(B, myarray):
            if self.r != B.r or self.c != B.c:
                print ("Matrices must have the same dimensions.")
                elems = None
            else:
                elems = [a * b for a, b in zip(self.elems, B.elems)]
        elif isinstance(B, (int, float, pl.poly)):
            elems = [a * B for a in self.elems]
        else:
            print ("Can't multiply this type of object")
            elems = None
        return myarray(elems, self.r, self.c, self.by_row)


    
#%%
    
    """The __matmul__ funtion is a little bit more complex. Firstly it gets in the range of the rows of the original matrix, then it gets into de columns of the new matrix and the it multiplies the first with the first elem, etc. Finally it sums it up and appends them to the elems list"""

    def __matmul__(self, B):
        if isinstance(B, myarray):
            if self.c != B.r:
                raise  ValueError("Number of columns of the first matrix must equal the number of rows of the second matrix.")
            else:
                elems = []
                for i in range(self.r):
                    for j in range(B.c):
                        s = 0
                        for k in range(self.c):
                            s += self.elems[self.get_pos(i, k)] * B.elems[B.get_pos(k, j)]
                        elems.append(s)
        else:
            print ("Can't add this type of object")
        return myarray(elems, self.r, B.c, self.by_row)
    

#%%

    """The __pow__ function firstly creates a result full of 0's and then changes the elements by the matrix elems powered by the scale factor. """
    
    def __pow__(self, n):
        if not isinstance(n, (int, float)):
            print ("Exponent must be a number.")
        
        result = [0] * (self.r * self.c)
        
        if self.by_row:
            for i in range(self.r):
                for j in range(self.c):
                    result[self.get_pos(i, j)] = self.elems[self.get_pos(i, j)] ** n
        else:
            for j in range(self.c):
                for i in range(self.r):
                    result[self.get_pos(i, j)] = self.elems[self.get_pos(i, j)] ** n
        
        return myarray(result, self.r, self.c, self.by_row)

#%%
    
    """The identity matrix, normally makes the simple generic identity, but when del_row is being used, it substracts the corresponding row from the identity matrix, and when swap is being used, it just swaps the corresponding rows from the identity"""
    @staticmethod
    def identity(n, del_row=None, swap_row=None, make_0=None):
        new_elems=[1]
        if del_row is None:
            a=0
            for i in range(n):
                new_elems += n*[0] + [1] 
        else:
            a=1
            for i in range(n):
                if i != (del_row-1) and i != del_row:
                    new_elems += n*[0] + [1]
                elif i==del_row:
                    new_elems += (n+1) * [0] + [1]
    
        salida = myarray(new_elems, n - a , n, True)
        if swap_row is not None:
            salida = salida.swap_rows(*swap_row)
        if make_0 is not None:
            salida = (1)
        return salida

#%%
    
    """After the hard part of the identity ajustments, we just call the modified identity, and premultiply it by the original matrix. The same with del_col, the only difference is that it has to be transposed and it is a postmultiplication"""

    def del_row1(self, j):
        if j < 0 or j >= self.r:
            raise (ValueError("Invalid row index."))
        
        identity1= self.identity(self.r, j)
        
        new_matrix = identity1 @ self
        return new_matrix
    
    def del_col1(self, k):
        if k < 0 or k >= self.c:
            raise (ValueError("Invalid row index."))
        
        identity1= self.identity(self.c, k).transpose()
        
        new_matrix = self @ identity1
        return new_matrix

#%%

    """The swap rows relies again in calling the old functions of swap, but the old functions just modify the identity, once the identity is modified, we premultiply it (if it's rows) by the original matrix and the new swap is done"""

    def swap_rows1 (self, j, i):
        if j < 0 or j >= self.r:
            raise (ValueError("Invalid row index."))
        
        identity1= self.identity(self.r, swap_row=(i, j))
        
        new_matrix = identity1 @ self
        return new_matrix
    
    def swap_cols1 (self, k, u):
        if k < 0 or k >= self.c:
            raise (ValueError("Invalid row index."))
        
        identity1= self.identity(self.c, swap_row=(u, k)).transpose()
        
        new_matrix = self @ identity1
        return new_matrix

#%%

    def add_rows(self, j, i, coef=1):
        if j < 0 or j >= self.r:
            raise (ValueError("Invalid row index."))
        if i < 0 or i >= self.r:
            raise (ValueError("Invalid row index."))
        new_elems = list(self.elems)
        for k in range(self.c):
            pos1 = self.get_pos(j, k)
            pos2 = self.get_pos(i, k)
            new_elems[pos1] += coef * new_elems[pos2]
        return myarray(new_elems, self.r, self.c, self.by_row)

        
    def inverse(self):
        # Check if matrix is square
        if self.r != self.c:
            print("Matrix must be square")
            return None
            
        identity = self.identity(self.r)
        new_matrix = myarray(self.elems.copy(), self.r, self.c)
            
        for i in range(self.c):
            pivot = None
            pivot_row = None
            for x in range(i, self.r):
                if new_matrix.get_elem(x, i) != 0:
                    pivot = new_matrix.get_elem( x, i)
                    pivot_row = x
                    break
                
            if pivot is None:
                print("Matrix is singular, has no inverse")
                return None
                
            if pivot_row != i:
                new_matrix = new_matrix.swap_rows1(pivot_row, i)
                identity = identity.swap_rows1(pivot_row, i)
                
            scale = 1 / pivot
            new_matrix = new_matrix.scale_row(i, scale)
            identity = identity.scale_row(i, scale)
                
            for j in range(self.r):
                if j != i:
                    coef = new_matrix.get_elem(j, i)
                    new_matrix = new_matrix.add_rows(j, i, -coef)
                    identity = identity.add_rows(j, i, -coef)
            
        return identity


#%%

    def cuadratic_form (self, x):
        type (x) == myarray
        self.r == self.c
        self.c == x.r
        
        salida1 = x.transpose()
        salida2 = self @ x
        salida3 = salida1 @ salida2
        
        return salida3
    
#%%

    def poly_car(self):
        if self.c == self.r:
            iden = self.identity(self.r)
            lambdaiden = iden * pl.poly(1, [0,1])
            resta = self - lambdaiden
            Polinomio_Caracteristico = resta.det()
        else:
            raise ValueError ("Martrices must be square")
            Polinomio_Caracteristico = None
            
        return Polinomio_Caracteristico
        

    def autoval(self, **kwargs):
        pol = self.poly_car()
        roots, multiplicity = pol.findroots()
        return roots
        

"""PROGRAM DONE BY RAFAEL ANDANT"""


    
#%%   
    
if __name__ == '__main__':
    
    """Type all the commands you want to!"""
    
    """Remember that for building an array it must me this way"""
    
    # matrix = myarray([1,2,3,4], 2, 2)
    
    """For printing the matrix, use .myprint()"""
    
    # matrix1.myptint()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    


    

#%%








