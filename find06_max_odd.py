def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i = 0
    odd = []
    # m = max(data)
    while i <len(data):
        if data[i] %2==1:
            odd.append(data[i])
        i += 1
    if odd:
        return max(odd)
    else:
        return -1 

print(find_max_odd([1, 8, 3, 8, 5]))    