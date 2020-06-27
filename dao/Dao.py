class Dao:
    def __init__(self):
        self._lista = []

    def adicionar(self, obj):
        item = self.buscar(obj.modelo.id)
        if item == None:
            self._lista.append(obj)

    def atualizar(self, obj):
        item = self.buscar(obj.modelo.id)
        if item != None:
            index = self._lista.index(item)
            self._lista.pop(index)
            self._lista.insert(index, item)

    def buscar(self, indetificador):
        for i in range(len(self._lista)):
            #print('id abaixo')
            #print(self._lista[i].modelo)
            if (indetificador == self._lista[i].modelo.id):
                return self._lista[i]
            else:
                return None

    def get_lista(self):
        return self._lista
