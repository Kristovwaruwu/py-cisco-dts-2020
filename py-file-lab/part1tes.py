print("a","b","c",sep="sep")
#out: asepbsepc


def fun(a, b):
    return b ** 2

print(fun(b=2, 2))

#out: Error

lst = [[x for x in range(3)]for y in range(3)]
print (lst)

for r in range(3):
    for c in range (3):
        if lst[r][c] % 2 != 0:
            print("#")
# out: # # #


lst = [i for i in range(-1, -2)]
print (lst)

#out: [] zero


def fun (x,y):
    if x  == y:
        return x
    else:
        return fun (x, y-1)

print (fun(0,3))

#out : 0


x = 3
y =2

x = x % y
print (x)
x = x % y
print (x)
y = y % x
print(y)

#out = 0

lst = [x * x for x in range(5)]
print(lst)
def fun (lst):
    del lst[lst[2]]
    return lst

print(fun(lst))

#out : [0, 1, 4, 9, 16]


dd ={"1":"0", "0":1}
for x in dd.vals():
    print(x, end="")
#out : 'dict' object has no attribute 'vals'