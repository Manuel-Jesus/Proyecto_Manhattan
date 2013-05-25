import smtplib
#import gdata.apps.emailsettings.client
from getpass import getpass
import requests
from lxml import etree
from bottle import Bottle, run, template,post,request

#'manueljesus@mark6.mygbiz.com' 


correo_origen = 'manueljesus@mark6.mygbiz.com'  #raw_input('Correo electronico de origen: ')
passwd=getpass('PASSWORD: ')
#correo_destino = raw_input('Correo electronico de destino: ')
#mensaje = raw_input('Introduce el correo que desee enviar: ')



## conexion a gmail
#conexion = smtplib.SMTP('smtp.gmail.com:587') # este es el servidor de correos gmail
##las sisguientes lineas forman parte del protocolo smtp
#conexion.ehlo()
#conexion.starttls()
#conexion.ehlo()
#conexion.login(correo_origen,passwd)
#conexion.sendmail(correo_origen, correo_destino, mensaje)#esta linea es la que envia el correo, si se pusuera mas veces se enviaria dichas veces el correo

#conexion.quit() #esta linea evidentemente cierra la conexion








datos={'Email':correo_origen, 'Passwd':passwd,'service':'apps'}#service: apps es lo que nos faltaba antes! NOTA: DIFERENCIA MAYUSCULAS DE MINUSCULAS
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
pet=requests.get('https://apps-apis.google.com/a/feeds/emailsettings/2.0/mark6.mygbiz.com/manueljesus/label',headers=headers)


#print pet.text#comentar si solo se quiere el token


kd = pet.text
#print kd
xml = etree.fromstring(kd.encode('utf-8'))



lista=xml.xpath("//text()")
print lista
a= len(lista)


contadorLista=0
labels=list()
for i in range(3, a-1):
  if i%2!=0:
	  indice=lista[i].rfind("/label/")
	  labels.append(lista[i][indice+7:len(lista[i])])
print labels



#pet2=requests.get('https://apps-apis.google.com/a/feeds/emailsettings/2.0/mark6.mygbiz.com/manueljesus/forwarding',headers=headers)

#print pet2.text

#pet3=requests.get('https://apps-apis.google.com/a/feeds/emailsettings/2.0/mark6.mygbiz.com/manueljesus/pop',headers=headers)

#print pet3.text

#pet4=requests.get('https://apps-apis.google.com/a/feeds/emailsettings/2.0/mark6.mygbiz.com/manueljesus/signature',headers=headers)

#print pet4.text



#resp_xml = etree.fromstring(pet.text)


bottle = Bottle()

@bottle.route('/login')
def home_page():
    return template('index')




@bottle.post('/salida')
def salida():
	correo_origen = request.forms.get('name')  #raw_input('Correo electronico de origen: ')
	passwd=request.forms.get('password')
	datos={'Email':correo_origen, 'Passwd':passwd,'service':'apps'}
	r=requests.post('https://www.google.com/accounts/Clientlogin', data=datos)
	indice=(r.text).rfind("Auth=")
	token=(r.text)[indice+5:len(r.text)-1]
	headers = {'content-type': 'application/atom+xml','Authorization':'GoogleLogin auth='+token}
	pet=requests.get('https://apps-apis.google.com/a/feeds/emailsettings/2.0/mark6.mygbiz.com/manueljesus/label',headers=headers)
	kd = pet.text
	xml = etree.fromstring(kd.encode('utf-8'))
	lista=xml.xpath("//text()")
	print lista
	a= len(lista)
	contadorLista=0
	labels=list()
	for i in range(3, a-1):
		if i%2!=0:
			indice=lista[i].rfind("/label/")
			labels.append(lista[i][indice+7:len(lista[i])])
    return template('salidaTest',CorreoOrigen=,CorreoDestino=passwd,contenido=labels[0] )

run(bottle, host='localhost', port=8080)
