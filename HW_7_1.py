print('<<<<< Добро из рук в руки >>>>>')

import os

os.chdir("C:\\Users\\trofi\\PycharmProjects\\untitled2\\HW_7")

while True:

    def good_data_writer():
        with open('data.txt', 'w', encoding='utf-8') as v:
            v.write(repr(good_data))


    with open('data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            good_data = eval(line)

    print('Выберите правило приема-раздачи вещей.')
    print('Для выбора правила приема-раздачи "стэк" (LIFO) введите "1" и нажмите Enter.')
    print('Для выбора правила приема-раздачи "очередь" (FIFO) введите "2" и нажмите Enter.')
    STRATEGY = str(input())
    if STRATEGY == '1' or STRATEGY == '2':
        good = input('Здравствуйте! Что у вас?')
        if good:
            quantity = input('Сколько?')
            good_data.append({'name': good, 'amount': quantity})
            print('Спасибо!\n')
        else:
            if good_data.__len__() < 1:
                print('Извините, пока ничего нет. Зайдите немного позже, что-то обязательно появится!\n')
            else:
                if STRATEGY == '1':
                    good_data.reverse()
                    if int(good_data[0].get('amount')) > 1:
                        print('Возьмите, вот вам', good_data[0].get('name'), '\n')
                        qty = int(good_data[0].get('amount')) - 1
                        good_data[0].update({'amount': qty})
                        good_data.reverse()
                    else:
                        print('Возьмите, вот вам', good_data[0].get('name'), '\n')
                        good_data.pop(0)
                        good_data.reverse()
                elif STRATEGY == '2':
                    if int(good_data[0].get('amount')) > 1:
                        print('Возьмите, вот вам', good_data[0].get('name'), '\n')
                        qty = int(good_data[0].get('amount')) - 1
                        good_data[0].update({'amount': qty})
                    else:
                        print('Возьмите, вот вам', good_data[0].get('name'), '\n')
                        good_data.pop(0)
        good_data_writer()
    else:
        print('Правило приема-раздачи вещей не выбрано.\n')
