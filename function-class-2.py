# function : 

# 1) *args
# 2) **kwargs

# def xv(a,b):
#     b= a+b
#     print(b)
# xv(12,34)

# def addthis(*args):
#     z = 0
#     for i in args:
#         z = z + i
#     print(z)
    

# addthis(12, 100, 100, 20, 1)


# def saveinfo(**kwargs):
#     print(kwargs)
    
# saveinfo(name="moris", age = 20)


# 1) lambda
# 2) map()
# 3) filter()
# 4) reduce ()

# def xuz(a, b):
#     c = a + b
#     print(c)

# xuz(12, 10)


# lambda function 

# lambda arguments : expression


# zx = lambda a, b : a + b

# print(zx(100, 200))
# print(zx(12, 50))


# map()

# lst = [1, 2, 3, 4, 5, 6, 7]

# # map(function, itreater)

# zx = map(lambda x : x * 10, lst)

# print(list(zx))


# filter() :

# lst = [12, 10, 11, 67, 90, 56, 101]

# we = filter(lambda x : x == 67 or x == 11, lst)

# print(list(we))


# reduce()

# from functools import reduce

# # reduce(function, itreter)

# a = [12, 2, 10, 90, 19, 1]

# sd = reduce(lambda x, y : x + y, a)

# print(sd)


