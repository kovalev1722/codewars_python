def unique_in_order(iterable):
    if iterable:
        unique_list = list()
        for index in range(len(iterable) - 1):
            if iterable[index] == iterable[index + 1]:
                continue
            else:
                unique_list.append(iterable[index])
        unique_list.append(iterable[-1])
        return unique_list
    else:
        return []
        
print(unique_in_order('AAAABBBCCDAABBB'))