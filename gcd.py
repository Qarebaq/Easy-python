a = 18
b = 12
gcd = b
if (a %b) ==0:
    gcd = b
    print(gcd)
else:
    while b != 0 :
        temp = b
        b = a % b
        a = temp

print(gcd)
