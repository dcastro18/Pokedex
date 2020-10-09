import pickle
from tkinter import messagebox
matriz = [['001', 'bulbasaur', 'http://pokeapi.co/api/v2/pokemon/1', ['https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png', 69, 7]],['002', 'ivysaur', 'http://pokeapi.co/api/v2/pokemon/1', ['https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png', 69, 7]],['003', 'venasaur', 'http://pokeapi.co/api/v2/pokemon/1', ['https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png', 69, 7]]]
pokemon = ['002', 'ivysaur', 'http://pokeapi.co/api/v2/pokemon/1', ['https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png', 69, 7]]

def archivoInicial():
    """
    Entrada: No recibe ninguna entrada
    Salida: Se encarga de crear el archivo de mis Pokemon con un ejemplo de como será mostrada la información.
    Funcionamiento: Mediante el uso de Pickle, se maneja la información en binario y se agrega el ejemplo.
    """
    archivo=open("misPokemons","wb")
    ejemplo=["ID","Nombre","URL del Pokemon",["Icono","Peso","Altura"]]
    pickle.dump(ejemplo,archivo)
    archivo.close()
def misPokemons(pokemon):
    """
    Entrada: Recibe la información de un pokemon escogido, la cual se revisará en el archivo considerando si será o no agregada al archivo.
    Salida: Se agrega el pokemon a la lista si no se encuentra anteriormente, si este pokemon se encuentra, le informa al usuario que ya fue agregado anteriormente, no agregandolo a la lista.
    Funcionamiento: Lee el archivo y busca al pokemon (su informacion) en el archivo, ahi realiza la comparacion de si se encuentra o no en el archivo.
    """
    archivo = open("misPokemons","rb")
    lista= pickle.load(archivo)
    if pokemon in lista:
        messagebox.showerror("Cuidado","Su pokemon ya fue agregado previamente")
        archivo.close()
    else:
        archivo=open("misPokemons","wb")
        lista.append(pokemon)
        pickle.dump(lista,archivo)
        archivo.close()


archivoInicial()

    
