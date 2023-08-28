# List : list is a collection of multipal data
# []

# list : ordedred, allow duplicasy, mutable (changes)





# Tuple : collection of multipla data....
# ()
# tuple :  ordered, allow duplicasy, imutable

# tpl = (12, 100, "hlo", 120.8, 100, 100)
# print(tpl)
# print(tpl, type(tpl))

# print(tpl[3])

# tpl.insert(1, 1200)

# print(tpl)



# # type casting  

# a = 10
# print(a, type(a))

# tpl = (12, 100, "hlo", 120.8, 100, 100)
# print(tpl)
# print(type(tpl))

# lst = list(tpl)
# print(lst)
# print(type(lst))

# lst.append(1200)

# print(lst)

# tl = tuple(lst)

# print(tl)
# print(type(tl))








# Set : its also a collcetion of multipal data
# {}

# set : unordered, do not allow duplicasty, mutable


# st = {12, 100, "hlo", "ok", 100, "hlo", 90, 50, 12}

# print(st)
# print(type(st))

# adding new data

# st.add(1200)

# st.pop()

# st.remove(12)

# print(st)






# dictionry : 
# {}
# key : value pairs 

# dict : ordered, do not allow duplicasy, mutable


# dictty = {
#     "name" : "moris",
#     "age" : 20,
#     "gender" : "male"
# }


# print(dictty)
# print(type(dictty))

# print(dictty['name'])



# print(dictty.keys())
# print(dictty.values())

# dictty = {
#     "name" : "moris",
#     "age" : 20,
#     "gender" : "male"
# }

# dictty["marks"] = 90

# dictty.pop("age")

# print(dictty)


lst = ["name", "age", "gender", "address"]

tpl = ("kriss", 20, "male", "this is address")



output:
{"name" : "kriss", "age" : 20, "gender" : "male", "address" : "this is address"}














solution


lst = ["name", "age", "gender", "address", "marks"]

tpl = ("kriss", 20, "male", "this is address", 90)

dict = {}

for i in range(5):
    # key = lst[i]
    # vl = tpl[i]
    
    # dict[key] = vl

    dict[lst[i]] = tpl[i]

print(dict)
    



# output:
# {"name" : "kriss", "age" : 20, "gender" : "male", "address" : "this is address"}

# dictin = {}

# dictin["name"] = "this is name"  
# dictin["age"] = 20
# print(dictin)
    
    
    
    
    





question ::::::::::::::::::::::


lst = ["name", "age", "gender", "address", "marks"]

tpl = ("kriss", 20, "male", "this is address", 90)



output :

{"name" : "kriss", "age" : 20, "gender" : "male", "marks" : 90}







