import turtle, time



class Prota():
    
    def __init__(self,nombre):
        self.nombre = nombre


with open(r"dialogos.txt",'r') as dialogo:
    lee = dialogo.read()
    cont=''
    lista = []
    for i in lee:
        if i != '\n':
            cont += i
        else:
            lista.append(cont)
            cont = ''
    print(lista)
            
        
    
    


