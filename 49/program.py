

import images
def ex49(fimm1,fimm2,fimm3):
    '''Design and implement a function ex49(fimm1,fimm2,fimm3) such that
    - it receives as arguments the addresses of three .PNG file names,
      two to be read (fimm1 and fimm2) and one (fimm3) to be created
    - it reads the two images and creates a third image to be saved in fimm3
    - it returns the number of pixels of the created image for which
      the sum of the three color coordinates is an odd number
    The third image is obtained from the first two. It has minimum
    width between the widths of fimm1 and fimm2 and the minimum height
    between fimm1 and fimm2 heights.
    For each i and j, if i and j are both even or odd numbers, then
    the pixel [i][j] of the new image has the same color of the
    corresponding pixel of the fimm1 image; otherwise, it has the same
    color of the corresponding pixel of the fimm2 image.
    For loading and saving PNG files, you can use the load and save
    functions of the images library.

    '''
    # insert your code here

