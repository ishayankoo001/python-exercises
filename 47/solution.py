def es47(string_list):
    return sorted(set(string_list), key=lambda x: (-len(x), x), reverse=True)
