def add(*args):
    """Adds up the number of arguments entered.

    Args:
        A random number of arguments.

    Returns:
        Sum of the total number of arguments entered.
    """
    print(type(args))
    print(args)

    total = 0
    for i in args:
        total += i
    return total


total2 = add(4, 5, 6, 3, 2, 1, 3, 4, 5)
print(total2)
