from tkinter import*
from tkinter import messagebox
from AutomataLogica import Automata
import pyttsx3,re,time

class Gui:
    def __init__(self):

        self.ventana = Tk()
        self.ventana.geometry("950x600")
        self.ventana.config(bg="bisque") #gray92 
        self.ventana.resizable(0,0)

        self.textPantalla = Label(self.ventana, text = "Ingrese el texto :", font = ("Angency FB",14))
        self.textPantalla.place(x=10,y=46)

        self.texto = StringVar()
        self.textCuadro = Entry(width=39, font = ("Angency FB",20),textvariable=self.texto).place(x=10,y=100)

        self.imagen = PhotoImage(file="Image/imag0.png")
        self.fondo = Label(self.ventana, image=self.imagen).place(x=10, y=250)

        self.boton = Button(self.ventana, text="GO",width=10, height=1,anchor="center", command =self.validar , borderwidth=4)
        self.boton.config(cursor="hand2")
        self.boton ['bg'] = 'darkblue'
        self.boton ['fg'] = 'white'
        self.boton ['highlightbackground'] = 'black'
        self.boton ["relief"] = "groove"
        self.boton.place(x=750,y=100)

        self.ventana.mainloop()

        #vector = ["Image/imag1.png","Image/imag2.png","Image/imag3.png","Image/imag4.png","Image/imag5.png","Image/imag6.png","Image/imag7.png","Image/imag8.png","Image/imag9.png",
         #           "Image/imag10.png","Image/imag11.png","Image/imag12.png","Image/imag13.png","Image/imag14.png"]
    def inciarPrograma(self):
        self.animar()
        self.grafo = Automata(self,self.texto.get())
        self.grafo.validarPalindrome()


    def voz(self,palabra):
        engine = pyttsx3.init()   
        voices = engine.getProperty('voices')
        engine.setProperty('voice','spanish-latin-am')
        engine.setProperty('rate', 150)   
        engine.setProperty('volume', 0.9)
        engine.say(palabra)
        engine.runAndWait()

    def validar(self):
        palabra = self.texto.get()
        validacion = re.match("^[a-b]*c[a-b]*$",palabra)
        if validacion is None:
            self.voz("Error")
            messagebox.showerror("Validación","Dato invalido")
            return False
        else: 
            return True

    def pintarGrafo(self,nombreImagen):
        grafo = PhotoImage(file = nombreImagen)
        pantalla = Label(self.ventana, image = grafo).place(x=10, y=250)
        self.ventana.update()
        time.sleep(1) 
           
g = Gui()