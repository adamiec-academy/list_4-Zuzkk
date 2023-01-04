def info(data):
    for row in data:
        for element in row:
            print(element, end="")
        print()


def border_map(a, b):
    return [a * ['X']] + [['X'] + (a - 2) * ['.'] + ['X'] for _ in range(1, b-1)] + [a * ['X']]
