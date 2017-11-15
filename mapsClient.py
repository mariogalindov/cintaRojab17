import googlemaps 

from datetime import datetime 

now = datetime.now()
print(now)

gmaps = googlemaps.Client(key= 'AIzaSyDK5jp6Tr7tGNXmN7f0nbSFVtai5lFmhDI')

origen = "Dev.f, Roma Norte, Ciudad de México, CDMX"
destino = "Bosque Esmeralda, Ciudad López Mateos, Méx."

direccion = gmaps.directions(origen, destino, mode = "driving", departure_time= now)

print(direccion)