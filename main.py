import os #Librería utilizada para limpiar pantalla.
from random import randint  #Librería utilizada para obtener un número aleatorio.
from unidecode import unidecode #Librería para eliminar acentos.


def random_word():   #Función que toma una palabra aleatoria del archivo "data.txt".
    words = []
    with open("data.txt", "r", encoding="utf-8") as data:
        for line in data:
            words.append(line)
    l = len(words)
    word = words[randint(0,l-1)]
    return word


word = random_word() #Elegimos una palabra usando la función random_word y la guardamos como variable global.
n = len(word)
uds = "_ " * (n-1)


def interface(uds):  #Función que muestra la interfaz.
    
    print("========================= JUEGO DEL AHOGADO ===========================")
    print("ADIVINA LA PALABRA")
    print("\n")
    print("".join(uds))  #El argumento de la función se convierte en un string, ya que en general el argumetno será una lista.
    print("\n")


def under_score(): #Función que actualiza la interfaz cada vez que escribimos la palabra correcta

    under = list(uds)
    list_word= list(unidecode(word)) #Se eliminan los acentos de la pabra.
    count = 1
    
    while n>(count):
        letter = input("INGRESA UNA LETRA: ")

        for i in list_word:
            
            if letter == i:
                ind = list_word.index(letter)   #Optenemos el indice en el que se encuentra la letra dada.
                list_word.pop(ind)              #Eliminamos la letra de la palabra. 
                list_word.insert(ind,"*")       #Agregamos el símbolo "*" en el lugar de la letra eliminada. (Esto es necesario cuando hay letras repetidas en una palabra)
                under.pop(ind*2)
                under.insert(ind*2,i.upper())
                count = count +1               
            
            else: continue

        os.system("clear")
        interface(under)


def win():
    print("¡¡¡FELICIDADES, HAS GANADO!!!")


def main(): #Función principal.
    
    os.system("clear")
    interface(uds)

    under_score()
    win()



if __name__ == "__main__": #Entry point.
    main()