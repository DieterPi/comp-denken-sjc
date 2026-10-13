jaartal = int(input("Geef het jaartal in: "))

eeuw = (jaartal - 1) // 100 + 1
decennium = (jaartal - 1) % 100 // 10 + 1

print(f"{jaartal} behoort tot het {decennium} e decennium van de {eeuw} e eeuw.")
