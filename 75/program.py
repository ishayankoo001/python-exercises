import images


def es75(w, h, colors_list, heights_list, palace_width, filePngOut):
    """Define the function es75 that takes as input
        h:                  image height
        w:                  image width
        colors_list:         a list of N colors in the format (R, G, B) that must be applied, in the order from left to right, to the rectangles
        heights_list:       a list of N heights < h
        palace_width:       the width of each of the rectangles to draw
        filePngOut:         PNG file path to save the image in
        :return             number of pixels changed more than 1 time
    and that creates an image with size w*h pixel, with a blue
    background (0,0,255).  On the image, the function has to draw N
    rectangles, equally spaced, and all with the same width,
    palace_width. The rectangles have to be drawn starting from the
    bottom of the image.  The height and color of the i-th rectangle
    (from left to right) is given by the i-th element of colors_list
    and heights_list, respectively.  Rectangles must be drawn so that
    the lower rectangles remain in the foreground over the higher
    rectangles.  The function has to return the number of pixels that
    belong to more than one rectangle (i.e. those of rectangles that
    have been covered by at least one other rectangle).

    Note: assume that the width w of the image is always a multiple of (1+N),
            so that the center of the x position of each building is an integer value
    Note: assume that palace_width is an even value
    Note: assume that all heights are less than or equal to the height h of the image

    """
    #insert here your code
