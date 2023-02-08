def min_max(data):
    minimum = data[0]
    maximum = data[0]
    for i in data[1:]:
        if i < minimum:
            minimum = i 
        elif i > maximum:
            maximum = i
    return (minimum,maximum)
