import gdata.apps.emailsettings.client
from getpass import getpass


dominio = raw_input('Introduce el dominio que quieres: ')
correo = raw_input('Introduce el Nombre de Usuario(usuario@dominion.com): ')
usuario = raw_input('Introduce el nombre de usuario: ')
nombrefiltro = raw_input('Introduce el nombre del filtro a crear: ')
passwd = getpass('Introduce la clave: ')

client = gdata.apps.emailsettings.client.EmailSettingsClient(domain= dominio)
client.ClientLogin(email = usuario , password = passwd , source = 'Proyecto Manhattan')
client.CreateLabel (username = usuario, name = nombrefiltro)
