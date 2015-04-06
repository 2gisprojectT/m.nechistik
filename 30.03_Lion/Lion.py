__author__ = 'mikhailnecistik'


# Class containing dict for Lion status
class Lion:
    # Constructor
    def __init__(self, Lion_script, Lion_status):
        # Initially Lion is always hungry
        for i in Lion_script:
            if Lion_status in i[1] and Lion_status != "":
                self.Lion_script = Lion_script
                self.Lion_status = Lion_status
                self.Lion_action = ""
                break

            else:
                self.Lion_status = None

    def do_all(self, text):
        self.Lion_action = self.Lion_script[(text, self.Lion_status)][0]
        self.Lion_status = self.Lion_script[(text, self.Lion_status)][1]


if __name__ == '__main__':

    # Initialization
    Lion_script = {('антилопа', 'сытый'): ('спать, и переходит в состояние голодный', 'голодный'),
                    ('охотник', 'сытый'): ('убежать от охотника, и переходит в состояние голодный', 'голодный'),
                    ('дерево', 'сытый'): ('смотреть на дерево, и переходит в состояние голодный', 'голодный'),

                    ('антилопа', 'голодный'): ('съесть антилопу, и переходит в состояние сытый', 'сытый'),
                    ('охотник', 'голодный'): ('убежать от охотника, и остаётся голодным', 'голодный'),
                    ('дерево', 'голодный'): ('спать в тени дерева, и остаётся голодным', 'голодный')}
    status = []
    action = []

    for i in Lion_script:
        if i[1] not in status:
            status.append(i[1])

    for a in Lion_script:
        if a[0] not in action:
            action.append(a[0])
    while True:
        print('Выберите один из статусов льва: ')
        for i in status:
            print(i)
        print('Введите статус: ')
        Lion_status = input()

        L = Lion(Lion_script, Lion_status)
        if L.Lion_status == None:
            print('Ошибка: Лев не знает какой он!')
        else:
            break


    while True:
        print('\n')
        print('Сейчас лев '+ L.Lion_status + '!')
        print('Выберите один из следующих объектов:')
        for a in action:
            print(a)
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
                L.do_all(text)
                print('Лев решает ' + L.Lion_action)
            except:
                print('Ошибка: Лев не знает что делать!')




