# List : ordered, allow duplicatcy, mutabale

# Tuple : collecton of multipal data
# ()

# ordered, allow duplicasy, imutable

# tpl = (12, "hlo", 12.8, 90, 100)

# print(tpl)
# print(type(tpl))

# print(tpl[2])
# print(tpl[2 : 4])


# Type casting : 

# a = 10
# print(a, type(a))

# b = str(a)
# print(b, type(b))

# c = float(a)
# print(c, type(c))

# list()
# tuple()
# set()
# dict()

# tpl = (12, 3, 100, 50)
# lt = list(tpl)

# print(lt)


# tpl = (12, 20, 100, 30, 90)
# print(tpl)
# # tpl.insert(1, 2000)
# lst = list(tpl)
# print(lst)

# lst.append(2000)

# print(lst)

# tpl = tuple(lst)

# print(tpl)


# set : collection of multipal data
# {}
# unordered, do not allow duplicasy, mutable

# st = {100, 20, "hlo", 50, 100, 90}
# print(st)
# print(type(st))

# st.add(2000)

# st.pop()
# st.remove(100)
# print(st)


# Dictionry : ordered, mutable, do not allow duplicasy
# {key : value, key : value}
#   paries



# dic = {"name" : "moris",
#         "age" : 20, 
#         "marks": 100
#     }
# print(dic)
# print(type(dic))

# print(dic['name'])

# print(dic.keys())

# print(dic.values())
# dic = {"name" : "moris",
#         "age" : 20, 
#         "marks": 100
#     }
    
# dic['phone_number'] = 982381623  
# dic["address"] = "mohali"
    

# # dic.remove('name').
# dic.pop('name')
# print(dic)



dic = {
    "name" : {
        "first_name" : "kriss",
        "second_name" : "moris"
    },
    "age" : 20
}

# print(dic)

print(dic['name']["second_name"])





