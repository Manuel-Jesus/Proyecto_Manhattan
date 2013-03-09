#protocolo para recibir correo
import poplib
from getpass import getpass


pop3 = poplib.POP3_SSL('pop.gmail.com',995)
#en la sigueinte linea conectaremos en el pop de gmail,
#ssl es el tipo de cifrado que usa y '995' es el puerto por el que se conecta a pop de gmail

pop3.user ('testmanhattan@gmail.com')
pop3.pass_('robert90')
#pop3.user / pop3.pass_ 

print 

