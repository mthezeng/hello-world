def tetration(value, tetronent):
    """
    >>> print(tetration(3,3)) # 3 ** 3 ** 3, or 3^(3^3)
    7625597484987
    """
    if tetronent == 1:
        return value
    else:
        return value ** tetration(value, tetronent-1)

number = int(input('Number: '))
tetronent_value = int(input('Tetronent: '))
print(tetration(number, tetronent_value))
