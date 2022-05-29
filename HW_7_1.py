print('<<<<< Добро из рук в руки >>>>>')

while True:
    good_data = []
    print('Выберите правило приема-раздачи вещей.')
    print('Для выбора правила приема-раздачи "стэк" (LIFO) введите "1" и нажмите Enter.')
    print('Для выбора правила приема-раздачи "очередь" (FIFO) введите "2" и нажмите Enter.')
    STRATEGY = input()
    if STRATEGY == '1':
        while STRATEGY == '1':
            good = input('Здравствуйте! Что у вас?')
            if good:
                good_data.append(good)
                print('Спасибо!\n')
            else:
                if good_data.__len__() < 1:
                    print('Извините, пока ничего нет. Зайдите немного позже, что-то обязательно появится!\n')
                    break
                else:
                    print('Возьмите, вот вам', good_data.pop(), '\n')
    elif STRATEGY == '2':
        while STRATEGY == '2':
            good = input('Здравствуйте! Что у вас?')
            if good:
                good_data.append(good)
                print('Спасибо!\n')
            else:
                if good_data.__len__() < 1:
                    print('Извините, пока ничего нет. Зайдите немного позже, что-то обязательно появится!\n')
                    break
                else:
                    print('Возьмите, вот вам', good_data.pop(0), '\n')
    else:
        print('Правило приема-раздачи вещей не выбрано.\n')