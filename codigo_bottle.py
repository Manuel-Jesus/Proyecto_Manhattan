import smtplib
import requests
from lxml import etree
from bottle import run, route, template,post,request,static_file, debug




#bottle = Bottle()#La aplicacion

@route('/style/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./style')

@route('/')#pagina de inicio
def home_page():
    return template('index')#simplemente nos devuelve la plantilla de la pagina de inicio




@post('/salida')
def salida():
	correo_origen = request.forms.get('origen')  #raw_input('Correo electronico de origen: ')
	passwd=request.forms.get('password')
        correo_destino=request.forms.get('destino')
        contenidomail=request.forms.get('texto')
	datos={'Email':correo_origen, 'Passwd':passwd,'service':'apps'}
        #en estas 3 lineas que vienen a continuacion vamos a separar el correo entre su dominio y el usuario. Se utilizara mas adelante.
        indice=correo_origen.rfind("@")
        solo_correo=correo_origen[:indice]
        solo_dominio=correo_origen[indice+1:]
	#service: apps es lo que nos faltaba antes! NOTA: DIFERENCIA MAYUSCULAS DE MINUSCULAS
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
	pet=requests.get('https://apps-apis.google.com/a/feeds/emailsettings/2.0/'+solo_dominio+'/'+solo_correo+'/label',headers=headers)
        #en la linea anterior hemos utilizado el dominio y el correo
	kd = pet.text
	#nos devuelve la petion y dentro de ella se podria ver los datos que queremos imprimir
	xml = etree.fromstring(kd.encode('utf-8'))
	#el etree es lo que recore la respuesta que nos da la api
	lista=xml.xpath("//text()")
	print lista
	a= len(lista)
	contadorLista=0
	labels=list()
        for i in range(3, a-1):
          if i%2!=0:
            indice=lista[i].rfind("/label/")
            labels.append(lista[i][indice+7:len(lista[i])])
	#en el for que es para que solo se muestre por pantalla la label y no todo lo que gmail nos manda
	
	# conexion a gmail
        conexion=smtplib.SMTP('smtp.gmail.com:587')
		#Las siguientes lineas forman parte del protocolo smtp
        conexion.ehlo()
        conexion.starttls()
        conexion.login(correo_origen,passwd)
        conexion.sendmail(correo_origen,correo_destino,contenidomail)
	#esta linea es la que envia el correo, si se pusuera mas veces se enviaria dichas veces el correo
        conexion.quit() #esta linea evidentemente cierra la conexion
	return template('salida',{'CorreoOrigen':correo_origen,'CorreoDestino':correo_destino,'contenido':contenidomail,'labels':labels})


debug(True)
run(host='localhost', port=8080)
