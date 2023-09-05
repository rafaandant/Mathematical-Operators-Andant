"""PROGRAM DONE BY RAFAEL ANDANT"""


import matplotlib.pyplot as plt
import numpy as np

class poly:
    def __init__(self, n=0, coefs=[0]):
        self.n = n
        self.coefs = coefs

    def __repr__(self):
        if len(self.coefs) < self.n+1:
            self.coefs += [0] * (self.n+1 - len(self.coefs))
        elif len(self.coefs) > self.n+1:
            self.coefs = self.coefs[:self.n+1]
        terms = []
        for i in range(self.n+1):
            if self.coefs[i] != 0:
                terms.append(str(self.coefs[i]) + 'x^' + str(i))
            
        if len(terms) == 0:
            return '0'
        else:
            return " + ".join(terms)
    
    def poly_plt(self, a, b, **kwargs):
        x = np.linspace(a, b, 10)
        y = np.zeros_like(x)
        for i in range(self.n+1):
            y += self.coefs[i] * x**i
        plt.plot(x, y, **kwargs)
        plt.grid(True)
        plt.show()
    
    def __call__(self, x):
        result = 0
        for i in range(self.n+1):
            result += self.coefs[i] * x**i
        return result
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            salida = __class__(self.n, [self.coefs[i] + other for i in range(self.n+1)])
        elif isinstance(other, poly):
            max_degree = max(self.n, other.n)
            self_coefs = self.coefs + [0] * (max_degree - self.n)
            other_coefs = other.coefs + [0] * (max_degree - other.n)
            salida = __class__(max_degree, [self_coefs[i] + other_coefs[i] for i in range(max_degree+1)])
        else:
            print ("Not a polynomial")
        return salida
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            salida = __class__(self.n, [self.coefs[i] - other for i in range(self.n+1)])
        elif isinstance(other, poly):
            max_degree = max(self.n, other.n)
            self_coefs = self.coefs + [0] * (max_degree - self.n)
            other_coefs = other.coefs + [0] * (max_degree - other.n)
            salida = __class__(max_degree, [self_coefs[i] - other_coefs[i] for i in range(max_degree+1)])
        else:
            print ("Not a polynomial")
        return salida
    
    def __rsub__(self, other):
        return self.__add__(other)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            salida = __class__(self.n, [coef * other for coef in self.coefs])
        elif isinstance(other, poly):
            n = self.n + other.n
            coefs = [0] * (n+1)
            for i in range(self.n+1):
                for j in range(other.n+1):
                    coefs[i+j] += self.coefs[i] * other.coefs[j]
            salida = __class__(n, coefs)
        else:
            print ("Not a polynomial")    
        return salida

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            salida = __class__(self.n, [coef * other for coef in self.coefs])
        else:
            print ("Not a polynomial")
            salida = None 
        return salida
    
    def __pow__(self, n):
        if n==1:
            salida = self
        else:
            salida = self*self**(n-1)
        return salida
            
    def copy(self):
        return poly(self.n, self.coefs.copy())
    
    def __divmod__(self, other):
        if isinstance(other, (int, float)):
            salidadiv = self.__class__(self.n, [coef // other for coef in self.coefs])
            salidamod = self.__class__(0, [coef % other for coef in self.coefs])
        elif self.n < other.n:
            salidadiv = self.__class__()
            salidamod = self.__class__()
        else:
            result_n = self.n - other.n
            result_coefs = [0] * (result_n + 1)
            divisor = other.coefs[-1]
            dividend = self.coefs.copy()
            for i in range(result_n, -1, -1):
                rdiv = dividend[i + other.n] / divisor
                result_coefs[i] = rdiv
                for j in range(other.n):
                    dividend[i + j] -= rdiv * other.coefs[j]
                    
            salidadiv = self.__class__(result_n, result_coefs)
            salidamod = self.__class__(other.n-1, dividend[:other.n])
        return salidadiv, salidamod
    
    def __floordiv__ (self, other):
        return self.__divmod__(other) [0]
    
    def __mod__ (self, other):
        return self.__divmod__(other) [1]
    
    def __rmod__ (self, other):
        if isinstance(other, (int, float)):
            result = __class__(0, [coef % other for coef in self.coefs])
            salida = result.__mod__(self)
        return salida

    def rootfind(self, x0=0, tol=1e-12, max_iter=100000):
        f = self
        df = self.__class__(self.n-1, [i*self.coefs[i] for i in range(1, self.n+1)])
        x = x0
        salida = None
        i = 1
        while i < max_iter and salida is None:
            i += 1
            fx = f(x)
            if abs(fx) < tol:
                salida = round(x, 3)
            else:
                dfx = df(x)
                if dfx == 0:
                    break
                x = x - fx/dfx
        return salida 

    def findroots(self, tol=1e-12):
        p = self
        roots = [p.rootfind(tol=tol)]
        roots1=[]

        while not roots[-1] is None:
            r = p.rootfind()
            if r is None:
                break
            else:
                p = p // poly(1, [-r, 1])
            k = 1
            while abs(p(r)) <= tol:
                k += 1
                p = p // poly(1, [-r, 1])
            roots1.append((r, k))
        
        if len(roots) == 0:
            salida = [p]
        else:
            salida = roots1, p
        return salida
        
    def factorize_polynomial(self):
        roots = self.findroots()[0]
        residual = str(self.findroots()[1])
        multiplicities = self.findroots()[0]
        factorized_list = []
        for i in range(len(roots)):
            root = round(roots[i][0],3)
            multiplicity = multiplicities[i][1]
            factorized_list.append("(X - {})**{}".format(root, multiplicity)) 
        factorized_list.append(residual)
        
        return " * ".join(factorized_list)
    

    
    def derivada (self):
        df = self.__class__(self.n-1, [i*self.coefs[i] for i in range(1, self.n+1)])
        return df
    
    def maxmin (self):
        deriv = self.derivada()
        roots = deriv.findroots()[0]
        X = []
        Y = [] 
        for i in range(len(roots)):
            root = roots [i][0]
            evaluation = self(root)
            X.append(round(root, 3))
            Y.append(round(evaluation, 3))
        for j in Y:
            for k in range(len(Y)):
                max1 = max(Y)
                min1 = min(Y)
                maximos = (X[k], max1)
                minimos = (X[k], min1)
        return maximos, minimos
    

"""PROGRAM DONE BY RAFAEL ANDANT"""  
        
        
    
#%%

if __name__=="__main__":
    
    """For building a Polynomial, please use the following technique:"""
    
    polynomial = poly(3, [5,6,7])
    
    print (polynomial)
    
    """Please check in the console the polynomial expressed is the one you wanted"""
    
    
    
    
    
    