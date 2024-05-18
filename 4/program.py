import images


def most_frequent_color(image):
    a = image
    dict = {}
    height = len(a)
    width = len(a[0])
    for i in a:
        for j in i:
            if j in dict:
                dict[j] += 1
            else:
                dict[j] = 1
    dict = sorted(dict.items(), key=lambda x:-x[1])
    return (dict[0][0])
def changePixels(image, fh, th, fw, tw, s):
    for h in range(fh, th):
        for w in range(fw,tw):
            try:
                image[h][w]=s
            except IndexError:
                print(h,w)
    return image
def ex4(fimm1, fimm2, h1, w1):
    '''Design a function ex4(fimm1,fimm2) such that:
    - it receives as arguments two filenames 'fimm1' and 'fimm2',
      where 'fimm1' is a file with an .PNG image, and two integers
      'h1' and 'w1', both greater than zero;
    - it reads the image in 'fimm1' and creates a new image that
      saves as a PNG image in the 'fimm2' file;
    - it returns a tuple with the color that appears most often in the
      original image and, in case of tie, the one that precedes the
      others in ascending order.
    The new image has h1 times the height of the original image and w1
    times the width of the original image. Each pixel of the original
    image corresponds in the new image to a rectangle of pixels with
    the same color and with height h1 and width w1.

    To load and save the image in PNG files, use the load and save
    functions of the images.py library.

    '''
    fimm1 = images.load(fimm1)
    height_original = len(fimm1)
    print(height_original)
    width_original = len(fimm1[0])
    print(width_original)
    height_new = h1*height_original
    width_new = w1*width_original
    #write here your code
    new_image = [[(0,0,0) for i in range(width_new)] for j in range(height_new)]
    print(len(new_image[0]))
    print(len(fimm1[0]))
    for h, val in enumerate(fimm1):
        for pixel,val2 in enumerate(val):
            changePixels(new_image,fh=h*h1,th=h1*(h+1),fw=pixel*w1,tw=w1*(pixel+1),s=val2)
    images.save(new_image, fimm2)
    return (most_frequent_color(fimm1))


# ex4(fimm1="fotoBN.png", fimm2="test.png",h1=2,w1=3)
cb = images.load("cubo.png")
print(most_frequent_color(cb))

