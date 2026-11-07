dems = int(input("Geef het aantal zetels voor de Democraten: "))
reps = int(input("Geef het aantal zetels voor de Republikeinen: "))

meerderheid = (dems + reps) // 2 + 1

if dems == reps:
    print("De Democraten moeten minstens één zetel veroveren een meerderheid.")
    print("De Republikeinen moeten minstens één zetel veroveren een meerderheid.")
else:
    veroveren = meerderheid - min(dems, reps)
    if dems < reps:
        partij = "Democraten"      
    else:
        partij = "Republikeinen"
    
    if veroveren == 1:
        print(f"De {partij} moeten minstens één zetel veroveren een meerderheid.")
    else:
        print(f"De {partij} moeten minstens {veroveren} zetels veroveren een meerderheid.")
