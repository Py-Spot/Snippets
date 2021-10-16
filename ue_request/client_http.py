import requests
import serverdaten
r = requests.post(serverdaten.server_ip, data={'foo': 'bar'})
print(r.text)
