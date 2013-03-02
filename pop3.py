import gdata.apps.emailsettings.client


client = gdata.apps.emailsettings.client.EmailSettingsClient(domain='yourdomain')
client.ClientLogin(email='adminUsername@yourdomain', password='adminPassword', source='your-apps')
client.UpdatePop(username='liz', enable=False)
