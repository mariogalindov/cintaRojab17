import requests

URL = "https://maps.googleapis.com/maps/api/directions/json?origin=Impact+Hub+Roma Norte,+MX&destination=Zócalo+Plaza+de+la+Constitución,+MX+07073&key=AIzaSyDK5jp6Tr7tGNXmN7f0nbSFVtai5lFmhDI"

mapa = requests.get(URL)
print(mapa.status_code)
print(mapa.json())



#AIzaSyDK5jp6Tr7tGNXmN7f0nbSFVtai5lFmhDI