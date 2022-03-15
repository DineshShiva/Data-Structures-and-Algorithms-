# reverse string without use of reverse function

def reverseStr(value):
    lengthOfValue = len(value)-1
    backward=[]
    for i in range(lengthOfValue,-1,-1):
        backward.append(value[i])
    return ''.join(backward)


# reverse string with reverse function

def reverseStr2(value):
    return value[::-1]

print(reverseStr2('Dineshkumar'))
