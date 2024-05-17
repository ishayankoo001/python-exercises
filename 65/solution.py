import images


def es65(k, list1, fout):
    img = [[(0, 0, 0) for _ in range(k)] for _ in range(k)]
    for q in list1:
        x, y, l, r, g, b = q
        c = maxColor(img, q)
        draw(img, x, y, l, c)
    immagini.save(img, fout)
    count = 0
    for x in range(len(img)):
        for y in range(len(img)):
            if img[x][y] == (0, 0, 0):
                count += 1
    return count


def maximum(c1, c2):
    r, g, b = c1
    r1, g1, b1 = c2
    if r > r1 or (r == r1 and g > g1) or (r == r1 and g == g1 and b >= b1):
        return c1
    return c2


def maxColor(img, q):
    side = len(img)
    x, y, l, r, g, b = q
    c = (r, g, b)
    for ny in range(y, y+l):
        for nx in range(x, x+l):
            if nx < side and ny < side:
                c = maximum(c, img[ny][nx])
    return tuple(c)


def draw(img, x, y, l, c):
    side = len(img)
    for ny in range(y, y+l):
        for nx in range(x, x+l):
            if nx < side and ny < side:
                img[ny][nx] = c
