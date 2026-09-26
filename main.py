def add(num_a, num_b):
    total = ""
    over = 0

    num_a = str(num_a)
    num_b = str(num_b)

    len_a = len(num_a)
    len_b = len(num_b)

    if len_a > len_b:
        num_b = "0"*(len_a-len_b)+num_b
    else:
        num_a = "0"*(len_b-len_a)+num_a
    
    nlen = len_a

    for i in range(nlen):
        result = _units_add(num_a[nlen - i - 1], num_b[nlen - i - 1], over)

        over = result[1]
        total += str(result[0])
    
    if over != 0:
        total += str(over)

    return total[::-1]

def _units_add(a,b,carry):
    result = [0,0]
    sum = int(a) + int(b) + int(carry)
    if len(str(sum)) > 1:
        result[1] = int(str(sum)[:1])
        result[0] = int(str(sum)[1:])
    else:
        result[0] = int(sum)
    
    return result

def subtract(num_a, num_b):
    return ""

while True:
    a = input("a: ")
    b = input("b: ")

    print(add(a,b))