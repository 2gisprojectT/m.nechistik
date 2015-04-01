__author__ = 'mikhailnecistik'

from unittest import TestCase
from Lion import Lion
from Lion import Action
from Lion import Change
import unittest

# Test for class Lion
class LionTest(TestCase):
    # Test Lion initialization
    def test_init(self):
        L = Lion()

        # Test initial status
        self.assertEqual('голодный', L.cur_status, 'Initial status is wrong in Lion')

        # Test key in dict Lion_status from class Lion
        self.assertIn('fed', L.Lion_status, 'There is no status fed in dict Lion_status')
        self.assertIn('hungry', L.Lion_status, 'There is no status hungry in dict Lion_status')

        # Test status for corresponding key in dict Lion_status from class Lion
        self.assertEqual('голодный', L.Lion_status['hungry'], 'Status hungry is wrong in dict Lion')
        self.assertEqual('сытый', L.Lion_status['fed'], 'Status fed is wrong in dict Lion')


    def test_set(self):
        L = Lion()

        # set status and check it
        L.set_cur_status('hungry')
        self.assertEqual('голодный', L.cur_status, 'Error when set status hungry in Lion')

        L.set_cur_status('fed')
        self.assertEqual('сытый', L.cur_status, 'Error when set status fed in Lion')

    def test_get(self):
        L = Lion()

        # set status and check that it is possible to get the correct current status
        L.set_cur_status('hungry')
        self.assertEqual('голодный', L.get_cur_status(), 'Error when set status hungry in Lion')

        L.set_cur_status('fed')
        self.assertEqual('сытый', L.get_cur_status(), 'Error when set status fed in Lion')

# Test for class Action
class ActionTest(TestCase):
    def test_init(self):
        A = Action()

        # Test key in dict Lion_fed from class Action
        self.assertIn('антилопа', A.Lion_fed, 'There is no status антилопа in dict Lion_fed')
        self.assertIn('охотник', A.Lion_fed, 'There is no status охотник in dict Lion_fed')
        self.assertIn('дерево', A.Lion_fed, 'IThere is no status дерево in dict Lion_fed')

        # Test key in dict Lion_hungry from class Action
        self.assertIn('антилопа', A.Lion_hungry, 'There is no status антилопа in dict Lion_hungry')
        self.assertIn('охотник', A.Lion_hungry, 'There is no status охотник in dict Lion_hungry')
        self.assertIn('дерево', A.Lion_hungry, 'There is no status дерево in dict Lion_hungry')

        # Test key in dict Lion_status_act from class Action
        self.assertIn('голодный', A.Lion_status_act, 'There is no status голодный in dict Lion_status_act')
        self.assertIn('сытый', A.Lion_status_act, 'There is no status сытый in dict Lion_status_act')


        # Test actions for corresponding key in dict Lion_fed from class Action
        self.assertEqual('спать, и переходит в состояние голодный', A.Lion_fed['антилопа'], 'Wrong action in status key in dict Lion_fed')
        self.assertEqual('убежать от охотника, и переходит в состояние голодный', A.Lion_fed['охотник'], 'Wrong action in status key in dict Lion_fed')
        self.assertEqual('смотреть на дерево, и переходит в состояние голодный', A.Lion_fed['дерево'], 'Wrong action in key дерево in dict Lion_fed')

        # Test actions for corresponding key in dict Lion_hungry from class Action
        self.assertEqual('съесть антилопу, и переходит в состояние сытый', A.Lion_hungry['антилопа'], 'Wrong action in key антилопа in dict Lion_hungry')
        self.assertEqual('убежать от охотника, и остаётся голодным', A.Lion_hungry['охотник'], 'Wrong action in key охотник in dict Lion_hungry')
        self.assertEqual('спать в тени дерева, и остаётся голодным', A.Lion_hungry['дерево'], 'Wrong action in key дерево in dict Lion_hungry')

        # Test dict for corresponding key in dict Lion_status_act from class Action
        self.assertEqual({'антилопа': 'спать, и переходит в состояние голодный', 'охотник': 'убежать от охотника, и переходит в состояние голодный','дерево': 'смотреть на дерево, и переходит в состояние голодный'}, A.Lion_status_act['сытый'], 'Wrong dict in key сытый in dict Lion_status_act')
        self.assertEqual({'антилопа': 'съесть антилопу, и переходит в состояние сытый', 'охотник': 'убежать от охотника, и остаётся голодным','дерево': 'спать в тени дерева, и остаётся голодным'}, A.Lion_status_act['голодный'], 'Wrong dict in key голодный in dict Lion_status_act')

    def test_get(self):
        A = Action()

        # check return actions for corresponding key, when current Lion status is fed
        self.assertEqual('спать, и переходит в состояние голодный', A.get_action('сытый', 'антилопа'), 'Wrong action for status антилопа when lion is сытый')
        self.assertEqual('убежать от охотника, и переходит в состояние голодный', A.get_action('сытый', 'охотник'), 'Wrong action for status охотник when lion is сытый')
        self.assertEqual('смотреть на дерево, и переходит в состояние голодный', A.get_action('сытый', 'дерево'), 'Wrong action for status дерево when lion is сытый')

        # check return actions for corresponding key, when current Lion status is hungry
        self.assertEqual('съесть антилопу, и переходит в состояние сытый', A.get_action('голодный', 'антилопа'), 'Wrong action for status антилопа when lion is сытый')
        self.assertEqual('убежать от охотника, и остаётся голодным', A.get_action('голодный', 'охотник'), 'Wrong action for status охотник when lion is сытый')
        self.assertEqual('спать в тени дерева, и остаётся голодным', A.get_action('голодный', 'дерево'), 'Wrong action for status дерево when lion is сытый')

