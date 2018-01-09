import unittest

from challenges.recursion.source.basic import *


class TestBasic(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(5), 120)

    def test_bunny_ears(self):
        self.assertEqual(bunny_ears(0), 0)
        self.assertEqual(bunny_ears(1), 2)
        self.assertEqual(bunny_ears(2), 4)
        self.assertEqual(bunny_ears(10), 20)
        self.assertEqual(bunny_ears(60), 120)
    
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(15), 610)
        self.assertEqual(fibonacci(24), 46368)
    
    def test_bunny_ears2(self):
        self.assertEqual(bunny_ears2(0), 0)
        self.assertEqual(bunny_ears2(1), 2)
        self.assertEqual(bunny_ears2(2), 5)
        self.assertEqual(bunny_ears2(10), 25)
        self.assertEqual(bunny_ears2(60), 150)
    
    def test_triangle(self):
        self.assertEqual(triangle(0), 0)
        self.assertEqual(triangle(1), 1)
        self.assertEqual(triangle(2), 3)
        self.assertEqual(triangle(10), 55)
        self.assertEqual(triangle(60), 1830)

    def test_count_7(self):
        self.assertEqual(count_7(0), 0)
        self.assertEqual(count_7(1), 0)
        self.assertEqual(count_7(27), 1)
        self.assertEqual(count_7(277), 2)
        self.assertEqual(count_7(7777), 4)
        self.assertEqual(count_7(17273477577767891077), 10)
    
    def test_count_8(self):
        self.assertEqual(count_8(0), 0)
        self.assertEqual(count_8(1), 0)
        self.assertEqual(count_8(87), 1)
        self.assertEqual(count_8(8778), 2)
        self.assertEqual(count_8(8818), 4)
        self.assertEqual(count_8(8810080088), 7)
        self.assertEqual(count_8(888), 5)
        self.assertEqual(count_8(888888), 11)
    
    def test_power_n(self):
        self.assertEqual(power_n(3, 0), 1)
        self.assertEqual(power_n(0, 2), 0)
        self.assertEqual(power_n(3, 3), 27)
        self.assertEqual(power_n(3, 1), 3)
        self.assertEqual(power_n(5, 5), 3125)
        self.assertEqual(power_n(5, 8), 390625)
        self.assertEqual(power_n(3, 13), 1594323)

    def test_count_x(self):
        self.assertEqual(count_x('yargs'), 0)
        self.assertEqual(count_x('xargs'), 1)
        self.assertEqual(count_x('xaxrgs'), 2)
        self.assertEqual(count_x(''), 0)
        self.assertEqual(count_x('xxiix'), 3)
    
    def test_count_hi(self):
        self.assertEqual(count_hi('yargs'), 0)
        self.assertEqual(count_hi('hiargs'), 1)
        self.assertEqual(count_hi('hiahirgs'), 2)
        self.assertEqual(count_hi(''), 0)
        self.assertEqual(count_hi('hhhiihi'), 2)
        self.assertEqual(count_hi('hihihihi'), 4)
    
    def test_change_x_y(self):
        self.assertEqual(change_x_y('yyyy'), 'yyyy')
        self.assertEqual(change_x_y('xyxy'), 'yyyy')
        self.assertEqual(change_x_y('xxxx'), 'yyyy')
        self.assertEqual(change_x_y('aaaa'), 'aaaa')
        self.assertEqual(change_x_y('xaaax'), 'yaaay')
        self.assertEqual(change_x_y('yaaay'), 'yaaay')
        self.assertEqual(change_x_y(''), '')
        self.assertEqual(change_x_y('a'), 'a')
        self.assertEqual(change_x_y('x'), 'y')
    
    def test_change_pi(self):
        self.assertEqual(change_pi('pipi'), '3.143.14')
        self.assertEqual(change_pi('piaaapi'), '3.14aaa3.14')
        self.assertEqual(change_pi('aaapiaa'), 'aaa3.14aa')
        self.assertEqual(change_pi('poipip'), 'poi3.14p')
        self.assertEqual(change_pi('yaaay'), 'yaaay')
        self.assertEqual(change_pi(''), '')
        self.assertEqual(change_pi('pi'), '3.14')

    def test_no_x(self):
        self.assertEqual(no_x('x'), '')
        self.assertEqual(no_x('xyxy'), 'yy')
        self.assertEqual(no_x('xxxx'), '')
        self.assertEqual(no_x('aaaa'), 'aaaa')
        self.assertEqual(no_x('abc'), 'abc')
        self.assertEqual(no_x('xxjjxx'), 'jj')
        self.assertEqual(no_x(''), '')
        self.assertEqual(no_x('a'), 'a')

    def test_array_6(self):
        self.assertTrue(array_6([6], 0))
        self.assertTrue(array_6([6, 4 , 1, 0, 6], 3))
        self.assertTrue(array_6([4, 3, 2, 1, 6], 4))
        self.assertTrue(array_6([1, 2, 3, 6, 6, 6, 6], 4))
        self.assertFalse(array_6([6], -1))
        self.assertFalse(array_6([6, 0, 9 , 0], 2))
        self.assertFalse(array_6([6], 1))
        self.assertFalse(array_6([], 0))

    def test_array_220(self):
        self.assertFalse(array_220([0], 0))
        self.assertTrue(array_220([0, 0], 0))
        self.assertFalse(array_220([3, 30, 300], 2))
        self.assertFalse(array_220([3, 30], 4))
        self.assertFalse(array_220([2, 20], 1))
        self.assertTrue(array_220([2, 200, 20, 200], 1))
        self.assertTrue(array_220([3, 30, 300], 1))
        self.assertTrue(array_220([1, 2, 20], 0))

    def test_all_star(self):
        self.assertEqual(all_star('a'), 'a')
        self.assertEqual(all_star(''), '')
        self.assertEqual(all_star('ab'), 'a*b')
        self.assertEqual(all_star('abcde'), 'a*b*c*d*e')

    def test_pair_star(self):
        self.assertEqual(pair_star('a'), 'a')
        self.assertEqual(pair_star(''), '')
        self.assertEqual(pair_star('ab'), 'ab')
        self.assertEqual(pair_star('all'), 'al*l')
        self.assertEqual(pair_star('hello'), 'hel*lo')
        self.assertEqual(pair_star('xxyy'), 'x*xy*y')
        self.assertEqual(pair_star('aaaa'), 'a*a*a*a')

    def test_end_x(self):
        self.assertEqual(end_x('re'), 're')
        self.assertEqual(end_x('xxre'), 'rexx')
        self.assertEqual(end_x('rexx'), 'rexx')
        self.assertEqual(end_x('xxhixx'), 'hixxxx')
        self.assertEqual(end_x('xyxyxy'), 'yyyxxx')

    def test_count_pairs(self):
        self.assertEqual(count_pairs('axa'), 1)
        self.assertEqual(count_pairs('ax'), 0)
        self.assertEqual(count_pairs('axax'), 2)
        self.assertEqual(count_pairs('axbx'), 1)
        self.assertEqual(count_pairs('axaba'), 2)

    def test_string_clean(self):
        self.assertEqual(string_clean('xyxy'), 'xyxy')
        self.assertEqual(string_clean('Hello'), 'Helo')
        self.assertEqual(string_clean('pizzza'), 'piza')
        self.assertEqual(string_clean('kaabbcc'), 'kabc')
        self.assertEqual(string_clean('abbcccddddeeeeeff'), 'abcdef')
        self.assertEqual(string_clean('A'), 'A')
        self.assertEqual(string_clean(''), '')

    def test_parent_bit(self):
        self.assertEqual(parent_bit('xyz(abc)123'), '(abc)')
        self.assertEqual(parent_bit('(abc)123'), '(abc)')
        self.assertEqual(parent_bit('xyz(abc)'), '(abc)')
        self.assertEqual(parent_bit('xyz(abc123'), '')
        self.assertEqual(parent_bit('xyz()'), '()')
        self.assertEqual(parent_bit('(xyz)'), '(xyz)')
    
    def test_nest_paren(self):
        self.assertFalse(nest_paren('abc'))
        self.assertFalse(nest_paren('(()))'))
        self.assertFalse(nest_paren('a(b(c)'))
        self.assertFalse(nest_paren('(})'))
        self.assertFalse(nest_paren('(}'))
        self.assertFalse(nest_paren('([])'))
        self.assertFalse(nest_paren('((abc))'))
        self.assertTrue(nest_paren('(())'))
        self.assertTrue(nest_paren('(((())))'))
        self.assertTrue(nest_paren('()'))

    def test_str_count(self):
        self.assertEqual(str_count('catcowcat', 'cat'), 2)
        self.assertEqual(str_count('catcowcat', 'cow'), 1)
        self.assertEqual(str_count('catcowcat', 'dof'), 0)
        self.assertEqual(str_count('catcat', 'cat'), 2)
        self.assertEqual(str_count('cacat', 'cat'), 1)
        self.assertEqual(str_count('catcowcat', 'cowcat'), 1)
        self.assertEqual(str_count('dogcatdogcatdog', 'dog'), 3)

    def test_str_copies(self):
        self.assertTrue(str_copies('catcowcat', 'cat', 2))
        self.assertTrue(str_copies('catcowcat', 'cow', 1))
        self.assertTrue(str_copies('catcowcat', 'dof', 0))
        self.assertTrue(str_copies('catcat', 'cat', 2))
        self.assertTrue(str_copies('cacat', 'cat', 1))
        self.assertTrue(str_copies('catcowcat', 'cowcat', 1))
        self.assertTrue(str_copies('dogcatdogcatdog', 'dog', 3))
        self.assertFalse(str_copies('catcat', 'cat', 3))
        self.assertFalse(str_copies('dogcatdodgcatdog', 'dog', 3))

    def test_str_dist(self):
        self.assertEqual(str_dist('catcowcat', 'cow'), 3)
        self.assertEqual(str_dist('catcowcat', 'cat'), 9)
        self.assertEqual(str_dist('cccatcowcatxx', 'cat'), 9)
        self.assertEqual(str_dist('catcowcat', 'bow'), 0)
        self.assertEqual(str_dist('catcowcat', 'ow'), 2)
        self.assertEqual(str_dist('catcowcat', 't'), 7)

