from subprocess import check_call

class GrafoArbolB:

    def __init__(self):
        self.contInser = 0

    def graficarArbol(self, arbol):
        acumuladores = ["digraph G{\nnode [shape=record, height=.1];\n", ""]

        if arbol.root != None:
            self.recorrerArbolB(arbol.root, acumuladores)
        
        filename = ""
        

        self.contInser = self.contInser + 1
        filename = "Grafos/Dots/ArbolB.dot"

        acumuladores[0] += acumuladores[1] + "\n}"
        archivo = open(filename, "w")
        archivo.write(acumuladores[0])
        archivo.close()

        check_call(['dot','-Tpng',filename,'-o', "Grafos/Imgs/ArbolB.png"])
        print("\n***********************************************************************************")
        print("Grafo generado con éxito. La imagen generada se encuentra en Grafos/Imgs/ArbolB.png")
        print("***********************************************************************************")

    # Algoritmo funcional para un árbol de un orden máximo 5
    def recorrerArbolB(self, root, acum):
        if root != None:
            llaves = []
            for i in range(root.count):
                llaves.append(str(root.data[i])) 
            if len(llaves) == 1:
                acum[0] +=  '"{}" [label=" <f0> | <f1> {} | <f2> "];\n'.format(str(hash(root)), llaves[0])
            elif len(llaves) == 2:
                acum[0] +=  '"{}" [label=" <f0> | <f1> {} | <f2>  | <f3> {} | <f4> "];\n'.format(str(hash(root)), llaves[0], llaves[1])
            elif len(llaves) == 3:
                acum[0] +=  '"{}" [label=" <f0> | <f1> {} | <f2>  | <f3> {} | <f4> | <f5> {} | <f6> "];\n'.format(str(hash(root)), llaves[0], llaves[1], llaves[2])
            elif len(llaves) == 4:
                acum[0] +=  '"{}" [label=" <f0> | <f1> {} | <f2>  | <f3> {} | <f4> | <f5> {} | <f6> | <f7> {} | <f8> "];\n'.format(str(hash(root)), llaves[0], llaves[1], llaves[2], llaves[3])
            # acum[0] +=  '"{}" [label="{}"];\n'.format(str(hash(root)), llaves)
            i = 0
            while i < root.count:
                j = 0
                if root.children[i] != None:
                    if i == 0:
                        f_i = '"f{}"'.format(str(j))
                        acum[1] += '"{}":{} -> "{}":f1;\n'.format(str(hash(root)), f_i, str(hash(root.children[i])))
                    else:
                        j += 2
                        f_i = '"f{}"'.format(str(j))
                        acum[1] += '"{}":{} -> "{}":f1;\n'.format(str(hash(root)), f_i, str(hash(root.children[i])))
                    self.recorrerArbolB(root.children[i], acum)
                i += 1
            j += 2
            if root.children[i] != None:
                f_i = '"f{}"'.format(str(j))
                acum[1] += '"{}":{} -> "{}";\n'.format(str(hash(root)), f_i, str(hash(root.children[i])))
                self.recorrerArbolB(root.children[i], acum)
