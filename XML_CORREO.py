from xml.etree.ElementTree import Element, SubElement, tostring
from tkinter import messagebox
import pickle
import email
import smtplib
import imaplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
pokemons = [['001', 'bulbasaur', 'http://pokeapi.co/api/v2/pokemon/1', ['https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png', 69, 7]],['002', 'ivysaur', 'http://pokeapi.co/api/v2/pokemon/1', ['https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png', 69, 7]],['003', 'venasaur', 'http://pokeapi.co/api/v2/pokemon/1', ['https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png', 69, 7]]]
#matriz = ['002', 'ivysaur', 'http://pokeapi.co/api/v2/pokemon/1', ['https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png', 69, 7]]
#ID=matriz[0]

def archivoInicialXML():
    pokemon=Element("Pokemons")
    ID=SubElement(pokemon,"id")
    ID.text="ID de Prueba"
    name= SubElement(pokemon,"name")
    name.text="Nombre"
    URL=SubElement(pokemon,"URL")
    URL.text="URL de prueba"
    icono=SubElement(pokemon,"icono")
    icono.text="Icono de prueba"
    peso=SubElement(pokemon,"peso")
    peso.text="Peso de prueba"
    altura=SubElement(pokemon,"altura")
    altura.text="Altura de Prueba"
    XML=tostring(pokemon)
    archivo=open("pokemonsXML.xml","wb")
    pickle.dump(XML,archivo)
    archivo.close()
    
def agregarArchivo(matriz):
    ID=matriz[0]
    archivo=open("pokemonsXML.xml","rb")
    linea=archivo.readline()
    print(str(linea))
    for i in linea:
        if ID in str(linea):
            messagebox.showinfo("Informacion","El pokemon ya fue agregado al archivo")
            break
        else:
            return sacarXML(matriz)
    return ""
    
def sacarXML(lista):
    """
    Entrada: Recibe una lista con la información de un pokemon predeterminado.
    Salida: Imprime la información de este pokemon de acuerdo a el standard de información XML.
    Funcionamiento: Mediante el uso de una librería especifica de XML se prosigue a convertir cada uno de los datos provenientes de la lista en elementos y subelementos de acuerdo a la clasificación XML.
    """
    matriz = lista
    pokemon = Element('Pokemons')
    ID = SubElement(pokemon, 'id')
    ID.text = matriz[0]
    name = SubElement(pokemon, 'nombre')
    name.text = matriz[1]
    URL = SubElement(pokemon, 'URL')
    URL.text = matriz[2]
    icono = SubElement(pokemon, 'icono')
    icono.text = matriz[3][0]
    peso = SubElement(pokemon, 'peso')
    peso.text = str(matriz[3][1])
    altura = SubElement(pokemon, 'altura')
    altura.text = str(matriz[3][2])
    print(tostring(pokemon))
    XML=tostring(pokemon)
    archivo=open("pokemonsXML.xml","ab")
    pickle.dump(XML,archivo)
    archivo.close()      
    toaddress=input("Digite la cuenta de correo a la cual desea enviar la información: ")
    return (validarCorreo(toaddress,archivo))

def validarCorreo(toaddress,archivo):
    """
    Entrada: El programa se encarga de recibir un correo electronico, mientras se cumplan las condiciones definidas de presentar una @ y puntos. Continuará solicitando el número del cifrado que se necesita
    Salidas: En caso de que no se introduzca un correo correcto, se le será indicado al usuario, si se cumple, se solicita la información necesaria con un cifrado y prosigue a continuar con la opcion del cifrado solicitada.
    Funcionamiento: Prosigue a verificar que los datos introducidos sean los correspondientes a un correo electronico, si no, será regresado que no lo es y prosiguira a preguntar de nuevo. Si lo es, prosigue a avanzar a la opcion de cifrado solicitada.
    """
    if '@' in toaddress and '.' in toaddress:
        return enviar_correo(toaddress) 
    else:
        print('La información ingresada no es un correo electronico')
        print()
        toaddress=input('Ingrese el correo electronico deseado: ')
        validarCorreo(toaddress,archivo)

def enviar_correo(toaddress):
    try:
        email_user = 'tp2taller2018@gmail.com'
        email_password = 'tareaprogramada2'
        email_send = toaddress

        subject = 'Archivo XML'

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        body = 'Adjunto el archivo con los pokemon en formato xml'
        msg.attach(MIMEText(body,'plain'))

        filename='pokemonsXML.xml'
        attachment  =open(filename,'rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_password)


        server.sendmail(email_user,email_send,text)
        server.quit()
        print("Su correo fue enviado correctamente")
    except:
        print("Ha ocurrido un error al enviar el correo")

archivoInicialXML()
