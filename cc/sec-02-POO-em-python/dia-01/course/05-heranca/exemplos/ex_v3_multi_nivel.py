class C: # C 
    def x(self): # método de exemplo
        print(1)

class B(C): # B herda de C
    pass

class A(B): # A herda de B
    pass


a = A()
a.x()
# 1