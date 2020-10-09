try:
    from PIL import Image, ImageTk
    import requests,json
    
except:
    import os
    os.system("pip install requests")
    os.system("python -m pip install --upgrade pip")
    os.system("python -m pip install simplejson")
    os.system("python -m pip install pillow")


from tkinter import *
from tkinter import messagebox
from sacarMatrizRapido import *
from XML_CORREO import *
from MisPokemonFinal import *
from io import BytesIO
from PIL import Image, ImageTk
import requests,json



################################ Ventana Principal e imagen de Fondo #######################################################################################


ventana=Tk()

ventana.title("Pokedex")

ventana.iconbitmap("icono.ico")

ventana.geometry("831x447")

ventana.resizable(0,0)

ventana.configure(background="white")

background_image=PhotoImage(file="pantilla.png")

background_label = Label(ventana, image=background_image)

background_label.place(x=0, y=0, relwidth=1, relheight=1)



############################ Botones y texto principal #####################################################################################################
Label(ventana,text="¿Cuántos desea buscar?",fg="white",font="none 10",bg="Red4").place(x=360,y=42)
Label(ventana,text="Nombre",fg="black",font="none 10",bg="gray89").place(x=390,y=95)
Label(ventana,text="ID",fg="black",font="none 10",bg="gray87").place(x=360,y=95)

textentry = Entry(ventana,width=18,bg="white")
textentry.place(x=523,y=43)

Button(ventana,text="Buscar",command=lambda:sacarN(),width=6,state="normal",relief="groove").place(x=655,y=38)

Button(ventana,text="Ver mis pokémones",width=19,height=1,command=lambda:verMisPokemones(),relief="flat",bg="yellow1",activebackground="yellow1",
       justify="left").place(x=619,y=375)

c,n1,n2,n3,b1,b2,b3,x1,x2,x3,sig,back,ID1,ID2,ID3,p,p1,p2,p3 = 0,Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button(),Label(),Label(),Label(),Label(),Label(),Label(),Label()

n = 0

############################ Funciones ######################################################################################################################

def sacarN():
    global n
    n = textentry.get()
    buscadorPokemon(n)
    textentry.delete(0,"end")
    

def buscadorPokemon(n):
    global c
    """
    Funcionamiento: Desarrolla una matriz con el siguiente orden: [[id,nombre,URL,[icobo,peso,largo]]], con [[int,str,str,[str,int,int]]] respetivamente
    Entrada: Un numero, el cual sera el n del rango de pokemones, es decir, desde 1 hasta dicho numero.(int)
    Salida: Una matriz con la informacion de cada pokemon.
    """
    
    if n.isdigit():
        if 0<int(n)<=949:
            try:
                mb.place(x=710,y=38)
                URL_API = 'https://pokeapi.co/api/v2/pokemon/?limit='+str(n)
                lista_de_pokemones = []
                info_del_pokemon = requests.get(URL_API)
                jsonToPython = json.loads(info_del_pokemon.content)
                for i in range(int(n)):
                    info = (jsonToPython["results"])[i]
                    URL = info["url"]
                    name = info["name"]
                    listaURL = URL.split("/")
                    ID = listaURL[-2]
                    if len(str(ID)) == 2:
                        ID = "0" + ID
                    if len(str(ID)) == 1:
                        ID = "00" + ID
                    pokemon = []
                    pokemon.append(ID)
                    pokemon.append(name)
                    pokemon.append(URL)
                    lista_de_pokemones.append(pokemon)
                    global lista
                    lista= lista_de_pokemones
                c = 0
                sacarNombres(lista,n)
            except:
                retry = messagebox.askretrycancel("Error", "No hay conexion con el servidor")
                if retry == True:
                    return buscadorPokemon(n)
        else:
            messagebox.showerror("Error", "Ingrese un rango entre 1-949")
    else:
        messagebox.showerror("Error", "Ingrese un número válido.")
    

