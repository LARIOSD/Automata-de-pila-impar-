from LogicaPila import Pila


#transicion_P_Q = ["c/#/#", "c/b/b", "c/a/a"]
#transicion_Q_Q = ["b/b/λ", "a/a/λ"]
#transicion_Q_R = ["λ/#/#"]

class Logica():
    def __init__(self):
        self.palabraLeguaje = "aabbc"
        self.transicion_P = ["b/b/bb/1", "a/b/ba/2", "b/a/ab/3", "a/a/aa/4", "b/#/#b/5", "a/#/#a/6","c/#/#/7", "c/b/b/8", "c/a/a/9"]
        self.transicion_Q = ["b/b/λ/1", "a/a/λ/2","λ/#/#/3"]
        self.transicionActual = " "
        self.cambio = 0

    def encontrarTransicion(self,letraLenguaje):
          for transicion in self.transicion_P:
                trans = transicion.split("/")
                leer = trans[0]
                sacar = trans[1]
                mete = trans[2]   
                if  leer == letraLenguaje and Pila.consutarTope() == sacar:
                    self.transicionActual = trans
                    return mete

    def locura(self):
        for letraLenguaje in self.palabraLeguaje:
            if letraLenguaje == "c":
                self.cambio = 1
                pass
            mete = self.encontrarTransicion(letraLenguaje)
            Pila.desaPilar()
            for a in mete:
                Pila.apilar(a)
        Pila.mostrarPila()

l = Logica()
l.locura()

#transicionesT = [transicion_P_P,transicion_P_Q,transicion_Q_R,transicion_Q_R]

