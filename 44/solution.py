def es44(a, b):
    integers = set()
    n = 2
    while len(integers) < a:
        ndiv = 0
        for i in range(1, n + 1):
            if n % i == 0:
                ndiv += 1
            if ndiv > b:
                break
        if ndiv != b:
            n += 1
            continue
        else:
            integers.add(n)
        n += 1
    return integers