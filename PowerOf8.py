num = int(input("Enter a number: "))

def checkPowerOf8(num):
    if (num == 0):
        return False
    while (num != 1):
            if (num % 8 != 0):
                return False
            num = num // 8
            
    return True


print(checkPowerOf8(num))