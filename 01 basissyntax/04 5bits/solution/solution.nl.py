binair = int( input( 'Geef de getal in (van 5 bits): ' ) )

TD = binair // 10000
TD_rest = binair % 10000

D = TD_rest // 1000
D_rest = TD_rest % 1000

H = D_rest // 100
H_rest = D_rest % 100

T = H_rest // 10
T_rest = H_rest % 10

E = T_rest

getal = TD * pow( 2, 4 ) + D * pow( 2, 3 ) + H * pow( 2, 2 ) + T * 2 + E

print('Dit is', getal,'in het decimale talstelsel')
