num = 600851475143
maximal =0
temp =0
i = 2
for i in range(2,int(num**0.5)+1):
    if num%i ==0:
        for j in range(2,i):
            if i%j == 0:
                temp = temp +1
        if temp == 0:
            maximal = i

print(maximal)
