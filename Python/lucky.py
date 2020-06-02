print("I'm lucky")
string="""I'm the luckiest husbund in the universe
and the worst"""
a = 15
b="ab"
print(type(b))
c=int(b,16)
print(c)
print("####",type(c))
x=b"asas"
_test_data = {"name":"akhi", "age" : 15, "name2":"vidya", "age2":15}
length = _test_data.__len__()
print(length)
print(type(_test_data))

def myfunct():
        print(_test_data.values())

myfunct()
print("The value of a is",a)
print(string)

quantity = "3X"
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

print(myorder,price)