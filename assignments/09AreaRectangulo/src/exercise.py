
def area_rect(x,y):
    area= x*y
    return area

def main():
    #escribe tu código abajo de esta línea

base= float(input('Dame la base:'))
altura= float( input('Dame la altura:'))
resultado= area_rect(base,altura)
print('El área del rectángulo es:', resultado)

if __name__=='__main__':
    main()
