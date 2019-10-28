import sys
import time
from tkinter import *
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

class Cinta():
    imagen = {}
    cinta = {}
    texto = {}
    creacionTri = {}
    bandera = bool
   
    def actualizarVentana(self,uno,dos,tres): 
        self.uno = uno
        self.dos = dos
        self.tres = tres
        for i in self.uno: 
            self.uno[i].destroy()
        self.uno.clear()
        for i in self.dos: 
            self.dos[i].destroy() 
        for i in self.tres: 
            self.tres[i].destroy() 


    def validar(self,palabra,bandera):
        self.bandera = bandera 
        varInfo.set(" ")
        self.palabra = palabra
        if len(self.palabra) % 2 == 0:
            varInfo.set("La palabra no es Impar") 
            respuesta = "La Palabra no es Impar"
            speaker.Speak(respuesta)
        else:
            self.actualizarVentana(self.cinta,self.texto,self.creacionTri)
            limpia = Pila()
            limpia.LimpiarPila()
            self.enListar(self.palabra)
        

    def enListar(self,palabra):
        self.palabra = palabra 
        listaPalabra=[]
        for i in range(0,len(self.palabra)):
            listaPalabra.append(self.palabra[i])
        self.imprimir(listaPalabra)

    
    def imprimir(self,lista):
        ancho = 670
        anchotexto = 688  
        i = 0
        j = 0 
        tamaoTexto = len(lista) -1 

        while i<len(lista):
            self.imagen[i] = PhotoImage(file="cintaP.png")
            self.cinta[i] = Label(ventana,image=self.imagen[i],bd=0)
            self.cinta[i].place(x=ancho,y=300)
            ancho = ancho - 47 
            i = i +1
    
        while j <len(lista):
            self.texto[j] = Label(ventana,text=lista[tamaoTexto],bg="#f6f6f6")
            self.texto[j].place(x=anchotexto,y=315)
            self.texto[j].config(font=("Courier",14))
            tamaoTexto -= 1
            anchotexto = anchotexto -47 
        
            j +=1
        mitad = int(len(self.cinta)/2)
    
        self.recorrerCinta(mitad,anchotexto,lista)
 
    def recorrerCinta(self,mitad,ancho,lista):
        self.listaPila = lista
        i = 0
        ancho = ancho -14
        altura = 500
        self.creacionTri[1] = Canvas(ventana, width=420, height=30,bg="white",bd=0)
        triangulo = self.creacionTri[1].create_polygon(20,10,30,30,10,30,fill='blue')
        self.creacionTri[1].place(x=ancho, y=350)

        while i <= mitad:
            ancho = ancho + 47
            self.creacionTri[1].move(triangulo,47,0)

            movimiento_grafo = Grafo()
            movimiento_grafo.estado1Grafo(i,mitad,self.bandera)

            if (i != mitad):
                rellenarPila = Pila() 
                rellenarPila.imprimir(i,altura,self.listaPila,self.bandera)

            ventana.update() 
            if self.bandera:    
                time.sleep(1)
            else:
                time.sleep(0.2)
            altura = altura -45
            i+=1
        rellenarPila.desapilar(altura,ancho) 

