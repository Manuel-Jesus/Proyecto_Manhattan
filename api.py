import requests
from getpass import getpass


usuario=raw_input('Introduce tu usuario(nombre@gmail.com): ')
passwd=getpass('Introdice tu clave: ')

#creamos la valiable con los datos que vamos a pasar posteriormente
datos={'Email':usuario, 'Passwd':passwd}
#enviamos los datos para solicitar el token
r=requests.post("https://www.google.com/accounts/Clientlogin", data=datos)
# En r esta el token


#el .text serviria para mostrarlo como texto
print r.text




#peticion = requests.get("https://apps-apis.google.com/a/feeds/emailsettings/2.0/gmail.com/testmanhattan/label")

#texto = peticion.text

#print (texto)
