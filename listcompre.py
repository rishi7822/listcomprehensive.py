cars = ["bugatti","mercedes","bmw","audi","ferrari"]
newcars = []

for x in cars:
    if "d" in x:
        newcars.append(x)

print(newcars)

#
#through list comprehension we can do this in one line
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlis = [x for x in fruits if "a" in x]

print(newlis)

#
#x! = "mercedes" will return all elements accept mercedes


newcars = [x for x in cars if x != "mercedes"]
print(newcars)

#range() fuyn tions
welist = [x for x in range(10)]
print(welist)