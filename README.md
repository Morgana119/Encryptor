# Encryptor

### Expliciación de funcionamiento general:

Son 3 formas diferentes de cifrar un texto:

1. Cifrado de César: ​​Es un tipo de cifrado por sustitución en el que una letra en el texto original
es reemplazada por otra letra que se encuentra un número fijo de posiciones más adelante en el alfabeto.
Por ejemplo, con undesplazamiento de 3, la A sería sustituida por la D (situada 3 lugares a la derecha
de la A), la B sería reemplazada por la E.

2. Cifrado rail fence/en zigzag: es una forma de cifrado por transposición. Un cifrado por transposición
implica la reorganización de las letras del texto plano para cifrar el mensaje. En el cifrado de rail fence,
el texto plano se escribe hacia abajo y en diagonal en sucesivas filas y luego se mueve hacia arriba cuando
llegamos a la fila inferior. Al llegar a la fila superior, el mensaje se escribe de nuevo hacia abajo hasta
que se escribe todo el texto plano

3. Crea tu propio lenguaje de cifrado: El usuario introducirá el mensaje que se quiere cifrar y los
valores para cada letra del abecedario, de acuerdo a esa selección se imprimirá el mensaje cifrado de
acuerdo al abecedario hecho previamente. 


### Casos de prueba:

def cifr_Cesar(texto, n):

Input: Número de opción (1. Cifrado de César)
Input: Escribir texto
Input: Número de clave
Output: Texto cifrado

Input: 1
Input: Python
Input: 2
Output: El cifrado de " python " es: ravjqp

Input: 1
Input: Hola?
Input: 18
Output: El cifrado de " Hola? " es: zgds?

Input: 1
Input: ¡Felicidades!
Input: 15
Output: El cifrado de " ¡Felicidades! " es: ¡utaxrxspsth!

Input: 0
Input: Hola mundo
Input: 0
Output: El cifrado de " Hola mundo " es: hola mundo

___________________________________________

def cifr_Rail (texto, f):

Input: Número de opción (2. Cifrado rail fence)
Input: Escribir texto
Input: Número de filas
Output: Texto cifrado

Input: 2
Input: Musica
Input: 2
Output: El cifrado de " Musica " es: Mscuia

Input: 2
Input: lindo dia
Input: 3
Output: El cifrado de " lindo dia " es: loiddani

Input: 2
Input: Debes encontrar el tesoro escondido
Input: 8
Output: El cifrado de " Debes encontrar el tesoro escondido " es: Deierlddbatnoereostscenosnoreco

___________________________________________

def cifr_A (texto, f):

Input: Número de opción (3. Crea tu propio lenguaje de cifrado)
Input: Escribir texto
a: Valor de a
b: Valor de b
c: Valor de c
d: Valor de d
e: Valor de e
f: Valor de f
g: Valor de g
h: Valor de h
i: Valor de i
j: Valor de j
k: Valor de k
l: Valor de l
m: Valor de m
n: Valor de n
o: Valor de o
p: Valor de p
q: Valor de q
r: Valor de r
s: Valor de s
t: Valor de t
u: Valor de u
v: Valor de v
w: Valor de w
x: Valor de x
y: Valor de y
z: Valor de z
Output: Texto cifrado

Input: Número de opción (3. Crea tu propio lenguaje de cifrado)
Input: encriptado
a: 1
b: 2
c: 3
d: 4
e: 5
f: 6
g: 7
h: 8
i: 9
j: '
k: ?
l: ¿
m: ¡
n: !
o: |
p: °
q: *
r: +
s: {
t: }
u: [
v: ]
w: -
x: .
y: ;
z: ,
Output: El cifrado de " encriptado " es: 5!3+9°}14|

___________________________________________

Input: Número de opción (4. Mis cifrados)
Output: Datos guardados en el archivo de texto

Input: 4
Output:

Tus cifrados fueron:

Cifrado de César
Mensaje: hola
Cifrado: jqnc

Cifrado rail fence
Mensaje: hola como estas
Cifrado: hlcmetsoaoosa

___________________________________________

Input: Número de opción (5. Salir)
Output: Mensaje "Adios"

Input: 5
Output: Adios

___________________________________________

Input: Número de opción (Opción inválida)
Output: Mensaje "Opcion_invalida"

Input: 6
Output: Selección inválida, seleccione una de las opciones disponibles
"""
