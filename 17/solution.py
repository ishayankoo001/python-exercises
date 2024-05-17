def es17(ls, k):
    result = 0
    indexes = []
    for word in ls:
        word_low = word.lower()
        car_count = dict()
        for c in word_low:
            if(c not in car_count):
                car_count[c] = 1
            else:
                car_count[c] += 1
        for value in car_count.values():
            if(value >= k):
                indexes.append(ls.index(word))
                result += 1
                break
    for i in range(0, len(indexes)):
        ls.remove(ls[indexes[i]-i])
    return result
