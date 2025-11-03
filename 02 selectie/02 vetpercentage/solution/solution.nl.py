ab = float(input("Geef de buikhuidplooi in (in mm): "))
th = float(input("Geef de huidplooi van het bovenbeen in (in mm): "))
age = float(input("Geef de leeftijd in: "))

BD = 1.08543 - (0.000886 * ab) - (0.0004 * th )
BF = 4.95 / BD - 4.50

if 20 <= age <= 39:
    print( 'Het vetpercentage bedraagt', round(BF * 100, 2), '%.')
    if BF < 0.08:
        print('Dit vetpercentage is te laag.')
    elif BF > 0.19:
        print('Dit vetpercentage is te hoog.')
    else:
        print('Dit is een gezond vetpercentage.')
elif 40 <= age <= 59:
    print('Het vetpercentage bedraagt', round(BF * 100, 2), '%.')
    if BF < 0.11:
        print('Dit vetpercentage is te laag.')
    elif BF > 0.21:
        print('Dit vetpercentage is te hoog.')
    else:
        print('Dit is een gezond vetpercentage.')
elif 60 <= age <= 79:
    print('Het vetpercentage bedraagt', round(BF * 100, 2), '%.')
    if BF < 0.13:
        print('Dit vetpercentage is te laag.')
    elif BF > 0.24:
        print('Dit vetpercentage is te hoog.')
    else:
        print('Dit is een gezond vetpercentage.')
else:
    print('Er zijn betere methodes om het vetpercentage van deze persoon te berekenen.')
