import smtplib
import requests
from lxml import etree
from bottle import Bottle, run, template,post,request



bottle = Bottle()#La aplicacion

@bottle.route('/')#pagina de inicio
def home_page():
    return template('index')#simplemente nos devuelve la plantilla de la pagina de inicio




@bottle.post('/salida')
def salida():
	correo_origen = request.forms.get('origen')  #raw_input('Correo electronico de origen: ')
	passwd=request.forms.get('password')
        correo_destino=request.forms.get('destino')
        contenidomail=request.forms.get('texto')
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
        conexion=smtplib.SMTP('smtp.gmail.com:587')
        conexion.ehlo()
        conexion.starttls()
        conexion.login(correo_origen,passwd)
        conexion.sendmail(correo_origen,correo_destino,contenidomail)
	return template('salidaTest',{'CorreoOrigen':correo_origen,'CorreoDestino':correo_destino,'contenido':contenidomail,'labels':labels})



run(bottle, host='localhost', port=8080)
