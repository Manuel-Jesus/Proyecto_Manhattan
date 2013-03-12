import smtplib
#import gdata.apps.emailsettings.client
from getpass import getpass

correo_origen = raw_input('Correo electronico de origen: ')
correo_destino = raw_input('Correo electronico de destino: ')
mensaje = raw_input('Introduce el correo que desee enviar: ')


usuario = raw_input('Usuario de Gmail: ')
password = getpass('Introduce el Password: ')

# conexion a gmail
conexion = smtplib.SMTP('smtp.gmail.com:587') # este es el servidor de correos gmail
#las sisguientes lineas forman parte del protocolo smtp
conexion.ehlo()
conexion.starttls()
conexion.ehlo()
conexion.login(usuario,password)
conexion.sendmail(correo_origen, correo_destino, mensaje)#esta linea es la que envia el correo, si se pusuera mas veces se enviaria dichas veces el correo

conexion.quit() #esta linea evidentemente cierra la conexion

