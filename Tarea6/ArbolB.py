
class NodoB:
	def __init__(self, m):
		# Data sera una llave en una pagina
		# Se incrementa en 1 ya que servirá para los casos en que hay que 
		# guardar el nodo que revasa el limite de claves en una pagina
		# y asi poder realizar la operacion de dividir
		self.data = [None] * (m+1)
		# Hijos de una pagina
		# Igual, tendra 1 hijo de mas para realizar facilmente
		# la operacion de dividir cuando se requiera
		self.children = [None] * (m+2)
		# La cantidad de claves en una pagina
		self.count = 0
		# El orden del arbol
		self.m = m
	
	def insertar(self, value):
		index = 0
		# binary_search
		while index < self.count and  self.data[index] < value : 
			index += 1

		if self.children[index] == None: # Leaf node
			self.insertar_en(value, index)
		else: 
			state = self.children[index].insertar(value)
			if state == -1 :
				self.reestructurar_rama(index)
		# Retorna -1 si la pagina ya alcanzó el limite de claves
		return -1 if self.count > self.m else 1 

	# Inserta una clave de forma ordenada 
	def insertar_en(self, value, index):
		j = self.count
		while j > index:
			# Moviendo las claves a la derecha del array de la pagina
			self.data[j] = self.data[j-1]
			# Moviendo los hijos una posicion a la derecha del array de hijos
			self.children[j+1] = self.children[j]
			j -= 1
		self.data[index] = value
		self.children[index+1] = self.children[index]
		self.count += 1

	# Reestructura el árbol cuando una rama ya hay más claves del limite (m). "index" hace referecia al hijo que se va a reestructruar
	def reestructurar_rama(self, index):
		ptr = self.children[index]
		# Creando los dos nuevos hijos
		child0 = NodoB(ptr.m)
		child1 = NodoB(ptr.m)
		i = 0
		while i  < ptr.m // 2:
			# Asignando las primeras claves de la pagina que rebalzó
			# al nuevo hijo izquierdo
			child0.data[i] = ptr.data[i]
			# Asignando los primeros hijos de la pagina que rebalzó
			# a los hijos de la nueva pagina izquierda
			child0.children[i] = ptr.children[i]
			# Cada vez que se inserte una clave, el numero de claves
			# de la nueva pagina izquierda va a aumentar
			child0.count += 1 
			i += 1
		# Asignando el hijo derecho de la ultima clave a pasar a la nueva 
		# pagina izquierda 
		child0.children[i] = ptr.children[i]
		# Almacenar la posicion del nodo pivote
		mid = i 
		# Aumentando para no tomar en cuenta la posicion del pivote mas adelante
		i += 1 # skip
		j = 0
		# Desde una posicion despues del pivote
		while i  < ptr.count:
			child1.children[j] = ptr.children[i]
			child1.data[j] = ptr.data[i]
			child1.count += 1 
			j += 1
			i += 1
		child1.children[j] = ptr.children[i]
		# Insertar en la raiz el dato pivote, es decir, subir lo a la raiz
		self.insertar_en(ptr.data[mid], index)  
		self.children[index] = child0
		self.children[index+1] = child1 

	# Se invoca cuando la raiz llegó al limite de claves
	def reestructurar_raiz(self, ptr):
		child0 = NodoB(ptr.m)
		child1 = NodoB(ptr.m)
		i = 0
		while i  < ptr.m // 2:
			child0.children[i] = ptr.children[i]
			child0.data[i] = ptr.data[i]
			child0.count += 1 
			i += 1
		child0.children[i] = ptr.children[i]
		# Guardando la posicion del pivote
		mid = i 
		i += 1
		j = 0
		while i  < ptr.count:
			child1.children[j] = ptr.children[i]
			child1.data[j] = ptr.data[i]
			child1.count += 1 
			j += 1
			i += 1
		child1.children[j] = ptr.children[i]
		# Guardando en la posicion 0
		ptr.data[0] = ptr.data[mid]
		# Hijo izquierdo de la primer clave
		ptr.children[0] = child0
		# Hijo derecho de la primer clave
		ptr.children[1] = child1
		# Reiniciando el contador el 
		ptr.count = 1


class ArbolB:
	def __init__(self, m):
		self.m = m
		self.root = NodoB(m)

	def insertar(self, value):
		state = self.root.insertar(value)		
		if state == -1:
			self.root.reestructurar_raiz(self.root)