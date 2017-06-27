list_a = [67,45,2,13,1,998]
for index in range(1, len(list_a)):
    value = list_a[index]
    i = index - 1
    while i >= 0:
        if value > list[i]:
            list[i+1] = list[i]
            list [i] =value
            i = i - 1
        else:
            break   

