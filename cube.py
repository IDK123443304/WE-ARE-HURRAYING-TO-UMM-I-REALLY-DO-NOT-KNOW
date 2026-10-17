def cube(num):
    return num*num*num
def isdivsible(num):
    if num%5==0:
        print(cube(num))
    else:
        print(num)

num = int(input("Enter a number: "))
isdivsible(num)