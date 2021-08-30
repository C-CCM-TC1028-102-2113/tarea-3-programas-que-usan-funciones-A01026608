def area_rect(x,y):
    area= x*y
    return area

def volumen_rect(a,b,c):
    volumen= (area_rect(a,b)*c)
    return volumen

def main():
    #escribe tu código abajo de esta línea
base= float(input('Dame la base:'))
altura= float(input('Dame la altura:'))
profundidad= float(input('Dame la profundidad:'))
total= volumen_rect(base,altura,profundidad)
print('El volumen del prisma es:',total)

if __name__=='__main__':
    main()
