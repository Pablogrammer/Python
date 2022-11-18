import turtle, time



#-----------------------PANTALLA----------------------
s = turtle.Screen()
s.title('Misioneando')
s.setup(1150,1000, 400, 0)
s.bgpic(r"./imagenes/background(2).gif")
s.tracer(1)
#-------------shapes-------------

s.register_shape(r"./imagenes/prota/static.gif")
s.register_shape(r"./imagenes/npcs/npc1.gif")
s.register_shape(r"./imagenes/npcs/npc2.gif")
s.register_shape(r"./imagenes/npcs/npc3.gif")

#-----------------Variables Globales------------------

nombre = s.textinput("Juego","Nombre de tu protagonista")

lista = []
with open(r"dialogos.txt",'r') as dialogo:
    lee = dialogo.read()
    cont=''
    for i in lee:
        if i != '\n':
            cont += i
        else:
            lista.append(cont)
            cont = ''
    

#------------------------CLASES-----------------------


class Juego:
    '''La clase juego contiene a todas las demás clases y las inicia para que todo comience
        a la vez'''
    
    def __init__(self):
        self.npc1 = Npc((300,290),1)
        self.npc2 = Npc((-180,-150),2)
        self.npc3 = Npc((-20,40),3)
        self.p = Prota()
        self.par = Partida()
 

class Persona(turtle.Turtle):
    '''La clase persona hereda de turtle.Turtle, ahora todos los objetos creados a partir de
        persona son tortugas. Se abre una ventana nueva de turtle graphics cuando se crea
        la primera tortuga'''
    
    def __init__(self,nombre,imagen):
        super().__init__()
        self.penup()
        self.nombre = nombre
        self.imagen = imagen
        self.shape(imagen)
    

class Npc(Persona):
    '''La clase Npc hereda de Persona, que a la vez hereda de turtle.Turtle.
        Los objetos Npcs serán las personas que te dan misiones para completar el juego'''
    
    def __init__(self,posicion,modelo):
        super().__init__('chef',r"./imagenes/npcs/npc{}.gif".format(modelo))
        self.hideturtle()
        self.goto(posicion)
        self.showturtle()
        self.shape(self.imagen)
        
    def decir_dialogo(self):
        pass
        
class Prota(Persona):
    
    def __init__(self):
        super().__init__(nombre,r"./imagenes/prota/static.gif")
        self.hideturtle()
        self.setposition(-250,200)
        self.showturtle()
        self.m1 = Mision((300,290),(270,-360),False)
        self.m2 = Mision((-180,-150),(-350,320),False)
        self.m3 = Mision((-20,40),(310,200),False)
        self.misiones = [self.m1,self.m2,self.m3]
        
    def mover_abajo(self):
        self.setheading(270)
        self.forward(20)        
        
    def mover_arriba(self):
        self.setheading(90)
        self.forward(20)
        
    def mover_izquierda(self):
        self.setheading(180)
        self.forward(20)
    
    def mover_derecha(self):
        self.setheading(0)
        self.forward(20)
    
    def posicion(self):
        print(self.position())
        
    
    def realizar_accion(self,):
        
        
        for i in self.misiones:
            if self.distance(i.pos_objetivo) < 50 and i.realizado == False:
                i.realizado = True
                j.par.misiones += 1
                j.par.muestra.clear()
                j.par.muestra_estado()
                if j.par.misiones == 3:
                    print('Terminar partida')
                    
            if self.distance(i.pos_salida) < 50 and i.realizado == False:
                j.par.texto.goto(i.pos_salida)
                
                if self.misiones.index(i) == 0:
                    for i in range(3):
                        j.par.texto.write(lista[i], font= ('Elephant', 15, 'normal'))
                        time.sleep(2)
                        j.par.texto.clear()
                        
                if self.misiones.index(i) == 1:
                    for i in range(4,7):
                        j.par.texto.write(lista[i], font= ('Elephant', 15, 'normal'))
                        time.sleep(2)
                        j.par.texto.clear()
                        
                if self.misiones.index(i) == 2:
                    for i in range(7,10):
                        j.par.texto.write(lista[i], font= ('Elephant', 15, 'normal'))
                        time.sleep(2)
                        j.par.texto.clear()
            else:
                pass#print('Ya has realizado esta mision')
            
        else:
            pass#print('Aquí no puedes hacer ninguna acción')
            

class Mision:
    
    def __init__(self,pos_salida,pos_objetivo,realizado):
        self.realizado = realizado
        self.pos_objetivo = pos_objetivo
        self.pos_salida = pos_salida
    

class Partida:
    
    def __init__(self):
        self.misiones = 0
        self.muestra = turtle.Turtle()
        self.texto = turtle.Turtle()
        self.texto.penup()
        self.texto.hideturtle()
        self.muestra_estado()
        
        
    def muestra_estado(self):
        self.muestra.penup()
        self.muestra.hideturtle()
        self.muestra.goto(-550,400)
        self.muestra.write('misiones: {}'.format(self.misiones),font=('Elephant', 40, 'normal'))
        
    
    def guarda_partida(self):
        mis = str(self.misiones)
        pos = str(j.p.position())
        with open('partida_guardada.txt','w') as archivo:
            archivo.write(mis+pos)
    
    def carga_partida(self):
        with open('partida_guardada.txt','r') as archivo:
            mis = archivo.read(1)
            pos = archivo.read(20)
            j.p.goto(pos)


#------------------INICIAL-----------------

j = Juego()

s.onkeypress(j.p.mover_abajo, "s")
s.onkeypress(j.p.mover_arriba, "w")
s.onkeypress(j.p.mover_derecha, "d")
s.onkeypress(j.p.mover_izquierda, "a")
s.onkeypress(j.p.posicion, "e")
s.onkeypress(j.par.guarda_partida, "g")
s.onkeypress(j.p.realizar_accion, "r")


s.listen()
s.mainloop()