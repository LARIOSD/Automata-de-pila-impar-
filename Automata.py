from LogicaPila import Pila

class Automata():
    def __init__(self):
        self.palabraLeguaje = "aabcbaa"
        self.transicion_P = ["b/b/bb/1", "a/b/ba/2", "b/a/ab/3", "a/a/aa/4", "b/#/#b/5", "a/#/#a/6","c/#/#/7", "c/b/b/8", "c/a/a/9"]
        self.transicion_Q = ["b/b/λ/1", "a/a/λ/2","λ/#/#/3"]
        self.transicionActual = " "
        self.cambio = 1

    def encontrarTransicion(self,letraLenguaje):
        transicionesActuales = []     
        if self.cambio == 1:
            transicionesActuales = self.transicion_P
        elif self.cambio == 2:
            transicionesActuales = self.transicion_Q
            
        for transicion in transicionesActuales:
            trans = transicion.split("/")
            leer = trans[0]
            sacar = trans[1]
            mete = trans[2]   
            if  leer == letraLenguaje and Pila.consutarTope() == sacar:
                self.transicionActual = trans
                return mete
        return None

    def validarPalindrome(self):
        for letraLenguaje in self.palabraLeguaje:
            Pila.mostrarPila()
            if letraLenguaje == "c":
                self.cambio = 2
                pass
            else :
                mete = self.encontrarTransicion(letraLenguaje)
                if mete != None:
                    Pila.desaPilar()
                    print(mete)
                    for a in mete:
                        Pila.apilar(a)
                else: 
                    print("No es palindrome")
                    break
        Pila.mostrarPila()
        if len(Pila.obtenerPila()) == 1:
            print("Es palindrome")

        Pila.mostrarPila()
        

p.Automata()
p.validarPalindrome()



