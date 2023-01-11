def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    i = 0
    count = 0
    m = min(data)
    while i <len(data):
        if data[i] == m:
            count += 1
        i += 1

    return count

print(find_min_count([15, 23, 3, 2, 2, 4]))
