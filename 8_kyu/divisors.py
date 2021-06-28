def divisors(n):
    array = list()
    for counter in range(2, n):
        if n % counter == 0:
            array.append(counter)
    if  not array:
        return(str(n, "is prime"))
    return array

divisors(5)