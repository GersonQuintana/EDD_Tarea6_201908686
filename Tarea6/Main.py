from ArbolB import ArbolB
from Grafo import GrafoArbolB

if __name__ == '__main__':
    # Orden del grafo
    orden = 5 
    arbolb = ArbolB(orden-1)
    # Se le resta 1 ya que el numero que resulta de la 
    # operacion orden - 1 será la cantidad de claves permitidas
    grafo = GrafoArbolB()
    # btree.insertar(2)
    arbolb.insertar(1)
    arbolb.insertar(2)
    arbolb.insertar(4)
    arbolb.insertar(5)
    arbolb.insertar(6)
    grafo.graficarArbol(arbolb)
