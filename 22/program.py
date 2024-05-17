import images
import json


def ex22(pngFile, jsonFile):
    '''Design and implement a function ex22(pngFile, jsonFile) such that:
    - it takes as arguments two path names ('pngFile' and 'jsonFile')
    - it reads and encodes the PNG image stored in the 'pngFile' and
      saves the encoded image in a JSON file, named 'jsonFile'
    - it returns the most frequent encoding string used during the
      encoding of the whole image.

    The image should be encoded in an matrix (list of lists) M of
    strings with dimensions w x h, where w is the width of the image
    and h is its height. For each pixel [i][j] of the image, the
    corresponding cell M[i][j] contains a string that encodes the
    color of that pixel: each of the three R, G and B components of
    the pixel color are encoded with a string of 3 characters,
    obtaining a string of 9 characters with their concatenation,
    keeping the R, G and B order. For example the color (0,0,0) is
    encoded as '000000000' and the color (50,10,200) as '050010200'.
    The function returns the most frequent string of the matrix, in
    case of tie, the first one in alphabetical order.

    To load and save the image in the PNG file, use the load and save
    functions of the images.py library.

    '''
    pass
