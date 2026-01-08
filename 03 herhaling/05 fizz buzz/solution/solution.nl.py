n = int(input("Geef het eindgetal in: "))

for i in range(n):
    getal = i + 1
    if getal % 3 == 0 and getal % 5 == 0:
        print("FizzBuzz")
    elif getal % 3 == 0:
        print("Fizz")
    elif getal % 5 == 0:
        print("Buzz")
    else:
        print(getal)
