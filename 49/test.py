import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, img1, img2, img3, expected, expectedImg):
        '''Test implementation
            - img1 : first image file
            - img2 : second image file
            - img3 : where to save the new image
            - expected : pixel number expected
            - expectedJSON : picture expected
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.ex49(img1, img2, img3)
        self.assertEqual(result, expected, f"Il risultato deve essere {expected} invece che {result}/The returned values should be {expected} instead of {result}")
        self.check_img_file(img3, expectedImg)


    @data(
        ('foto1.png','foto2.png','test1.png', 30003, 'RisTest1.png'),
        ('foto1.png','foto3.png','test2.png', 2573, 'RisTest2.png'),
        ('foto3.png','foto1.png','test3.png', 2630, 'RisTest3.png')
    )
    @unpack
    def test(self, img1, img2, img3, expected, expectedImg):
        return self.do_test(img1, img2, img3, expected, expectedImg)


# The tests can be performed running program.py or calling pytest in the directory
if __name__ == '__main__':
    Test.main()
