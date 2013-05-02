import requests
#creamos la valiable con los datos que vamos a pasar posteriormente

usuario='XXXXXXXXX@gmail.com'
passwd='XXXXXXXXX'

datos={'Email':usuario, 'Passwd':passwd}
#enviamos los datos para solicitar el token
r=requests.post("https://www.google.com/accounts/Clientlogin", data=datos)
# En r esta el token
print r.content


l=requests.post("google.com/accounts/IssueAuthToken")

print l.text


archivos={'':(open('file.xml','rb'))}
headers = {'content-type': 'application/atom+xml','Authorization':'GoogleLogin auth='+r.text}
pet=requests.post('https://apps-apis.google.com/a/feeds/emailsettings/2.0/titaniumsystem.mygbiz.com/manueljesus/label',headers=headers,data=archivos)

print pet.text