# Test for class Change
class ChangeTest(TestCase):
    def test_init(self):
        C = Change()

        # Test key in dict change_fed from class Change
        self.assertIn('антилопа', C.change_fed, 'There is no key антилопа in dict change_fed')
        self.assertIn('охотник', C.change_fed, 'There is no key охотник in dict change_fed')
        self.assertIn('дерево', C.change_fed, 'There is no key дерево in dict change_fed')

        # Test key in dict change_hungry from class Change
        self.assertIn('антилопа', C.change_hungry, 'There is no key антилопа in dict change_hungry')
        self.assertIn('охотник', C.change_hungry, 'There is no key охотник in dict change_hungry')
        self.assertIn('дерево', C.change_hungry, 'There is no key дерево in dict change_hungry')

        # Test key in dict change_Lion from class Change
        self.assertIn('голодный', C.change_Lion, 'There is no key голодный in dict change_Lion')
        self.assertIn('сытый', C.change_Lion, 'There is no key сытый in dict change_Lion')


        # Test status for corresponding key in dict change_fed from class Change
        self.assertEqual('hungry', C.change_fed['антилопа'], 'Wrong status in key антилопа in dict change_fed')
        self.assertEqual('hungry', C.change_fed['охотник'], 'Wrong status in key охотник in dict change_fed')
        self.assertEqual('hungry', C.change_fed['дерево'], 'Wrong status in key дерево in dict change_fed')

        # Test status for corresponding key in dict change_hungry from class Change
        self.assertEqual('fed', C.change_hungry['антилопа'], 'Wrong status in key антилопа in dict change_hungry')
        self.assertEqual('hungry', C.change_hungry['охотник'], 'Wrong status in key охотник in dict change_hungry')
        self.assertEqual('hungry', C.change_hungry['дерево'], 'Wrong status in key дерево in dict change_hungry')

        # Test dict for corresponding key in dict change_Lion from class Change
        self.assertEqual({'антилопа': 'fed', 'охотник': 'hungry','дерево': 'hungry'}, C.change_Lion['голодный'], 'Wrong dict in key голодный in dict change_Lion')
        self.assertEqual({'антилопа': 'hungry', 'охотник': 'hungry','дерево': 'hungry'}, C.change_Lion['сытый'], 'Wrong dict in key сытый in dict change_Lion')

    # Test change Lion status
    def test_change(self):
        L = Lion()
        C = Change()

        # Set Lion status
        L.set_cur_status('fed')
        # Change lion status
        C.ch_lion(L, 'антилопа')
        # Check that status was changed correct
        self.assertEqual('голодный', L.cur_status, 'Improperly changed the status of a lion when he current status is сытый and key is антилопа')

        L.set_cur_status('fed')
        C.ch_lion(L, 'охотник')
        self.assertEqual('голодный', L.cur_status, 'Improperly changed the status of a lion when he current status is сытый and key is охотник')

        L.set_cur_status('fed')
        C.ch_lion(L, 'дерево')
        self.assertEqual('голодный', L.cur_status, 'Improperly changed the status of a lion when he current status is сытый and key is дерево')


        L.set_cur_status('hungry')
        C.ch_lion(L, 'антилопа')
        self.assertEqual('сытый', L.cur_status, 'Improperly changed the status of a lion when he current status is голодный and key is антилопа')

        L.set_cur_status('hungry')
        C.ch_lion(L, 'охотник')
        self.assertEqual('голодный', L.cur_status, 'Improperly changed the status of a lion when he current status is голодный and key is охотник')

        L.set_cur_status('hungry')
        C.ch_lion(L, 'дерево')
        self.assertEqual('голодный', L.cur_status, 'Improperly changed the status of a lion when he current status is голодный and key is дерево')

if __name__ == '__main__':
    unittest.main()
