import images

def es65(k, list1, fout):
    '''A square on the plane is identified by the 6-tuple of integers
    (x,y,l,r,g,b) where (x,y) is the coordinate of the top left vertex
    of the square, l is the length of its side and the last three
    values are its color (r,g,b).  The function es65(k, list1, fout)
    saves a squared image of side k*k in a PNG file at the path
    fout. The image is obtained as follows:
    - create a black background (0,0,0) of size k by k
    - draw in sequence the squares listed in the list1.
    The squares listed in list1 can be fully or partially in the k by
    k image.  The color of the squares is not always the original
    color, but it is determined according to this rule:
    - it is the original color, if none of the pixels on which the
    square is drawn has a greater color,
    - it is the maximum color among the pixels over which it is drawn,
    otherwise.
    A color(x,y,z) is greater than another (x',y',z') if x>x' or, in
    case of a tie, y>y' or, in case of a tie, z>z'.  The function
    returns the number of black pixels appearing in the image after
    the squares have been drawn.

    For example if
    list1=[(20,50,20,0,255,0),(30,60,20,255,0,0),(60,50,20,255,0,0),(70,60,20,0,255,0)]
    with es65(100,list1,'prova1.png') you will obtain the image in the prova1.png file
    and the function will  return the value 8600.
    '''
    # insert here your code
    
