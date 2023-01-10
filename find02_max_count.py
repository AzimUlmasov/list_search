def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    i = 0
    count = 0
    m = max(data)
    while i <len(data):
        if data[i] == m:
            count += 1
        i += 1

    return count

print(find_max_count([1, 2, 5, 3, 4, 5]))

