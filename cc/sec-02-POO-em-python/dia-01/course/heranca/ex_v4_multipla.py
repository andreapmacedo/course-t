class C: # C não herda de ninguém
    pass

class B: # B não herda de ninguém
    pass

class A(B, C): # A herda de B e de C
    pass

class A2(C, B): # A2 herda de C e de B. A ordem aqui faz diferença para o MRO.
    pass