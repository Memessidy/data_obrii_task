a = [{6, 'A'}, (5, 'R'), {2: 'O'}, {1: 'C'}, [3, 'N'],
     {'hah,trick': {4: 'G'}}
    , 7, 'T', 8, 'U', 9, 'L', 10, 'A', {15: 'S'}, {14: 'N'},
     {11: 'T'}, {12: 'I'}]

result_items = []
next_iteration = True
index, value = None, None

for i, item in enumerate(a):
    if not next_iteration:
        next_iteration = True
        continue

    elif isinstance(item, int):
        index = item
        value = a[i + 1]
        next_iteration = False

    elif any((isinstance(item, set), isinstance(item, list), isinstance(item, tuple))):
        index, value = item

    elif isinstance(item, dict):
        index, value = list(item.items())[0]
        if isinstance(value, dict):
            index, value = list(value.items())[0]

    if not isinstance(index, int):
        index, value = int(value), index

    result_items.append((index, value))


result_items.sort(key=lambda x: x[0])
print(''.join(map(lambda x: x[1], result_items)))
