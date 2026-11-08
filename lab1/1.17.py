def merge_dicts(d1, d2):
    for key in d2:
        if key not in d1:
            d1[key] = d2[key]
        else:
            if type(d1[key]) == dict and type(d2[key]) == dict:
                merge_dicts(d1[key], d2[key])
            elif type(d1[key]) == list and type(d2[key]) == list:
                for item in d2[key]:
                    d1[key].append(item)
            elif type(d1[key]) == tuple and type(d2[key]) == tuple:
                d1[key] = d1[key] + d2[key]
            elif type(d1[key]) == set and type(d2[key]) == set:
                for item in d2[key]:
                    d1[key].add(item)
            else:
                d1[key] = d2[key]

dicta = {"a": 1, "b": {"c": 1, "f": 4}}
dictb = {"d": 1, "b": {"c": 2, "e": 3}}
merge_dicts(dicta, dictb)
print("Результат слияния:", dicta)