def sacarNombres(lista,n):
    global c,n1,n2,n3,b1,b2,b3,x1,x2,x3,ID1,ID2,ID3,p,p1,p2,p3,sig,back

    n1.destroy()
    n2.destroy()
    n3.destroy()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    x1.destroy()
    x2.destroy()
    x3.destroy()
    ID1.destroy()
    ID2.destroy()
    ID3.destroy()
    p.destroy()
    p1.destroy()
    p2.destroy()
    p3.destroy()
    sig.destroy()
    back.destroy()
    

    ID1=Label(ventana,bg='gray87')
    ID1.place(x=360,y=130)
    ID2=Label(ventana,bg='gray87')
    ID2.place(x=360,y=180)
    ID3=Label(ventana,bg='gray87')
    ID3.place(x=360,y=230)
    
    if(len(lista) - c != 0):
        if(len(lista[c]) == 4):
            p = Label(ventana,bg='gray87',text = "Peso")
            p.place(x=525,y=95)
            p1 = Label(ventana,bg='white')
            p1.place(x=525,y=133)
            p2 = Label(ventana,bg='white')
            p2.place(x=525,y=183)
            p3 = Label(ventana,bg='white')
            p3.place(x=525,y=233)
        else:
            p.destroy()
          

    n1 = Button(ventana,width=15,relief="groove",bg="gray85")
    n1.place(x=390,y=130)
    n2 = Button(ventana,width=15,relief="groove",bg="gray85")
    n2.place(x=390,y=180)
    n3 = Button(ventana,width=15,relief="groove",bg="gray85")
    n3.place(x=390,y=230)

    b1 = Button(ventana,text="Guardar en Binario",width=15,command=lambda:misPokemons(pokemonEscogido(lista[c][0])),bg="turquoise3",relief="ridge")
    b1.place(x=565,y=130)
    b2 = Button(ventana,text="Guardar en Binario",width=15,command=lambda:misPokemons(pokemonEscogido(lista[c+1][0])),bg="turquoise3",relief="ridge")
    b2.place(x=565,y=180)
    b3 = Button(ventana,text="Guardar en Binario",width=15,command=lambda:misPokemons(pokemonEscogido(lista[c+2][0])),bg="turquoise3",relief="ridge")
    b3.place(x=565,y=230)
    
    x1=Button(ventana,text="Guardar en XML",command=lambda:agregarArchivo(pokemonEscogido(lista[c][0])),width=15,bg="yellow2",relief="ridge")
    x1.place(x=680,y=130)
    x2=Button(ventana,text="Guardar en XML",command=lambda:agregarArchivo(pokemonEscogido(lista[c+1][0])),width=15,bg="yellow2",relief="ridge")
    x2.place(x=680,y=180)
    x3=Button(ventana,text="Guardar en XML",command=lambda:agregarArchivo(pokemonEscogido(lista[c+2][0])),width=15,bg="yellow2",relief="ridge")
    x3.place(x=680,y=230)

    sig = Button(ventana,text="siguiente",command=lambda:siguiente(lista,n),width=15,relief="ridge",bg="gray85")
    sig.place(x=680,y=300)
    back = Button(ventana,text="atras",command=lambda:atras(lista,n),width=15,relief="ridge",bg="gray85")
    back.place(x=390,y=300)

    if len(lista) - c != 0:
        n1.config(text = lista[c][1])
        n1.config(command=lambda:abrirventana1(pokemonEscogido(lista[c][0]),c))
        x1.config(command=lambda:sacarXML(pokemonEscogido(lista[c][0])))
        ID1.config(text=lista[c][0])
        if(len(lista[c]) == 4):
            p1.config(text=lista[c][3])
    else:
        n1.destroy()
        x1.destroy()
        b1.destroy()
        ID1.destroy()
        try:
            p1.destroy()
        except:
            pass
    if len(lista) - c > 1:
        n2.config(text = lista[c+1][1])
        n2.config(command=lambda:abrirventana1(pokemonEscogido(lista[c+1][0]),c+1))
        x2.config(command=lambda:agregarArchivo(pokemonEscogido(lista[c+1][0])))
        ID2.config(text=lista[c+1][0])
        if(len(lista[c + 1]) == 4):
            p2.config(text=lista[c + 1][3])
    else:
        n2.destroy()
        x2.destroy()
        b2.destroy()
        ID2.destroy()
        try:
            p2.destroy()
        except:
            pass
    if len(lista) - c > 2:
        n3.config(text = lista[c+2][1])
        n3.config(command=lambda:abrirventana1(pokemonEscogido(lista[c+2][0]),c+2))
        x3.config(command=lambda:agregarArchivo(pokemonEscogido(lista[c+2][0])))
        ID3.config(text=lista[c+2][0])
        if(len(lista[c + 2]) == 4):
            p3.config(text=lista[c + 2][3])
    else:
        n3.destroy()
        x3.destroy()
        b3.destroy()
        ID3.destroy()
        try:
            p3.destroy()
        except:
            pass
    if c == 0:
        back.destroy()
    if int(len(lista)) - c <= 3:
        sig.destroy()

def siguiente(lista,n):
    global c
    c = c + 3
    sacarNombres(lista,n)

def atras(lista,n):
    global c
    c = c - 3
    sacarNombres(lista,n)


def verMisPokemones():
    archivo = open("misPokemons","rb")
    lista= pickle.load(archivo)
    lista= lista[4:]
    listaNueva=[]
    for i in lista:
        listaNueva.append(i[:-1])
    global c
    c=0
    return sacarNombres(listaNueva,len(listaNueva))
    


