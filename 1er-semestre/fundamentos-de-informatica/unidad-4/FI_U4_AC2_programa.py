print('Hello World')
print("Bienvenido a Python")
print("Mi nombre es: Mauro Noel Sánchez Campos")
print("Diferentes formas de mostrar una cadena de texto")
print('Esto es texto. ', "Esto es un String.", ' También es string')
print("Los números los puedo convertir a string")
print("5", "200", "1.5", "0.957")
print("Operaciones básicas:")
print("Suma")
print(5+9, 3.8+9, complex(3,1)+complex(4,5))
print("Resta")
print(5-7, 38.5-70, complex(6,2)-complex(2,6))
print("Multiplicación ")
print(2*9, 2.5*6, complex(5,7)*complex(2,8))
print("División ")
print(8/3, 3.8/9, complex(3,1)/complex(4,5))
print("Potencia ")
print(2**3)
print("Raíz cuadrada ")
print(2**(.5))
texto1 = 'Concatenación con '
texto2 = 'python'
texto3 = texto1 + texto2
print(texto3)
texto4 = 'Repetición '
print(texto4*5)
texto5 = '''renglon1
renglon2
renglon3'''
print(texto5)
texto6 = 'col1\tcol2\tcol3\n1\t2\t3\n'
print(texto6)
print("Entradas del usuario ")
edad = int(input('Teclea tu edad:'))
print('Tu edad es:', edad)
nombre = 'Mauro'
edad = 0  # <-- CAMBIA el 0 por tu edad
print("Formato para impresión ")
print('Mi nombre es {} mi edad es {}'.format(nombre, edad))

#Programa que calcula el área de un triángulo
base = int(input('Introduzca la base del triángulo: '))
altura = int(input('Introduzca la altura del triángulo: '))
area = (1.0 / 2) * base * altura
print (area)
