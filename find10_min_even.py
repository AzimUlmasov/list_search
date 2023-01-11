def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    i = 0
    even = []
    while i <len(data):
        if data[i] %2==0:
            even.append(data[i])
        i += 1
    if even:
        return min(even)
    else:
        return -1 

print(find_min_even([7, 8, 4, 3, 5]))    
