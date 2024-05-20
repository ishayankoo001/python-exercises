import images


def ex15(fimm1, fimm2, fimm3):
    '''Design a function ex15(fimm1,fimm2,fimm3) such that:
    - it receives as arguments three filenames of .PNG files. The
      files 'fimm1' and 'fimm2' store two images WITH DIFFERENT
      DIMENSIONS
    - it creates a third image and saves it in a .PNG file with name
      'fimm3'
    - it returns the number of black pixels in the created image.
    The third image is obtained from the first two. Its width is the
    maximum width between the widths of fimm1 and fimm2 and its height
    is the maximum height between the heights of fimm1 and fimm2.
    Each pixel [y][x] of the third image will be:
    - of black color (0,0,0) if a pixel [y][x] exists in both or none
      of the first two images
    - of the same color of the pixel in the only image where such a
      pixel exists.
    
    To load and save the image in PNG files, use the load and save
    functions of the images.py library.

    '''
    fimm1 = images.load(fimm1)
    fimm2 = images.load(fimm2)
    fimm1_height, fimm1_width = (len(fimm1), len(fimm1[0]))
    fimm2_height, fimm2_width = (len(fimm2), len(fimm2[0]))
    imm3_height, imm3_width = (max(fimm1_height, fimm2_height), max(fimm2_width, fimm1_width))
    minw, minh = (min(fimm1_width, fimm2_width), min(fimm1_height, fimm2_height))
    height_source = fimm1 if fimm1_height == imm3_height else fimm2
    width_source = fimm1 if fimm1_width == imm3_width else fimm2
    imm3 = [[(0, 0, 0) for x in range(imm3_width)] for x in range(imm3_height)]
    for h in range(minh, imm3_height):
        for w in range(len(height_source[0])):
            print(h, w)
            imm3[h][w] = height_source[h][w]
    for h in range(len(width_source)):
        for w in range(minw, imm3_width):
            imm3[h][w] = width_source[h][w]
    images.save(imm3, fimm3)
    count = 0
    for i in range(imm3_height):
        for j in range(imm3_width):
            if imm3[i][j] == (0, 0, 0):
                count += 1
    return count


ex15("foto1.png", "foto2.png", "testt.png")