class Pila(Cinta):
    infoPila = {}
    imagenPila = {}  
    pila = {}
    posicionPila = {}
    bandera = bool 
    
    def imprimir(self,i,altura,listaPila,bandera):
        self.listaPila = listaPila
        self.bandera = bandera
        self.altura = altura 
        self.i = i
        self.imagenPila[i] = PhotoImage(file="pila.png")
        self.pila[i] = Label(ventana,image=self.imagenPila[i],bd=0)
        self.pila[i].place(x=900,y=self.altura)

        self.infoPila[i] = Label(ventana,text=self.listaPila[i],bg="white")
        self.infoPila[i].place(x=920,y=(self.altura+10))
        self.infoPila[i].config(font=("Courier",14))
    
    def LimpiarPila(self):
        Pila.actualizarVentana(self,self.pila,self.infoPila,self.posicionPila)
    
    def eliminarNodo(self,mitad): 
        self.infoPila[mitad].destroy()
        self.pila[mitad].destroy()
    
    def desapilar(self,altura,ancho):
        self.altura = altura
        mitad = int(len(self.listaPila)/2)-1
        total = len(self.listaPila)-1
        conteo = -1
        i = 0
        self.posicionPila[1] = Canvas(ventana, width=30, height=370,bg="white",bd=0)
        triangulo = self.posicionPila[1].create_polygon(30,20,10,30,10,10,fill='red')
        self.posicionPila[1].place(x=865, y=altura+85)
        self.posicionPila[2] = Canvas(ventana, width=370, height=30,bg="white",bd=0)
        triangulo2 = self.posicionPila[2].create_polygon(20,10,30,30,10,30,fill='green')
        self.posicionPila[2].place(x=ancho, y=350)
        self.posicionPila[2].move(triangulo2,47,0)
        if self.bandera:    
            time.sleep(1)
        else:
            time.sleep(0.2)         
        while i <= mitad:
            aceptada = False
            if self.listaPila[i] == self.listaPila[total-i]:
                conteo += 1 
                aceptada = True
                estado_grafo = Grafo()
                estado_grafo.estado2Grafo(i,aceptada,self.bandera)
                self.eliminarNodo(mitad-i)
                self.posicionPila[1].move(triangulo,0,47)
                self.posicionPila[2].move(triangulo2,47,0)
                ventana.update()
                if self.bandera:    
                    time.sleep(1)
                else:
                    time.sleep(0.2)
            i = i+1
         
        if conteo == mitad: 
            estado_grafo.estado_finish(i)
            self.imagenPila[i] = PhotoImage(file="siP.png")
            self.pila[i] = Label(ventana,image=self.imagenPila[i],bd=0)
            self.pila[i].place(x=0,y=230)
            respuesta = "La Palabra es Palíndroma"
            speaker.Speak(respuesta) 
        else:
            self.imagenPila[i] = PhotoImage(file="noP.png")
            self.pila[i] = Label(ventana,image=self.imagenPila[i],bd=0)
            self.pila[i].place(x=0,y=230)
            respuesta = "La Palabra no es Palíndroma"
            speaker.Speak(respuesta)   

    
      
