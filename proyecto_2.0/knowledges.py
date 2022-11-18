#Repaso examen


#------------------------------Clases(herencias,metodos,iteraciones)-------------------------



#------------------  Iter + Correción de errores  -----------------
class Iterable:
    
    def __init__(self):
        self.i = -1
        self.lista = [1,2,3,4,5,6,7,8,9,10]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.i += 1
        try:
            if self.i == len(self.lista):
                raise StopIteration
            else:
                return print(self.lista[self.i])
        except StopIteration:
            print('Ya está bro')
            
            
        except IndexError:
            print('Hermano tetas pasando')
            self.i = -1
        
        finally:
            print('')

            
# it = Iterable()    
# for i in range(100):
#     next(it)


class Persona:
    
    def __init__(self):
        self.nombre = 'Paco'
        

class Vehiculo:
    
    def __init__(self,nombre='Indefinido'):
        self.nombre = nombre
        self.arrancado = False
        self.velocidad = 0
        
    def __str__(self):
        return 'este vehiculo es un {}, y tiene velocidad {}'.format(self.nombre,self.velocidad)
    
    def arrancar(self):
        self.arrancado = True
        
    def acelerar(self):
        if self.arrancado == True:
            self.velocidad += 5
        
        
class Coche(Vehiculo):
    
    def init(self):
        super().__init__()
        self.parabrisas = False
        self.p = Persona()
    
    def parabrisas(self):
        self.parabrisas = True
    
    def acelerar(self):
        if self.arrancado == True:
            self.velocidad += 10
    
v = Vehiculo('Pito')    
c = Coche('coche1')
Coche.__mro__


#---------------------------------Generadores--------------------------------------

generador = (i for i in range (10)) #<------ Generador por comprensión

for i in generador:                 #<------ Hay que recorrer para imprimir
    print(i)

def gen():                          #<------ Generador en función
    lista = ['Paco','Pepe','Peco','Papo','Pito']
    for i in lista:
        yield i

for i in gen():                     #<------ Hay que recorrer para imprimir
    print(i)


#-------------------------------------Ficheros---------------------------------
'''
-------Métodos ficheros-----

with open('NombreFichero','r') as f:
    f.readlines()

readline()
read()
readlines()

open(nombrefichero,modo)
modos(r,w,a)

r --> lee el fichero
w --> sirve para escribir pero machacas el contenido del fichero
a --> es para añadir al final del fichero


'''


with open('prueba.txt') as f:
    f1 = f.readlines()
    f2 = []

    for i in f1:
        f2.append(i.strip('\n'))
    print(f2)

with open('prueba.txt','a') as f:
    f.write('hola')
    
for i in range(10):
    with open('prueba.txt') as f:
        print(f.readlines())
        
    with open('prueba.txt','a') as f:
        f.write('como')
    




