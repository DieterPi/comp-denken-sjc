# Onderstaande code haalt een lijst op, waarin een voorspelling 
# staat van de temperaturen gedurende de volgende uren in Aalst.
import urllib.request
req = urllib.request.Request("https://api.open-meteo.com/v1/forecast?latitude=50.9384&longitude=4.0334&hourly=temperature_2m", 
                             headers={'User-Agent': 'Mozilla/5.0'})
resp =  urllib.request.urlopen(req)
data = eval(resp.read().decode().replace('false', 'False').replace('true', 'True'))

temperaturen = data["hourly"]["temperature_2m"]
# Deze bevat gegevens als [16.1, 17.2, 15.1, ..., 20.2]
# waarbij 16.1 de temperatuur van vandaag om middernacht is,
# 17.2 de temperatuur om 01.00 u. 's nachts,
# 15.1 de temperatuur om 02.00 u. 's nachts,
# ... enz...


# Schrijf HIERONDER het gevraagde programma
