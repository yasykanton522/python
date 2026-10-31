def flatten(lst, start=0):
    i = start
    while i < len(lst):
        if type(lst[i]) == list:
            temp = lst[i]
            lst.pop(i)
            for j in range(len(temp) - 1, -1, -1):
                lst.insert(i, temp[j])
            flatten(lst, i)
        i += 1