num = int(input("Enter a number: "))

def checkPowerOf4(num):
    if (num == 0):
        return False
    while (num != 1):
            if (num % 4 != 0):
                return False
            num = num // 4
            
    return True


print(checkPowerOf4(num))