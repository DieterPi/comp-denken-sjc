file = float(input("Geef de bestandsgrootte (in GB): "))
speed = float(input("Geef de downloadsnelheid (in Mbps): "))

file_mb = file * 1000
speed_mb = speed / 8

time = file_mb / speed_mb
time_min = time / 60

print(f"Het duurt {round(time_min, 2)} minuten om een bestand van {file} GB te downloaden.")
