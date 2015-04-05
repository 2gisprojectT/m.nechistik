__author__ = 'mikhailnecistik'

from unittest import TestCase
from Lion import Lion
import unittest

# Test for class Lion
class LionTest(TestCase):
    Lion_script = {('антилопа', 'сытый'): ('спать, и переходит в состояние голодный', 'голодный'),
                    ('охотник', 'сытый'): ('убежать от охотника, и переходит в состояние голодный', 'голодный'),
                    ('дерево', 'сытый'): ('смотреть на дерево, и переходит в состояние голодный', 'голодный'),

                    ('антилопа', 'голодный'): ('съесть антилопу, и переходит в состояние сытый', 'сытый'),
                    ('охотник', 'голодный'): ('убежать от охотника, и остаётся голодным', 'голодный'),
                    ('дерево', 'голодный'): ('спать в тени дерева, и остаётся голодным', 'голодный')}

    def test_init(self):
        Lion_status = 'голодный'
        L = Lion(self.Lion_script, Lion_status)

        # set status and check that it is possible to get the correct current status
        self.assertEqual('голодный', L.Lion_status, 'Error when status hungry in Lion')
        self.assertEqual('', L.Lion_action, 'Error when status hungry in Lion')
        self.assertEqual(self.Lion_script, L.Lion_script, 'Error when status hungry in Lion')


        Lion_status = 'сытый'
        L = Lion(self.Lion_script, Lion_status)

        # set status and check that it is possible to get the correct current status
        self.assertEqual('сытый', L.Lion_status, 'Error when status hungry in Lion')
        self.assertEqual('', L.Lion_action, 'Error when status hungry in Lion')
        self.assertEqual(self.Lion_script, L.Lion_script, 'Error when status hungry in Lion')



    def test_do_all_antelope(self):
        Lion_status = 'голодный'
        L = Lion(self.Lion_script, Lion_status)

        L.do_all('антилопа')
        self.assertEqual('сытый', L.Lion_status, 'Error when status hungry in Lion')
        self.assertEqual('съесть антилопу, и переходит в состояние сытый', L.Lion_action, 'Error when status hungry in Lion')


        Lion_status = 'сытый'
        L = Lion(self.Lion_script, Lion_status)

        L.do_all('антилопа')
        self.assertEqual('голодный', L.Lion_status, 'Error when status hungry in Lion')
        self.assertEqual('спать, и переходит в состояние голодный', L.Lion_action, 'Error when status hungry in Lion')


    def test_do_all_hunter(self):
        Lion_status = 'голодный'
        L = Lion(self.Lion_script, Lion_status)

        L.do_all('охотник')
        self.assertEqual('голодный', L.Lion_status, 'Error when status hungry in Lion')
        self.assertEqual('убежать от охотника, и остаётся голодным', L.Lion_action, 'Error when status hungry in Lion')


        Lion_status = 'сытый'
        L = Lion(self.Lion_script, Lion_status)

        L.do_all('охотник')
        self.assertEqual('голодный', L.Lion_status, 'Error when status hungry in Lion')
        self.assertEqual('убежать от охотника, и переходит в состояние голодный', L.Lion_action, 'Error when status hungry in Lion')


    def test_do_all_tree(self):
        Lion_status = 'голодный'
        L = Lion(self.Lion_script, Lion_status)

        L.do_all('дерево')
        self.assertEqual('голодный', L.Lion_status, 'Error when status hungry in Lion')
        self.assertEqual('спать в тени дерева, и остаётся голодным', L.Lion_action, 'Error when status hungry in Lion')


        Lion_status = 'сытый'
        L = Lion(self.Lion_script, Lion_status)

        L.do_all('дерево')
        self.assertEqual('голодный', L.Lion_status, 'Error when status hungry in Lion')
        self.assertEqual('смотреть на дерево, и переходит в состояние голодный', L.Lion_action, 'Error when status hungry in Lion')

if __name__ == '__main__':
    unittest.main()
