import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, w, h, colors_list, heights_list, palace_width, filePngOut, expected, expectedPng):
        '''Test implementation
            - w                 : image width
            - h                 : image height
            - colors_list       : list of colors to apply to rectangles
            - heights_list      : list of rectangle heights
            - palace_width      : width of buildings
            - filePngOut        : PNG file where to save there image
            - expected          : expected number of pixels belonging to multiple rectangles
            - expectedPng       : expected image
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es75(
                w, h, colors_list, heights_list, palace_width, filePngOut)
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")
        self.check_img_file(filePngOut, expectedPng)

    @data(
        (1200, 500, [(20, 0, 0), (40, 0, 0), (60, 0, 0), (80, 0, 0), (100, 0, 0), (120, 0, 0), (140, 0, 0), (160, 0, 0), (180, 0, 0), (200, 0, 0), (220, 0, 0)], [
         100, 150, 220, 360, 340, 300, 100, 280, 370, 320, 200], 200, 'test.101.png', [211000], ['expected.101.png']),
        (1200, 500, [(0, 10, 0), (0, 20, 0), (0, 30, 0), (0, 40, 0), (0, 50, 0), (0, 60, 0), (0, 70, 0), (0, 80, 0), (0, 90, 0), (0, 100, 0), (0, 110, 0), (0, 120, 0), (0, 130, 0), (0, 140, 0), (0, 150, 0), (0, 160, 0), (0, 170, 0), (0, 180,
                                                                                                                                                                                                                                          0), (0, 190, 0), (0, 200, 0), (0, 210, 0)], [410, 390, 300, 240, 110, 320, 420, 280, 340, 30, 40, 80, 390, 420, 330, 500, 420, 300, 480, 350, 320], 200, 'test.102.png', [387980, 374500], ['expected.102-1.png', 'expected.102-2.png'])
    )
    @unpack
    def test(self, w, h, colors_list, heights_list, palace_width, filePngOut, expected, expectedPng):
        try:
            print("\ntrying first interpretation")
            return self.do_test(w, h, colors_list, heights_list, palace_width, filePngOut, expected[0], expectedPng[0])
        except:
            print("\ntrying second interpretation")
            return self.do_test(w, h, colors_list, heights_list, palace_width, filePngOut, expected[1], expectedPng[1])


# Tests are performed both executing program.py and calling  pytest in the directory
if __name__ == '__main__':
    Test.main()
