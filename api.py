import gdata.apps.emailsettings.client
from getpass import getpass


dominio = raw_input('Introduce el dominio que quieres: ')
usuario = raw_input('Introduce el Nombre de Usuario(usuario@dominion.com): ')
passwd = getpass('Introduce la clave: ')

client = gdata.apps.emailsettings.client.EmailSettingsClient(domain= dominio)
client.ClientLogin(email = usuario , password = passwd , source = 'Proyecto Manhattan')
