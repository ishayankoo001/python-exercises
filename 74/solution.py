import images


def es74(filePng, center, thickness, colors, pngFileOut):
    img = images.load(filePng)
    conti = []
    for i, colore in enumerate(colors):
        radiusIn = i*thickness
        radiusOut = (i+1)*thickness
        conti.append(drawAnello(img, center, radiusIn, radiusOut, colore))
    images.save(img, pngFileOut)
    return conti


def drawRing(img, center, rIn, rOut, colore):
    count = 0
    h = len(img)
    w = len(img[0])
    cx, cy = center
    # be sure to not overflow the image margins
    minx = max(cx-rOut, 0)
    miny = max(cy-rOut, 0)
    maxx = min(cx+rOut, w)
    maxy = min(cy+rOut, h)
    # evaluate the ring pixels instead of the whole image
    for x in range(minx, maxx):
        for y in range(miny, maxy):
            d2 = (x-cx)**2 + (y-cy)**2  # square of the distance: check
            # if it is included in the area between internal and
            # external radiuses
            if rIn**2 <= d2 < rOut**2:
                img[y][x] = colore
                count += 1
    return count
