import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, f1, f2, expected, expectedQuad):
        '''Test implementation
            - f1 : JSON file containing the Latin square in the form of a list of lists
            - f2 : JSON file to create
            - expected : set of symbols expected
            - expectedQuad : square expected
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.ex34(f1, f2)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}/The result should be {expected} instead of {result}")
        with open(f2, encoding='utf8') as f:
            scacchiera = json.load(f)
        self.assertEqual(
            scacchiera, expectedQuad, f"Il quadrato deve essere {expectedQuad} invece che {scacchiera}/The completed Latin square should be {expectedQuad} instead of {scacchiera}")

    @data(
        ('file3.json', 'risposta5.json', {'X', '1', '?'}, [
         ['X', '1', '?'], ['?', 'X', '1'], ['1', '?', 'X']]),
        ('file4.json', 'risposta6.json', {'a', 'b', '!', '1', '='}, [['a', 'b', '!', '1', '='], [
         '1', 'a', '=', '!', 'b'], ['!', '1', 'b', '=', 'a'], ['=', '!', 'a', 'b', '1'], ['b', '=', '1', 'a', '!']])
    )
    @unpack
    def test(self, f1, f2, expected, expectedQuad):
        return self.do_test(f1, f2, expected, expectedQuad)


# The tests can be performed running program.py or calling pytest in the directory
if __name__ == '__main__':
    Test.main()
