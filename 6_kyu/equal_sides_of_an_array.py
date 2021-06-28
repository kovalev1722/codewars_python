def find_even_index(arr):
    #print(sum(arr))
    for index, number in enumerate(arr):
        if sum(arr[:index]) == sum(arr[index+1:]):
            return(index)
    return -1

print(find_even_index([1,2,3,4,3,2,1]))