
class NodoTernario:    
    def __init__( self,value,left=None, center=None, rigth=None ):
        self.data= value 
        self.left= left
        self.center = center
        self.rigth = rigth

arbol = NodoTernario(20, None , NodoTernario(19, NodoTernario(67, center=NodoTernario(99)), None, None), NodoTernario(23, None, NodoTernario(57), None))


print(arbol.center.left.center.data)
print(arbol.rigth.center.data)
