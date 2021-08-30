def tarjetas(x,y):
    t= x*12
    p= y*35
    if t<= p:
        return t
    elif p<=t:
        return p
def main():
    #escribe tu código abajo de esta línea
    pliegos= int(input('Dame la cantidad de pliegos albanene:'))
    plumones= int(input('Dame la cantidad de plumones:'))
    total= tarjetas(pliegos,plumones)
    print('El número máximo de tarjetas que se pueden hacer es:',total)
if __name__=='__main__':
    main()
