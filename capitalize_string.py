def capitalize(string):
    l = string.split(' ')
    for c in range(0, len(l)):
        l[c] = l[c].capitalize()
    return " ".join(l)
