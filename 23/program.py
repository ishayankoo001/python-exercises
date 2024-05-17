import images
import json


def es23(fileJson, filePng):
    '''We have a json type file containing a matrix (list of lists) M
    whose elements are strings. The matrix encodes an image.  The
    image has width w and height h, where w is the number of columns
    of the matrix M and h is the number of rows.  The color (r,g,b) of
    the x,y coordinate pixel is encoded with the string in M[y][x],
    since the string is composed by 9 digits.  The three most
    significant digits are the encoding of the r-component, the three
    middle ones are the encoding of the g-component and the three less
    significant the encoding of the b-encoding.
    Design and implement the function es23(fileJson, filePng) that
    reads the json file and produces a new PNG file with the image
    decoded by the json file. The function returns, also, the color
    that appears most often in the image. In case of tie, the color
    that precedes the others with respect to the order of the color
    components is returned.
    The function takes as arguments:
        :param fileJson: the path of the json file where the matrix of
                         the encoded image is located
        :param filePng:  the path of the PNG file where to save the
                         decoded image
        :return: the color that appears most often among those of the
                 pixels of the image

    '''
    pass
