import images


def calc_dist(i, j, center, times, thickness):
    x = abs(i - center[0])
    y = abs(j - center[1])
    length = ((x ** 2 + y ** 2) ** 0.5)
    if (length < thickness * (times + 1)):
        return True
    return False
def es74(filePng, center, thickness, colors, pngFileOut):
    """Design and implement the function
    es74(filePng, center, thickness, colors, pngFileOut) that, given a
    png image, draws a target (namely a series of colored rings) on it
    and saves the image in a second PNG file.  The function returns a
    list containing the number of pixels colored of each color, in
    order.
Note: to avoid rounding errors, do not calculate the distance of a
      pixel from the center with the square root, but compare the sum
      of the square of the sides with the square of the radius of the
      current circle (in short, use Pythagora's theorem).
Note: for each ring the pixels on the inner edge must be included (use
      the >= comparison) while those on the outer edge must be
      excluded (use the < comparison)
The parameters are the following:
      filePng:  the pathname of the PNG file containing the image to modify
      center: a pair (x, y) indicating the coordinates of the center
              of the target
      thickness: thickness of the rings
      colors: list of colors to be applied in order from the center to
              the outermost ring 
      return: list with the number of pixels colored of each color

    """


    img = images.load(filePng)
    s = [0 for i in range(len(colors))]
    print(len(s))
    print(len(colors))
    for j in range(len(img)):
        for i in range(len(img[0])):
            for k in range(len(colors)-1,-1,-1):
                if calc_dist(i,j,center,k, thickness):
                    img[j][i] = colors[k]
                    s[k] += 1
    images.save(img,pngFileOut)
    for i in range(len(s)-1,-1,-1):
         if i!=0:
             s[i] -= s[i-1]

    return s
