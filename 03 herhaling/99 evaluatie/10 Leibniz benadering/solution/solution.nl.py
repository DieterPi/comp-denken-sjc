aantal = int(input("Geef het aantal termen in: "))

som = 0
for i in range( aantal ):
    som += (-1)**(i) / ( 2*i +1)
benadering = 4 * som

if aantal != 1:
    print(f"De benadering met {aantal} termen bedraagt {round(benadering, 9)}")
else:
    print(f"De benadering met 1 term bedraagt ongeveer {round(benadering, 9)}")