class Grafo(): 
    fotoEstado = {}
    estado = {} 
  
    def estado1Grafo(self,i,mitad,bandera):
        self.mitad = mitad
        self.bandera = bandera
        self.i = i
        if self.i == 0:
            self.fotoEstado[self.i] = PhotoImage(file="flecha1.png")
            self.estado[self.i] = Label(ventana,image=self.fotoEstado[self.i],bd=0)
            self.estado[self.i].place(x=150, y=450)
            ventana.update()
            if self.bandera:    
                time.sleep(1)
            else:
                time.sleep(0.2)

            self.fotoEstado[self.i] = PhotoImage(file="estado1B.png")
            self.estado[self.i] = Label(ventana,image=self.fotoEstado[self.i],bd=0)
            self.estado[self.i].place(x=150, y=450)
            ventana.update()
            if self.bandera:    
                time.sleep(1)
            else:
                time.sleep(0.2) 
        elif self.i == self.mitad:
            
            self.fotoEstado[self.i] = PhotoImage(file="flecha2.png")
            self.estado[self.i] = Label(ventana,image=self.fotoEstado[self.i],bd=0)
            self.estado[self.i].place(x=150, y=450)
            ventana.update()
            if self.bandera:    
                time.sleep(1)
            else:
                time.sleep(0.2)

            self.fotoEstado[self.i] = PhotoImage(file="estado2B.png")
            self.estado[self.i] = Label(ventana,image=self.fotoEstado[self.i],bd=0)
            self.estado[self.i].place(x=150, y=450)
            ventana.update()
            if self.bandera:    
                time.sleep(1)
            else:
                time.sleep(0.2)
        else:
            
            self.fotoEstado[self.i] = PhotoImage(file="estado1A.png")
            self.estado[self.i] = Label(ventana,image=self.fotoEstado[self.i],bd=0)
            self.estado[self.i].place(x=150, y=450)
            ventana.update()
            if self.bandera:    
                time.sleep(1)
            else:
                time.sleep(0.2) 

            self.fotoEstado[self.i] = PhotoImage(file="estado1B.png")
            self.estado[self.i] = Label(ventana,image=self.fotoEstado[self.i],bd=0)
            self.estado[self.i].place(x=150, y=450)
            ventana.update()
            if self.bandera:    
                time.sleep(1)
            else:
                time.sleep(0.2)             

    def estado2Grafo(self,i,aceptada,bandera):
        self.i = i
        self.aceptada = aceptada
        self.bandera = bandera

        self.fotoEstado[self.i] = PhotoImage(file="estado2A.png")
        self.estado[self.i] = Label(ventana,image=self.fotoEstado[self.i],bd=0)
        self.estado[self.i].place(x=150, y=450)
        ventana.update()
        if self.bandera:    
            time.sleep(1)
        else:
            time.sleep(0.2) 

        if self.aceptada:
            self.fotoEstado[self.i] = PhotoImage(file="estado2B.png")
            self.estado[self.i] = Label(ventana,image=self.fotoEstado[self.i],bd=0)
            self.estado[self.i].place(x=150, y=450)
            ventana.update()
            if self.bandera:    
                time.sleep(1)
            else:
                time.sleep(0.2)

    def estado_finish(self,i):
            self.fotoEstado[self.i] = PhotoImage(file="flecha3.png")
            self.estado[self.i] = Label(ventana,image=self.fotoEstado[self.i],bd=0)
            self.estado[self.i].place(x=150, y=450)
            ventana.update()
            if self.bandera:    
                time.sleep(1)
            else:
                time.sleep(0.2) 

            self.fotoEstado[self.i] = PhotoImage(file="final.png")
            self.estado[self.i] = Label(ventana,image=self.fotoEstado[self.i],bd=0)
            self.estado[self.i].place(x=150, y=450)
            ventana.update()
            if self.bandera:    
                time.sleep(1)
            else:
                time.sleep(0.2)


Palabra = Cinta() 
ventana = Tk()   
ventana.title("Automata de Pila") 
ventana.geometry("1000x600")

 
varInfo = StringVar() 

imagenF = PhotoImage(file="fondo3.png") 
fondo = Label(ventana,image=imagenF,bd=0) 
fondo.place(x=0,y=0)

titulo = Label(ventana,text="Palabra Palidromo:",bg="white")
titulo.place(x=100,y=130)
titulo.config(font=("Courier",15 )) 

entradaPalabra = Entry(ventana)     
entradaPalabra.place(x=320,y=133,width=250,height=23)
entradaPalabra.config(font=("Courier",17),relief=RIDGE,highlightcolor="blue")
entradaPalabra.focus()

botonValidar = Button(ventana,text="Validar lento", command= lambda:Palabra.validar(str(entradaPalabra.get()),True))
botonValidar.place(x=230,y=170)
botonValidar.config(font=("Courier",13 ))

botonValidar2 = Button(ventana,text="Validar rapido", command= lambda:Palabra.validar(str(entradaPalabra.get()),False))
botonValidar2.place(x=400,y=170)
botonValidar2.config(font=("Courier",13 )) 

respuesta = Label(ventana,text="",textvariable = varInfo,bg="white")
respuesta.place(x=200, y=220)
respuesta.config(font=("Courier",13 ))

imagenGrafo = PhotoImage(file="grafodia2.png")
grafo = Label(ventana,image=imagenGrafo,bd=0)
grafo.place(x=150, y=450)
   
ventana.mainloop()  
