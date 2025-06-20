# use of *args and **kwag

# when we are not sure how many data(entry) we get besides name then we use *args
def person(name, *data):
    print(name, data)


person("avin", 27, "ktm", '986585665')



# keyworded Variable Length Arguments **kwags; when we need to used key(eg 'age', 'city") too  
def person(name, **data):
    print(name)

    for i, j in data.items():
        print(i, j)


person(name="avin", age=27, city="ktm", Phno='986585665')
