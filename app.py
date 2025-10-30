def add_two_numbers(num1, num2):
    carry = 0
    place = 1
    num = 0
    while num1>0 or num2>0 or carry>0:
        d1 = num1%10
        d2 = num2%10
        num1 //= 10
        num2 //= 10
        a = d1+d2+carry
        if (a)>9:
            carry = 1
        elif (a)<=9:
            carry = 0
        num = num + ((a)%10)*place
        place *= 10
    return num
