def tickets(people):
    vasya_dollars = []
    for pay in people:
        if pay == 25: 
            vasya_dollars.append(pay)
        else:
            for change in vasya_dollars[::-1]:
                while pay - 25 > change:
                    pass
        vasya_dollars.sort()

    return vasya_dollars

#print(tickets([25, 25, 50]))
print(list(range(1,100)))