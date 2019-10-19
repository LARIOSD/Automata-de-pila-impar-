class Grafo():
    def __init__(self):
        pass

class Transiciones():
    def __init__(self,lee, extrae, inserta, idTransicion):
        self.lee = lee
        self.extrae= extrae
        self.inserta = inserta
        self.idTransicion = idTransicion
    
    def simboloLeer(self):
        return self.lee
    
    def simboloExtrae(self):
        return self.extrae
    
    def simboloInserta(self):
        return self.inserta

    




# LeeTopePila ExtraerTopePila InsertaPila
