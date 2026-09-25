def add(digit_a, digit_b):
    total = ""
    over = 0

    digit_a = str(digit_a)
    digit_b = str(digit_b)

    len_a = len(digit_a)
    len_b = len(digit_b)

    if len_a > len_b:
        digit_b = "0"*(len_a-len_b)+digit_b
    else:
        digit_a = "0"*(len_b-len_a)+digit_a

    for i in range(len_a):
        result = sub_one_add(digit_a[len_a-i-1], digit_b[len_a-i-1], over)

        over = result[1]
        total += str(result[0])
    
    if over != 0:
        total += str(over)

    return total[::-1]

def sub_one_add(a,b,over):
    result = [0,0]
    sum = int(a) + int(b) + int(over)
    if len(str(sum)) > 1:
        result[1] = int(str(sum)[:1])
        result[0] = int(str(sum)[1:])
    else:
        result[0] = int(sum)
    
    return result

while True:
    a = input("a: ")
    b = input("b: ")

    print(add(a,b))