def es25(n):
    '''Design and implement function es25(n), namely a recursive function
    or a function that makes use of a recursive function, which
    calculates the i-th row of the triangle of Tartaglia, that is the
    list of the i-th power coefficients of the binomial (a+b).

    The definition of the triangle of Tartaglia:
            1
           1 1
          1 2 1
         1 3 3 1
        1 4 6 4 1
       ...........
    Tartaglia(0) = [1]   # base case
    The numbers that appear in each row of the triangle of Tartaglia
    are obtained as the sum of those above, in the previous line.
    Where a value is missing, you can use the value 0 (zero).

    '''
    a = n
    b = 0
    list = []
    while(a>=0):
        list.append((choose(a,n)))
        a -= 1
        b += 1
    return list
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)
def choose(n, k):
    return (int)(factorial(k)/(factorial(n)*factorial(k-n)))
