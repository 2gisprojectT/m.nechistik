__author__ = 'mikhailnecistik'

# Class containing dict for Lion status
class Lion:
    # Constructor
    def __init__(self):
        self.Lion_status = {'fed': 'сытый', 'hungry': 'голодный'}
        # Initially Lion is always hungry
        self.set_cur_status('hungry')

    # set current Lion status
    def set_cur_status(self, stat):
        self.cur_status = self.Lion_status[stat]

    # get current Lion status
    def get_cur_status(self):
        return self.cur_status


# Class containing dict for Lion actions
class Action:
    # Constructor
    def __init__(self):
        self.Lion_fed = {'антилопа': 'спать, и переходит в состояние голодный', 'охотник': 'убежать от охотника, и переходит в состояние голодный','дерево': 'смотреть на дерево, и переходит в состояние голодный'}
        self.Lion_hungry = {'антилопа': 'съесть антилопу, и переходит в состояние сытый', 'охотник': 'убежать от охотника, и остаётся голодным','дерево': 'спать в тени дерева, и остаётся голодным'}
        self.Lion_status_act = {'голодный': self.Lion_hungry, 'сытый': self.Lion_fed}

    # get action for Lion
    def get_action(self, stat, text):
        return self.Lion_status_act[stat][text]

# Class containing dict for change Lion status
class Change:
    # Constructor
    def __init__(self):
        self.change_fed = {'антилопа': 'hungry', 'охотник': 'hungry','дерево': 'hungry'}
        self.change_hungry = {'антилопа': 'fed', 'охотник': 'hungry','дерево': 'hungry'}
        self.change_Lion = {'голодный': self.change_hungry, 'сытый': self.change_fed}

    # change Lion current status
    def ch_lion(self, L, text):
        L.set_cur_status(self.change_Lion[L.get_cur_status()][text])

if __name__ == '__main__':

    # Initialization
    L = Lion()
    A = Action()
    C = Change()

    while True:
        print('\n')
        print('Сейчас лев '+ L.get_cur_status() + '!')
        print('Выберите один из следующих объектов: антилопа, охотник, дерево')
        print('Если вам наскучил лев, вы всегда можете выйти: выход')
        print('Введите объект: ')
        # input from keyboard
        text = input()
        # For exit
        if text == 'выход':
            break
        else:
            # For wrong data
            try:
                print('Лев решает ' + A.get_action(L.get_cur_status(),text))
                C.ch_lion(L, text)
            except:
                print('Ошибка: Лев не знает что делать!')
