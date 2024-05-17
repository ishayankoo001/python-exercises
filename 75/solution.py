import images


def es75(w, h, listColors, listHeights, widthPalace, filePngOut):
    return es75_interpretation2(w, h, listColors, listHeights, widthPalace, filePngOut)


def es75_interpretation1(w, h, listColors, listHeights, widthPalace, filePngOut):
    blu = (0, 0, 255)
    img = [[blu for _ in range(w)] for _ in range(h)]
    counts = [[0 for _ in range(w)] for _ in range(h)]
    rectangles = []
    N = len(listHeights)

    # first interpretation of the words "equispaced rectangles" (= with the equispaced centers in the image)
    # the centers of the buildings are spaced regularly in the image
    step = w//(N+1)
    # BUT! if widthPalace > step then they can overflow from the image
    start = step - widthPalace//2
    end = start + widthPalace

    for color, height in zip(listColors, listHeights):
        rectangles.append((start, end, h-height, h, color))
        start += step
        end += step
    rectangles.sort(key=lambda r: r[2])
    for r in rectangles:
        drawRectangle(img, *r, counts)
    immagini.save(img, filePngOut)
    changed = 0
    for line in counts:
        for n in line:
            if n > 1:
                changed += 1
    return changed

def es75_interpretation2(w, h, listColors, listHeights, widthPalace, filePngOut):
    blu = (0, 0, 255)
    img = [[blu for _ in range(w)] for _ in range(h)]
    counts = [[0 for _ in range(w)] for _ in range(h)]
    rectangles = []
    N = len(listHeights)

    # second possible interpretation of the words "equispaced rectangles"
    # (= first and last laying on the edge, the others spaced uniformly)
    # the first and the last building are leaning to the left and to the right
    start = 0
    end = widthPalace
    # the others are spaced regularly (N-1 spaces)
    step = (w-widthPalace)//(N-1)

    for color, height in zip(listColors, listHeights):
        rectangles.append((start, end, h-height, h, color))
        start += step
        end += step
    rectangles.sort(key=lambda r: r[2])
    for r in rectangles:
        drawRectangle(img, *r, counts)
    immagini.save(img, filePngOut)
    changed = 0
    for line in counts:
        for n in line:
            if n > 1:
                changed += 1
    return changed


def drawRectangle(img, l, r, t, b, c, counts):
    # you avoid to overflow from the image
    w = len(img[0])
    h = len(img)
    l = max(l, 0)
    r = min(r, w)
    t = max(t, 0)
    b = min(b, h)
    for x in range(l, r):
        for y in range(t, b):
            img[y][x] = c
            counts[y][x] += 1
