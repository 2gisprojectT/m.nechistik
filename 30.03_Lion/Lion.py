__author__ = 'mikhailnecistik'

# Class containing dict for Lion status
class Lion:
    # Constructor
    def __init__(self):
        # Initially Lion is always hungry
        self.Lion_status = 'голодный'
        self.Lion_action = {('антилопа', 'сытый'): ('спать, и переходит в состояние голодный', 'голодный'),
                            ('охотник', 'сытый'): ('убежать от охотника, и переходит в состояние голодный', 'голодный'),
                            ('дерево', 'сытый'): ('смотреть на дерево, и переходит в состояние голодный','голодный'),

                            ('антилопа', 'голодный'): ('съесть антилопу, и переходит в состояние сытый', 'сытый'),
                            ('охотник', 'голодный'): ('убежать от охотника, и остаётся голодным', 'голодный'),
                            ('дерево', 'голодный'): ('спать в тени дерева, и остаётся голодным', 'голодный')}



    # get current Lion status
    def get_status(self):
        return self.Lion_status

    def get_action(self, text):
        buf = self.Lion_action[(text, self.Lion_status)][0]
        self.Lion_status = self.Lion_action[(text, self.Lion_status)][1]
        return buf

if __name__ == '__main__':

    # Initialization
    L = Lion()

    while True:
        print('\n')
        print('Сейчас лев '+ L.get_status() + '!')
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
                print('Лев решает ' + L.get_action(text))
            except:
                print('Ошибка: Лев не знает что делать!')
