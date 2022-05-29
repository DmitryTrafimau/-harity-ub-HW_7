print('<<<<< Добро из рук в руки >>>>>')

import os
os.chdir("C:\\Users\\trofi\\PycharmProjects\\untitled2\\HW_7")

while True:
    good_data = []


    def good_data_writer():
        with open('data.txt', 'w', encoding='utf-8') as v:
            for good in good_data:
                v.write(good + '\n')


    with open('data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            good_data.append(line.strip('\n'))

    print('Выберите правило приема-раздачи вещей.')
    print('Для выбора правила приема-раздачи "стэк" (LIFO) введите "1" и нажмите Enter.')
    print('Для выбора правила приема-раздачи "очередь" (FIFO) введите "2" и нажмите Enter.')
    STRATEGY = input()
    print(STRATEGY)
    if STRATEGY == '1' or STRATEGY == '2':
        good = input('Здравствуйте! Что у вас?')
        if good:
            good_data.append(good)
            print('Спасибо!\n')
        else:
            if good_data.__len__() < 1:
                print('Извините, пока ничего нет. Зайдите немного позже, что-то обязательно появится!\n')
            else:
                if STRATEGY == '1':
                    print('Возьмите, вот вам', good_data.pop(), '\n')
                elif STRATEGY == '2':
                    print('Возьмите, вот вам', good_data.pop(0), '\n')
        good_data_writer()
        print(good_data)
    else:
        print('Правило приема-раздачи вещей не выбрано.\n')
