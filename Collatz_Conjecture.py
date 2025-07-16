
num = int(input("Enter that thing: "))

def is_even(num):
    if num%2 == 0:
        return 0
    else:
        return 1
    
def calculate(num):
    print(num) 
    if is_even(num) == 0:
        num = num // 2
        if num != 1:
            calculate(num)
        else:
            print(1)
    else:
        num = (num * 3) + 1
        if num != 1:
            calculate(num)
        else:
            print(1)        

calculate(num)


