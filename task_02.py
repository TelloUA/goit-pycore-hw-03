import random

def get_numbers_ticket(min, max, quantity) -> list:
    # validate input data
    if min < 1:
        return []
    if max > 1000:
        return []
    # check if function can find enough unique numbers
    if (max - min + 1) < quantity:
        return []
    
    result = set()
    while len(result) < quantity:
        number = random.randint(min, max)
        result.add(number)

    # change type to list for sorting
    for_sort = list(result)
    for_sort.sort()
    return for_sort

numbers = get_numbers_ticket(1, 36, 5)
print(numbers)
