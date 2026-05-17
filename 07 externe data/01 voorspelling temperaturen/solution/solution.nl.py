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
doel = float(input("Geef de doeltemperatuur op:"))

aantal = -1
for i in range(len(temperaturen)):
    temp = temperaturen[i]
    if temp >= doel and aantal == -1:
        aantal = i

if aantal == -1:
    print(f"De temperatuur {doel} °C wordt in de nabije toekomst niet bereikt.")
elif aantal == 0:
    print(f"Om middernacht was het al {doel} °C.")
elif aantal == 1:
    print(f"De temperatuur {doel} °C wordt bereikt na 1 uur.")
else:
    print(f"De temperatuur {doel} °C wordt bereikt na {aantal} uren.")
