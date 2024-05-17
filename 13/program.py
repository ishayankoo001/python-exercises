

import images
def ex13(fimm,fimm1):
    # first = images.load("Foto2.png")
    # modified = images.load("RisFoto2.png")
    # lengthy = len(first) * len(first[0])
    # guess = sorted(first)
    # lengthy2 = len(modified) * len(modified[0])
    # print(lengthy)
    # print(first[0][0])
    # print(modified[0][0])
    # print(guess[0][0])
    # print(first[0][0:51])
    # print(modified[0][0:51])
    '''Design a function ex13(fimm1,fimm2) such that,
        - it receives as argument path names of two .PNG files ('fimm1'
          and 'fimm2')
        - it reads and modifies the image stored in 'fimm1' and then saves
          the new image into 'fimm2' file
        - it returns the number of DIFFERENT colors present in the
          modified image.
        The color of each pixel of the original image is modified with the
        following procedure:
        - the tuples of the DIFFERENT colors in the first image are
          ordered in ascending order
        - the ordered sequence of tuples is, then, divided into ordered
          groups of 50 (if the total number of tuples is not a multiple of
          50, then the last group will have less than 50 elements)
        - all the colors in a given group will be modified with the first
          color of the group.
        This implies that the pixels with colors belonging to the same
        group will alll have the same color, corresponding to the first
        color of the group.

        Example: the function should transform the image of Foto2.png into
        the image of RisFoto2.png and return the value 4.

        To load and save the image in PNG files, use the load and save
        functions of the images.py library.

    '''
    # insert your code here
    img = images.load("Foto2.png")
    img = sorted(img)
    count = 0
    pixels = []
    for i, row in enumerate(img):
        for j, pixel in enumerate(row):
            if count % 50 == 0:
                newColor = pixel
            img[i][j] = newColor
            count += 1
            if pixel not in pixels:
                pixels.append(pixel)
    images.save(img, "test.png")
    return len(pixels)

print(ex13(3,3))

