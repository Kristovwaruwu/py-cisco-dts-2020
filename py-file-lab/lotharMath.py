print("this is collatz prove test")
c0 = int(input("Input any number bigger than 1 : "))
steps = 0
while  c0 != 1:
    if c0 < 1:
        c0 = int(input("Input any number bigger than 1 : "))
    elif c0 % 2 == 0:
        c0 = c0 // 2
        print(str(c0))
        steps += 1
    else:
        c0 = c0 * 3 + 1
        print (c0)
        steps += 1
print("Steps : ", steps)    