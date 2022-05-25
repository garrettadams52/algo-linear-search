array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)

def linear_search(value_to_find, array_to_search_through):
    # your code here

    for i,x in enumerate(array_to_search_through):
        if value_to_find == x:
            return i

    return None