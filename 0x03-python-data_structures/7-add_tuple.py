def add_tuple(tuple_a=(), tuple_b=()):
    
    tuple_a = tuple_a + (0, 0) if len(tuple_a) < 2 else tuple_a[:2]
    tuple_b = tuple_b + (0, 0) if len(tuple_b) < 2 else tuple_b[:2]
    new_tuple = tuple(x + y for x, y in zip(tuple_a, tuple_b))

    return new_tuple
