import requests

peticion = requests.get("https://apps-apis.google.com/a/feeds/emailsettings/2.0/gmail.com/testmanhattan/label")

texto = peticion.text

print (texto)
