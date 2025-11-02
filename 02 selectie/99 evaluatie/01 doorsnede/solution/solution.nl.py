a = int(input("Geef de eerste ondergrens in: "))
c = int(input("Geef de eerste bovengrens in: "))

b = int(input("Geef de tweede ondergrens in: "))
d = int(input("Geef de tweede bovengrens in: "))

e = max(a,b)
f = min(c,d)

if e < f:
    print('De doorsnede van [',a ,',',c,'] en [', b,',',d,'] is [',e, ',',f,']')
elif e == f:
    print('De doorsnede van [',a ,',',c,'] en [', b,',',d,'] is singleton', e)
else: 
    print('De doorsnede van [',a ,',',c,'] en [', b,',',d,'] is ledig')
