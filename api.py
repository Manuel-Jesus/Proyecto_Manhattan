import requests
from getpass import getpass

usuario="manueljesus@titaniumsystem.mygbiz.com"
passwd=getpass('PASSWORD: ')

datos={'Email':usuario, 'Passwd':passwd,'service':'apps'}#service: apps es lo que nos faltaba antes! NOTA: DIFERENCIA MAYUSCULAS DE MINUSCULAS
#enviamos los datos para solicitar el token
r=requests.post('https://www.google.com/accounts/Clientlogin', data=datos)
# En r esta el token
#print r.content #lo que hay que hacer es coger el auth pegarlo en la peticion de abajo en la parte de headers

indice=(r.text).rfind("Auth=")
#print indice
token=(r.text)[indice+5:len(r.text)-1]
#print token

#la autentificacion va en las cabeceras
#archivos={'':(open('file.xml','rb'))}#para el futuro, posible necesidad de archivo.
headers = {'content-type': 'application/atom+xml','Authorization':'GoogleLogin auth='+token}
pet=requests.get('https://apps-apis.google.com/a/feeds/emailsettings/2.0/titaniumsystem.mygbiz.com/manueljesus/label',headers=headers)

print pet.text#comentar si solo se quiere el token
