dag = int(input("Geef de dag in: "))
maand = int(input("Geef de maand in: "))
jaar = int(input("Geef het jaar in: "))

if dag == 31 and maand == 12:
    dag = 1
    maand = 1
    jaar += 1
elif maand == 2 and dag == 28:
    dag = 1
    maand = 3
elif (maand == 4 or maand == 6 or maand == 9 or maand == 11) and dag == 30:
    dag = 1
    maand += 1
elif (maand == 1 or maand == 3 or maand == 5 or maand == 7 or maand == 8 or maand == 10) and dag == 31:
    dag = 1
    maand += 1
else:
    dag += 1

print()
print("Morgen is het", dag, "/", maand, "/", jaar)
