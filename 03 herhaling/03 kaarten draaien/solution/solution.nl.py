n = int(input("Geef het aantal stappen in: "))

bits = [0] * 10

i = 9
while n > 0:
    bits[i] = n % 2
    n //= 2
    i -= 1

str = ""
for i in range(len(bits)):
    bit = bits[i]
    if bit == 0:
        str += "X"
    else:
        str += "O"
    if i != len(bits) - 1:
        str += " "

print(str)
