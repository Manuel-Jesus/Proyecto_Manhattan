import smtplib
import requests
from lxml import etree
from bottle import run, route,get, template,post,request,static_file, debug
from requests_oauthlib import OAuth1
from urlparse import parse_qs

#variables requeridas para oAuth 
REQUEST_TOKEN_URL = "https://www.google.com/accounts/OAuthGetRequestToken"
AUTHENTICATE_URL = "https://www.google.com/accounts/OAuthAuthorizeToken?oauth_token="
ACCESS_TOKEN_URL = "https://www.google.com/accounts/OAuthGetAccessToken"
 
CONSUMER_KEY = "750829952488.apps.googleusercontent.com"
CONSUMER_SECRET = "9PZBykCAfYiM1bNGZlICBwh3"
# Definimos los parametros SCOPE y CALLBACK_URI
SCOPE = "https://apps-apis.google.com/a/feeds/emailsettings/2.0/ https://www.googleapis.com/auth/userinfo.email"#scope necesario y ES SEPARADO POR ESPACIOS
#si eliminamos el segundo scope no llegamos a obtener la direccion de correo del cliente, la cual es necesaria para realizar las peticiones de labels
CALLBACK_URI = "http://localhost:8080/oauth2callback"

TOKENS = {}
#funciones previas a oauth: peticion de la url

def get_request_token():
# La cabecera oauth lleva en este caso el parametro callback_uri
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   callback_uri=CALLBACK_URI,
    )
# Enviamos por POST el parametro scope
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth, data={"scope":SCOPE})
    print r.text
    credentials = parse_qs(r.content)
    TOKENS["request_token"] = credentials.get('oauth_token')[0]
    TOKENS["request_token_secret"] = credentials.get('oauth_token_secret')[0]
 

def get_access_token(TOKENS):
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["request_token"],
                   resource_owner_secret=TOKENS["request_token_secret"],
                   verifier=TOKENS["verifier"],
    )
 
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    TOKENS["access_token"] = credentials.get('oauth_token')[0]
    TOKENS["access_token_secret"] = credentials.get('oauth_token_secret')[0]







#bottle = Bottle()#La aplicacion

@route('/style/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./style')



@route('/style/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./style')

@route('/')#pagina de inicio
def home_page():
    get_request_token()
    authorize_url = AUTHENTICATE_URL + TOKENS["request_token"]
    return template('index.tpl', enlaceOauth=authorize_url)
#ahora la pagina de inicio incluye un enlace para oauth, sacar el enlace requiere un poco mas de trabajo



def get_labels(token,correo):
    indice=correo.rfind("@")
    solo_correo=correo[:indice]
    solo_dominio=correo[indice+1:]
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
    print lista
    contadorLista=0
    labels=list()
    for i in range(3, a):
        if i%2!=0:
            indice=lista[i].rfind("/label/")
            labels.append(lista[i][indice+7:len(lista[i])])
	#en el for que es para que solo se muestre por pantalla la label y no todo lo que gmail nos manda
    return labels



@post('/salida')
def salida():
	correo_origen = request.forms.get('origen')  #raw_input('Correo electronico de origen: ')
	passwd=request.forms.get('password')
        correo_destino=request.forms.get('destino')
        contenidomail=request.forms.get('texto')
	datos={'Email':correo_origen, 'Passwd':passwd,'service':'apps'}
       
	r=requests.post('https://www.google.com/accounts/Clientlogin', data=datos)

	indice=(r.text).rfind("Auth=")

	token=(r.text)[indice+5:len(r.text)-1]
        labels=get_labels(token,correo_origen)
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



@get('/oauth2callback')
def get_verifier():
    TOKENS["verifier"] = request.query.oauth_verifier
    print TOKENS["verifier"]
    get_access_token(TOKENS)
    token=   TOKENS["access_token"]
    print token
    token=token[:len(token)]
    print token
    headers = {'content-type': 'application/atom+xml','Authorization':'GoogleLogin auth='+token}
    pet=requests.get('https://apps-apis.google.com/a/feeds/emailsettings/2.0/'+'mark6.mygbiz.com'+'/'+'manueljesus'+'/label',headers=headers)
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
    print labels
#    TOKENS.extend(labels)
    print TOKENS
    return template('salida',{'CorreoOrigen':'VERSION EN DESAROLLO','CorreoDestino':'Con oauth no se puede enviar un correo','contenido':'Esta es una version en desarollo. En lugar de las labels imprimiremos en primer lugar todo lo recibido por google, y luego la respuesta al hacer la peticion de labels','labels':lista})
# return lista

debug(True)
run(host='localhost', port=8080)


