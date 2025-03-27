



def is_Palindrome(num):
    temp1 = int(num)
    temp = int(num) 
    n = 0
    Check = 0 
    while num> 0:
        num = num // 10
        n = n + 1
    arr = [0] * n
    arrtst = [0] * n
    for i in range(0,n):
        arr[i]  = temp %10 
        temp = int(temp // 10)
    for j in range(n-1,-1,-1):
        arrtst[j] = temp1 % 10
        temp1 = int(temp1 // 10)
    for i in range(0,n):
        if (arr[i] == arrtst[i]):
            Check = Check + 1
    
    if (Check == n):
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")
    

num = int(input("Enter a number: "))
is_Palindrome(num)

