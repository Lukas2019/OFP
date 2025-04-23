def charFrequenz(s):
    print(s)
    s.lower()
    s = sorted(s)

    s_dict = {}
    alt_s = None
    for i in s:
        if "a"<= i <="z":
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i]=1
    count_list = []
    for key in s_dict:
        count_list.append((key, s_dict[key]))
    print(count_list)
    return count_list


charFrequenz("test")