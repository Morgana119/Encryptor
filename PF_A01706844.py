def cifr_Cesar(texto, num): #Función que ejecuta el cifrado de César 
    textoL = texto.lower()
    
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    traduccion1 = ""
    
    for c in range(len(textoL)): 
        if textoL[c] == ' ' or textoL[c] == '?' or textoL[c] == '¿' or textoL[c] == '!' or textoL[c] == '¡' or textoL[c] == ';' or textoL[c] == '.' or textoL[c] == ',':
            traduccion1 = traduccion1 + textoL[c]
            
        elif textoL[c] != ' ':     
            i = abc.index(textoL[c]) #Variable i de índice, guarda el índice de la posición de la letra del texto en el abecedario
            i = (i + num) % 27 #Número de letras + 1, porque no se empieza a contar en la letra de origen, sino que en la siguiente
            traduccion1 = traduccion1 + abc[i]
    
    guarda_cifrado("Cifrado de César","Mensaje: " + texto,"Cifrado: " + traduccion1)
    return traduccion1
        
        
def cifr_Rail(texto, fila): #Función que ejecuta el cifrado Rail fence 
    dir = 1 #Dirección 
    lista = []
    for i in range(fila): 
        lista.append([])

    n = 0 #Posición
    final = []
    texto = texto.replace(' ', '') 

    for i in texto: #Agrega cada caracter del texto a la matriz de acuerdo a la posicion n
        lista[n].append(i)
        n = n + dir
        if n == 0 or n == fila - 1: #Cambio de dirección cuando llega al extremo superior o inferior
            dir = dir * -1
    
    for i in range(len(lista)): 
        final = final + lista[i]
    
    final = ''.join(map(str, final)) 
    
    guarda_cifrado("Cifrado rail fence","Mensaje: " + texto,"Cifrado: " + final)
    return final    
    

def cifr_A(texto): #Función para crear tu propio lenguaje de cifrado    
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    abc_nuevo = []
    
    for i in range(len(abc)): 
        letra = abc[i]
        abc_nuevo.append(input(letra + ": "))

    textoL = texto.lower()

    traduccion3 = ""

    for c in textoL: 
        indice = abc.index(c) #Encontrar el indice de c en abc 
        letra_trad = abc_nuevo[indice] #Usar el indice encontrado en abc y usarlo en abc_nuevo para encontrar el valor para el cifrado
        traduccion3 = traduccion3 + letra_trad
    
    guarda_cifrado("Crea tu propio lenguaje de cifrado","Mensaje: " + texto,"Cifrado: " + traduccion3)
    return traduccion3

def guarda_cifrado(tipo,mensaje,traduccion): #Función que guarda los datos en el archivo
    file = open("Mis cifrados.txt", "r+")
    
    contenido = file.read()
        
    file.write(tipo)
    file.write('\n')
    
    file.write(mensaje)
    file.write('\n')
    
    file.write(traduccion)
    file.write('\n')
    file.write('\n')

    file.close()

def menu(): #Menú de opciones
    print()
    print("1. Cifrado de César")
    print("2. Cifrado rail fence")
    print("3. Crea tu propio lenguaje de cifrado")
    print("4. Mis cifrados")
    print("5. Salir")
    
def main():
    file = open("Mis cifrados.txt", "w+")
    file.close()
    
    nombre = str(input("Dame tu nombre: "))
    print("\n"+"Hola",nombre,"!","\n")
    print("Bienvenido a tu cifrador favorito")
    
    condicion = True
    while condicion == True:
        menu()
        opcion = int(input("Selecciona un opción: "))

        if opcion == 1: #Cifrado de César
            texto = str(input("Escribe tu texto: "))
            num = int(input("Ingresa el número de clave: ")) #Número de desplazamiento
            if num >= 0 and num <= 23:
                traduccion = cifr_Cesar(texto, num)
  
            else:
                print("Número inválido, debe ser un número entre 1 - 26")
            
            print("""El cifrado de " """ + texto + """ " es: """ + traduccion)
  
        elif opcion == 2: #Cifrado rail fence
            texto = str(input("Escribe tu texto: "))
            fila = int(input("Ingresa el número de filas: "))
            traduccion = cifr_Rail(texto, fila)
            print("""El cifrado de " """ + texto + """ " es: """ + traduccion)
                 
        elif opcion == 3: #Crear tu propio lenguaje de cifrado
            texto = str(input("Escribe tu texto: "))
            traduccion = cifr_A(texto)
            print("""El cifrado de " """ + texto + """ " es: """ + traduccion)
            
        elif opcion == 4: #Mis cifrados
            file = open("Mis cifrados.txt", "r")
            cifrados = file.read()
            
            print()
            print("Tus cifrados fueron:")
            print()

            print(cifrados)
            file.close()
        
        elif opcion == 5: #Salir
            print("Adios")
            condicion = False
            
        else:
            print("Selección inválida, seleccione una de las opciones disponibles")

main()
