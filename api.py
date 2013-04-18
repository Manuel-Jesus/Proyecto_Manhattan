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
#print r.text




datos={'Content-type':'application/atom+xml', 'Authoritation':r.text}

t=requests.get("https://apps-apis.google.com/a/feeds/emailsettings/2.0/titaniumsystem.mygbiz.com/manueljesus/label",data=datos);

print t.text
