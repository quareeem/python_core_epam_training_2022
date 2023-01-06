def get_fractions(a_b: str, c_b: str) -> str:
    temp_a = a_b.split('/')
    temp_b = c_b.split('/')
    numer = int(temp_a[0]) + int(temp_b[0])

    return f'{a_b} + {c_b} = {numer}/{temp_a[1]}'
