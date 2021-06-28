def move_zeros(array):
    update_array = list(filter(lambda x: x != 0, array))
    update_array.extend([0] * array.count(0))
    return update_array

print((move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])))
