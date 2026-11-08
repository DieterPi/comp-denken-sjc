a = int(input("Geef het aantal minuten dat de hond agressief is: "))
r = int(input("Geef het aantal minuten dat de hond rustig is: "))
tijdstip = int(input("Geef in na hoeveel minuten de postbode langskomt: "))

if 0 < tijdstip % (a + r) <= a:
    print("De hond is agressief.")
else:
    print("De hond is rustig.")
