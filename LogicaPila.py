
class Pila:
    def __init__(self):
        self.Pila = ["#",]

    def preguntaPilaVacia(self):
        if len(self.Pila) > 1 :
            return False
        else: return True

    def apilar(self,datoApilar):
        self.Pila.append(datoApilar)
    
    def desaPilar(self):
        if self.preguntaPilaVacia() :
            return None
        else: return self.Pila.pop()
    
    def consutarTope(self):
        return self.Pila[len(self.Pila)-1]

    def mostrarPila(self):
        print(self.Pila)
    
a = Pila()
a.mostrarPila()
print(a.consutarTope())



    




