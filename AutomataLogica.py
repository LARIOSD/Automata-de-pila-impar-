from LogicaPila import MiPila

class Automata():
    def __init__(self,palabraLeguaje):
        self.palabraLeguaje = palabraLeguaje
        self.transicion_P = ["b/b/bb/1", "a/b/ba/2", "b/a/ab/3", "a/a/aa/4", "b/#/#b/5", "a/#/#a/6","c/#/#/7", "c/b/b/8", "c/a/a/9"]
        self.transicion_Q = ["b/b/λ/10", "a/a/λ/11","λ/#/#/12"]
        self.transicionActual = []
        self.imageVector = ["Image/imag1.png",]
        self.matriPila = []
        self.cambio = 1
        self.Pila = MiPila()
        #self.miGrafo = Gui
    


    def identificarTransicion(self): 
        for iden in self.transicionActual:
            if iden == "1":
                self.imageVector.append("Image/imag2.png")
            if iden == "2":
                self.imageVector.append("Image/imag3.png")
            if iden == "3":
                self.imageVector.append("Image/imag4.png")
            if iden == "4":
                self.imageVector.append("Image/imag5.png")
            if iden == "5":
               self.imageVector.append("Image/imag6.png")
            if iden == "6":
                self.imageVector.append("Image/imag7.png")
            if iden == "7":
                self.imageVector.append("Image/imag8.png")
            if iden == "8":
                self.imageVector.append("Image/imag9.png")
            if iden == "9":
                self.imageVector.append("Image/imag10.png")
            if iden == "10":
                self.imageVector.append("Image/imag11.png")
            if iden == "11":
                self.imageVector.append("Image/imag12.png")
            if iden == "12":
                self.imageVector.append("Image/imag13.png")
    

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
            id = trans[3]
            if  leer == letraLenguaje and self.Pila.consutarTope() == sacar:
                self.transicionActual.append(id)
                return mete
        return None

    def validarPalindrome(self):
        for letraLenguaje in self.palabraLeguaje:
            self.Pila.mostrarPila()

            #Aqui debaeria obtener el vector de pilas
            self.matriPila.append(self.Pila.obtenerPila())

            if letraLenguaje == "c":
                self.encontrarTransicion(letraLenguaje)
                self.cambio = 2
                pass
            else :
                mete = self.encontrarTransicion(letraLenguaje)
                if mete != None:
                    self.Pila.desaPilar()
                    print(mete)
                    for a in mete:
                        self.Pila.apilar(a)
                else: 
                    print("No es palindrome")
                    break
        self.Pila.mostrarPila()
        if len(self.Pila.obtenerPila()) == 1:
            print("Es palindrome")

        #self.Pila.mostrarPila()
        print(self.transicionActual)
        self.identificarTransicion()
        print(self.imageVector)
        for p in self.matriPila:
            print(p)

        

aut = Automata("abacabaλ")
aut.validarPalindrome()



