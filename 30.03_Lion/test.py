__author__ = 'mikhailnecistik'

from unittest import TestCase
from Lion import Lion
import unittest


class LionTest(TestCase):
    Lion_script = {('антилопа', 'голодный'): ('съесть', 'сытый')}

    def test_init(self):
        Lion_status = 'голодный'
        L = Lion(self.Lion_script, Lion_status)
        self.assertEqual('голодный', L.Lion_status, 'Error, wrong status')
        self.assertEqual('', L.Lion_action, 'Error, wrong action')
        self.assertEqual(self.Lion_script, L.Lion_script, 'Error, wrong dict')

    def test_init_empty_lion_status(self):
        Lion_status = ''
        L = Lion(self.Lion_script, Lion_status)
        self.assertIsNone(L.Lion_status, 'Error')

    def test_init_wrong_lion_status(self):
        Lion_status = 'nxfd'
        L = Lion(self.Lion_script, Lion_status)
        self.assertIsNone(L.Lion_status, 'Error')

    def test_do_all(self):
        Lion_status = 'голодный'
        L = Lion(self.Lion_script, Lion_status)
        L.do_all('антилопа')
        self.assertEqual('сытый', L.Lion_status, 'Error, wrong status')
        self.assertEqual('съесть', L.Lion_action, 'Error, wrong action')

    def test_do_all_wrong_data(self):
        Lion_status = 'голодный'
        L = Lion(self.Lion_script, Lion_status)
        try:
            L.do_all('dshsdhsfh')
        except:
            print('')
        self.assertEqual('голодный', L.Lion_status, 'Error, wrong status, when wrong data')
        self.assertEqual('', L.Lion_action, 'Error, wrong action, when wrong data')

    def test_do_all_empty_data(self):
        Lion_status = 'голодный'
        L = Lion(self.Lion_script, Lion_status)
        try:
            L.do_all('')
        except:
            print('')
        self.assertEqual('голодный', L.Lion_status, 'Error, wrong status, when wrong data')
        self.assertEqual('', L.Lion_action, 'Error, wrong action, when wrong data')

if __name__ == '__main__':
    unittest.main()
