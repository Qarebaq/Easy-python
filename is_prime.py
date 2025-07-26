def is_prime(x):
    if x==1:
        return False
    prime =True
    for i in range(2,x):
        if x%i == 0:
            prime = False
    return prime


n = int(input("Enter the number: "))
print(is_prime(n))
