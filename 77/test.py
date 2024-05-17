import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, word, expected):
        '''Implementation of the test
            - word : string of chars
            - expected : suffix list 
        '''
        par2 = copy.deepcopy(word)
        try:
            isrecursive.decorate_module(program)
            program.es77(par2)
        except isrecursive.RecursionDetectedError:
            raise Exception("Recursion detected.")
        finally:
            isrecursive.undecorate_module(program)

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es77(word)
        self.assertEqual(type(result), list, "The result is not a list")
        self.assertEqual(
            result, expected, f"The result should be {expected} instead of {result}")

    @data(
        ("fondamenti", ['i', 'ti', 'nti', 'enti', 'menti', 'amenti',
                        'damenti', 'ndamenti', 'ondamenti', 'fondamenti']),
        ('supercalifragilistichespiralidoso', ['o', 'so', 'oso', 'doso', 'idoso', 'lidoso', 'alidoso', 'ralidoso', 'iralidoso', 'piralidoso', 'spiralidoso', 'espiralidoso', 'hespiralidoso', 'chespiralidoso', 'ichespiralidoso', 'tichespiralidoso', 'stichespiralidoso', 'istichespiralidoso', 'listichespiralidoso', 'ilistichespiralidoso', 'gilistichespiralidoso', 'agilistichespiralidoso',
                                               'ragilistichespiralidoso', 'fragilistichespiralidoso', 'ifragilistichespiralidoso', 'lifragilistichespiralidoso', 'alifragilistichespiralidoso', 'califragilistichespiralidoso', 'rcalifragilistichespiralidoso', 'ercalifragilistichespiralidoso', 'percalifragilistichespiralidoso', 'upercalifragilistichespiralidoso', 'supercalifragilistichespiralidoso']),
        ('3gne.nm/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', ['n', '*n', '§*n', '#§*n', '"#§*n', '$"#§*n', 't$"#§*n', 'tt$"#§*n', '4tt$"#§*n', 'n4tt$"#§*n', '2n4tt$"#§*n', 'o2n4tt$"#§*n', '7o2n4tt$"#§*n', 'n7o2n4tt$"#§*n', '3n7o2n4tt$"#§*n', '53n7o2n4tt$"#§*n', '.53n7o2n4tt$"#§*n', 'y.53n7o2n4tt$"#§*n', ',y.53n7o2n4tt$"#§*n', '3,y.53n7o2n4tt$"#§*n', '-3,y.53n7o2n4tt$"#§*n', '.-3,y.53n7o2n4tt$"#§*n', '2.-3,y.53n7o2n4tt$"#§*n', 'y2.-3,y.53n7o2n4tt$"#§*n', 'ny2.-3,y.53n7o2n4tt$"#§*n', '4ny2.-3,y.53n7o2n4tt$"#§*n', '34ny2.-3,y.53n7o2n4tt$"#§*n', 'g34ny2.-3,y.53n7o2n4tt$"#§*n', '=g34ny2.-3,y.53n7o2n4tt$"#§*n', '!=g34ny2.-3,y.53n7o2n4tt$"#§*n',
                                                           '&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', 'm/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', 'nm/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '.nm/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', 'e.nm/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', 'ne.nm/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', 'gne.nm/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '3gne.nm/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n'])
    )
    @unpack
    def test(self, word, expected):
        return self.do_test(word, expected)


# TESTS ARE TO BE PERFORMED IF YOU PERFORM program.py or by calling pytest in the directory
if __name__ == '__main__':
    Test.main()
