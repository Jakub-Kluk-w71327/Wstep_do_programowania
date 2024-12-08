def max_value(*args):

    list_of_element = []

    for element in args:
        list_of_element.append(element)

    list_of_element.sort()
    
    return list_of_element[-1]


print(max_value(1,6,4,2,44,12,43,12,76,342,888,1214,0,5,123))