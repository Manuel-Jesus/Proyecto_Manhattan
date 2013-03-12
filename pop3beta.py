#protocolo para recibir correo
import poplib
from getpass import getpass


pop3 = poplib.POP3_SSL('pop.gmail.com',995)
#en la sigueinte linea conectaremos en el pop de gmail,
#ssl es el tipo de cifrado que usa y '995' es el puerto por el que se conecta a pop de gmail

correopop = raw_input('Introduce tu correo: ')
passwordpop = getpass ('Introduce el password: ')




pop3.user (correopop)
pop3.pass_(passwordpop)
#pop3.user / pop3.pass_ 

nummensaje = pop3.list()[1]
#la linea anterior es la lista que te da todos los mensajes
print (nummensaje)
	
#print "Primer correo"
	
print pop3.retr(len(nummensaje))
#nos muestra el ultimo mensaje recibido
