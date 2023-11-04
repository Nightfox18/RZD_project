#класс локомотив
class Locomotive():

    locomotive_count = 0

    def __init__ (self, parovoz, electrovoz, teplovoz, gruzovoy_vagon, special_vagon, passazhirzskiy_vagon):

        #Переменные класса
        self.parovoz = parovoz
        self.electrovoz = electrovoz
        self.teplovoz = teplovoz
        self.gruzovoy_vagon = gruzovoy_vagon
        self.special_vagon = special_vagon
        self.passazhirzskiy_vagon = passazhirzskiy_vagon

        Locomotive.locomotive_count += 1

    #Вывод количества локомотивов
    def display_count(self):

        return 'Всего локомотивов: %d' % Locomotive.locomotive_count


    #Функция определения вывода состава локомотива

    def __del__(self):

            class_name = self.__class__.__name__
            print('{} уничтожен'.format(class_name))


    def errors_and_complte_of_a_locomotive(self):

        if self.parovoz==0 and self.electrovoz == 0 and self.teplovoz == 0:
            return 'ОШИБКА: Состав не может быть без ведущего вагона'

        elif self.parovoz > self.teplovoz and self.parovoz > self.electrovoz and self.parovoz <=1:

            if self.gruzovoy_vagon == 0 and self.special_vagon != 0 and self.passazhirzskiy_vagon != 0:
                return 'Ведущий вагон Паровоз: {}. Почтовых вагонов: {}. Пассажирских вагонов: {}'.format(self.parovoz, self.special_vagon,
                                                                           self.passazhirzskiy_vagon)

            elif self.special_vagon == 0 and self.gruzovoy_vagon != 0 and self.passazhirzskiy_vagon != 0:
                return 'Ведущий вагон Паровоз: {}. Грузовых вагонов: {}. Пассажирских вагонов: {}'.format(self.parovoz, self.gruzovoy_vagon,
                                                                           self.passazhirzskiy_vagon)

            elif self.passazhirzskiy_vagon == 0 and self.special_vagon != 0 and self.gruzovoy_vagon != 0:
                return 'Ведущий вагон Паровоз: {}. Почтовых вагонов: {}. Грузовых вагонов: {}'.format(self.parovoz, self.special_vagon,
                                                                           self.gruzovoy_vagon)

            elif self.gruzovoy_vagon != 0 and self.special_vagon != 0 and self.passazhirzskiy_vagon != 0:
                return 'Ведущий вагон Паровоз: {}. Почтовых вагонов: {}. Пассажирских вагонов: {}. Грузовых вагонов: {}'.format(self.parovoz, self.special_vagon,
                                                                           self.passazhirzskiy_vagon, self.gruzovoy_vagon)

            elif self.gruzovoy_vagon == 0 and self.passazhirzskiy_vagon == 0 and self.special_vagon != 0:
                return 'Ведущий вагон Паровоз: {}. Почтовых вагонов: {}'.format(self.parovoz, self.special_vagon)

            elif self.gruzovoy_vagon == 0 and self.special_vagon == 0 and self.passazhirzskiy_vagon != 0:
                return 'Ведущий вагон Паровоз: {}. Пассажирских вагонов: {}'.format(self.parovoz, self.passazhirzskiy_vagon)

            elif self.special_vagon == 0 and self.passazhirzskiy_vagon == 0 and self.gruzovoy_vagon != 0:
                return 'Ведущий вагон Паровоз {}. Грузовых вагонов: {}'.format(self.parovoz, self.gruzovoy_vagon)

            elif self.special_vagon == 0 and self.passazhirzskiy_vagon == 0 and self.gruzovoy_vagon == 0:
                return 'Ведущий вагон Паровоз: {}'.format(self.parovoz)

        elif self.teplovoz > self.parovoz and self.teplovoz > self.electrovoz and self.teplovoz <=1:

            if self.gruzovoy_vagon == 0 and self.special_vagon != 0 and self.passazhirzskiy_vagon != 0:
                return 'Ведущий вагон Тепловоз: {}. Почтовых вагонов: {}. Пассажирских вагонов: {}'.format(self.teplovoz, self.special_vagon,
                                                                           self.passazhirzskiy_vagon)

            elif self.special_vagon == 0 and self.gruzovoy_vagon != 0 and self.passazhirzskiy_vagon != 0:
                return 'Ведущий вагон Тепловоз: {}. Грузовых вагонов: {}. Пассажирских вагонов: {}'.format(self.teplovoz, self.gruzovoy_vagon,
                                                                           self.passazhirzskiy_vagon)

            elif self.passazhirzskiy_vagon == 0 and self.gruzovoy_vagon != 0 and self.special_vagon != 0:
                return 'Ведущий вагон Тепловоз: {}. Почтовых вагонов: {}. грузовых вагонов: {}'.format(self.teplovoz, self.special_vagon,
                                                                           self.gruzovoy_vagon)

            elif self.gruzovoy_vagon != 0 and self.special_vagon != 0 and self.passazhirzskiy_vagon != 0:
                return 'Ведущий вагон Тепловоз: {}. Почтовых вагонов: {}. Пассажирских вагонов: {}. Грузовых вагонов: {}'.format(self.teplovoz, self.special_vagon,
                                                                           self.passazhirzskiy_vagon, self.gruzovoy_vagon)

            elif self.gruzovoy_vagon == 0 and self.passazhirzskiy_vagon == 0 and self.special_vagon != 0:
                return 'Ведущий вагон Тепловоз: {}. Почтовых вагонов: {}'.format(self.teplovoz, self.special_vagon)

            elif self.gruzovoy_vagon == 0 and self.special_vagon == 0 and self.passazhirzskiy_vagon != 0:
                return 'Ведущий вагон Тепловоз: {}. Пассажирских вагонов: {}'.format(self.teplovoz, self.passazhirzskiy_vagon)

            elif self.special_vagon == 0 and self.passazhirzskiy_vagon == 0 and self.gruzovoy_vagon != 0:
                return 'Ведущий вагон Тепловоз: {}. Грузовых вагонов: {}'.format(self.teplovoz, self.gruzovoy_vagon)

            elif self.special_vagon == 0 and self.passazhirzskiy_vagon == 0 and self.gruzovoy_vagon == 0:
                return 'Ведущий вагон Тепловоз: {}'.format(self.teplovoz)

        elif self.electrovoz > self.parovoz and self.electrovoz > self.teplovoz and self.electrovoz <=1:

            if self.gruzovoy_vagon == 0 and self.special_vagon != 0 and self.passazhirzskiy_vagon != 0:
                return 'Ведущий вагон Электровоз: {}. Почтовых вагонов: {}. Пассажирских вагонов: {}'.format(self.electrovoz, self.special_vagon,
                                                                           self.passazhirzskiy_vagon)

            elif self.special_vagon == 0 and self.gruzovoy_vagon != 0 and self.passazhirzskiy_vagon != 0:
                return 'Ведущий вагон Электровоз: {}. Грузовых вагонов: {}. Пассажирских вагонов: {}'.format(self.electrovoz, self.gruzovoy_vagon,
                                                                           self.passazhirzskiy_vagon)

            elif self.passazhirzskiy_vagon == 0 and self.gruzovoy_vagon != 0 and self.special_vagon != 0:
                return 'Ведущий вагон Электровоз: {}. Почтовых вагонов: {}. грузовых вагонов: {}'.format(self.electrovoz, self.special_vagon,
                                                                           self.gruzovoy_vagon)

            elif self.gruzovoy_vagon != 0 and self.special_vagon != 0 and self.passazhirzskiy_vagon != 0:
                return 'Ведущий вагон Электровоз: {}. Почтовых вагонов: {}. Пассажирских вагонов: {}. Грузовых вагонов: {}'.format(self.electrovoz, self.special_vagon,
                                                                           self.passazhirzskiy_vagon, self.gruzovoy_vagon)

            elif self.gruzovoy_vagon == 0 and self.passazhirzskiy_vagon == 0 and self.special_vagon != 0:
                return 'Ведущий вагон Электровоз: {}. Почтовых вагонов: {}'.format(self.electrovoz, self.special_vagon)

            elif self.gruzovoy_vagon == 0 and self.special_vagon == 0 and self.passazhirzskiy_vagon != 0:
                return 'Ведущий вагон Электровоз: {}. Пассажирских вагонов: {}'.format(self.electrovoz, self.passazhirzskiy_vagon)

            elif self.special_vagon == 0 and self.passazhirzskiy_vagon == 0 and self.gruzovoy_vagon != 0:
                return 'Ведущий вагон Электровоз: {}. Грузовых вагонов: {}'.format(self.electrovoz, self.gruzovoy_vagon)

            elif self.special_vagon == 0 and self.passazhirzskiy_vagon == 0 and self.gruzovoy_vagon == 0:
                return 'Ведущий вагон Электровоз: {}'.format(self.electrovoz)

        else:
            return "ОШИБКА: Неверно заданы параметры локомотива"




