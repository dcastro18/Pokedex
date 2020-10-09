import requests,json
    
def pokemonEscogido(n):
        pok= int(n)
        URL_API = 'http://pokeapi.co/api/v2/pokemon/'+ str(pok)#URL de la pokeAPI.
        print(n)
        info_del_pokemon = requests.get(URL_API)#Consigue la informacion del URL
        print(info_del_pokemon)
        print(info_del_pokemon)
        jsonToPython = json.loads(info_del_pokemon.content)#Convierte la info de formato json a Python.
        ID = jsonToPython["id"]#Saca el ID.
        if len(str(ID))==1:#Convierte ID en 3 digitos.
            ID='00'+str(ID)
        elif len(str(ID))==2:
            ID='0'+str(ID)
        global nombre,peso,altura,icono
        nombre = jsonToPython["name"]#Saca el ID.
        URL = URL_API #Usa el URL formado
        icono = jsonToPython["sprites"]["front_default"]#Saca el icono.
        peso = jsonToPython["weight"]#Saca el peso.
        altura = jsonToPython["height"]#Saca la altura.
        pokemon = [ID,nombre,URL]#primeros 3 elementos de la matriz.
        icono_peso_altura = [icono,str(peso),str(altura)]#Ultimo elemento de la matriz(sublista).
        pokemon.append(icono_peso_altura)
        return pokemon



        
######################################################            