mb=  Menubutton (ventana, text="Filtrar", relief="ridge",width=6 )
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu
pesoVar = IntVar()
nombreVar = IntVar()
mb.menu.add_checkbutton ( label="→ Por Peso",variable=pesoVar ,command=lambda:entradasPeso())
mb.menu.add_checkbutton (label="→ Por Nombre",variable=nombreVar,command=lambda:entradasNombre())

def entradasNombre():
    mb.place_forget()
    global filtro,filtroText,button1
    filtroText=Label(ventana,text="Filtro:",fg="white",font="none 10",bg="Red4")
    filtroText.place(x=350,y=365)
    filtro = Entry(ventana, width=10)
    filtro.place(x=400,y=367)
    button1 = Button(ventana, text="Filtrar", command=filtrarNombre,width=6,state="normal",relief="groove")
    button1.place(x=470,y=365)
def filtrarNombre():
    global c, lista
    listaFiltrada = []
    if filtro.get().isdigit() and filtro.get() != "":
        messagebox.showerror("Error", "Se deben ingresar letras o palabras unicamente.")
    else:
        for pokemon in lista:
            nombre = pokemon[1]
            if filtro.get() in nombre:
                listaFiltrada.append(pokemon)
        if filtro.get() != "" and len(listaFiltrada) == 0:
            messagebox.showerror("Error", "No se encontraron pokemones.")
        else:
            c = 0
            lista = listaFiltrada
            sacarNombres(lista,n)
            
    if filtro.get() == "":
        buscadorPokemon(n)
        sacarNombres(lista,n)
    filtro.destroy()
    button1.destroy()
    filtroText.place_forget()

def entradasPeso():
    mb.place_forget()
    global desde, hasta,desdeText,hastaText,button2
    desdeText=Label(ventana,text="Desde:",fg="white",font="none 9",bg="Red4")
    desdeText.place(x=350,y=370)
    desde = Entry(ventana, width=10)
    desde.place(x=400,y=370)
    hastaText=Label(ventana,text="Hasta: ",fg="white",font="none 9",bg="Red4")
    hastaText.place(x=350,y=390)
    hasta = Entry(ventana, width=10)
    hasta.place(x=400,y=390)
    button2 = Button(ventana, text="Filtrar", command=avisoTiempo,width=6,state="normal",relief="groove")
    button2.place(x=470,y=384)
def avisoTiempo():
    if desde.get().isdigit() and hasta.get().isdigit():
        aviso = messagebox.askokcancel("Aviso", "Este proceso tardara varios minutos, incluso horas dependiendo del rango a filtrar.")
        if aviso == True:
            filtrarPeso()
    else:
        messagebox.showerror("Error", "Se deben ingresar numeros enteros.")
def filtrarPeso():
    listaFiltrada = []
    for pokemon in lista:
        peso = (json.loads(requests.get('http://pokeapi.co/api/v2/pokemon/'+pokemon[0]).content))["weight"]
        if int(desde.get())<int(peso)<int(hasta.get()):
            pokemon.append(peso)
            listaFiltrada.append(pokemon)

    messagebox.showinfo("Atencion","Proceso Terminado.")
            
    desdeText.destroy()
    desde.destroy()
    hastaText.destroy()
    hasta.destroy()
    button2.destroy()
    return sacarNombres(listaFiltrada,len(listaFiltrada))



def abrirventana1(lista,c):
    
    pilImage = Image.open(BytesIO(requests.get(lista[3][0]).content)).resize((180, 180))


    image2 = ImageTk.PhotoImage(pilImage)

    photo=Label(image=image2,bg="white").place(x=80,y=70)
    
    np1=Label(text="Nombre:",fg="black",font="none 10",bg="white")
    np2=Label(text=lista[1]+"    ",fg="black",font="none 10",bg="white")

    ep1=Label(text="Estatura:",fg="black",font="none 10",bg="white")
    ep2=Label(text=lista[3][2]+"   ",fg="black",font="none 10",bg="white")

    pp1=Label(text="Peso: ",fg="black",font="none 10",bg="white")
    pp2=Label(text=lista[3][1]+"   ",fg="black",font="none 10",bg="white")

    np2.place_forget()

    ep2.place_forget()

    pp2.place_forget()
    
    np1.place(x=80,y=250)
    np2.place(x=150,y=250)

    ep1.place(x=80,y=290)
    ep2.place(x=150,y=290)

    pp1.place(x=80,y=330)
    pp2.place(x=150,y=330)
  

    ventana.mainloop()



ventana.mainloop()

