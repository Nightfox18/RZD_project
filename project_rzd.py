import pygame
import pygame_menu as pm
import os
import locomotive
import button
import sys

os.environ['SDL_VIDEO_CENTERED'] = '1'

FPS = 60

pygame.init()

info = pygame.display.Info()  # You have to call this before pygame.display.set_mode()
screen_width, screen_height = info.current_w, info.current_h

# Screen
window_width, window_height = screen_width, screen_height
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

WIDTH = window_width
HEIGHT = window_height

# Standard RGB colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (190, 190, 190)
GRAY_BACK = (150, 150, 150)

# Окно создания элементов ( отрисовка и формирование экрана)
creating_screen = pygame.Rect((475, 375, WIDTH / 1.5, HEIGHT / 1.5))

font = pygame.font.SysFont("arialblack", 50)
font_class = pygame.font.SysFont("arialblack", 30)
font_class_OUTPUT = pygame.font.SysFont("arialblack", 25)
font_main = pygame.font.SysFont("arialblack", 40)

# Изображения для кнопок
locomotive_img = pygame.image.load('images/Локомотивы.png').convert_alpha()
Brigads_img = pygame.image.load('images/Бригады.png').convert_alpha()
Settings_img = pygame.image.load('images/Настройки.png').convert_alpha()
back_img = pygame.image.load('images/back.png').convert_alpha()
plus_element_img = pygame.image.load('images/i.png').convert_alpha()
minus_element_img = pygame.image.load('images/-.png').convert_alpha()
createlocomotive_img = pygame.image.load('images/Добавить_локомотив.png').convert_alpha()
createbrigad_img = pygame.image.load('images/Начальник_станции.png').convert_alpha()
save_img = pygame.image.load('images/save.png').convert_alpha()

# Кнопки
locomotive_button = button.Button(75, 70, locomotive_img, 1)
Brigads_button = button.Button(375, 70, Brigads_img, 1)
Settings_button = button.Button(625, 70, Settings_img, 1)
back_button = button.Button(900, 70, back_img, 1)
PLus_button = button.Button(WIDTH / 1.9, HEIGHT / 2.7, plus_element_img, 0.5)
Minus_button = button.Button(WIDTH / 2.1, HEIGHT / 2.7, minus_element_img, 1)
PLus1_button = button.Button(WIDTH / 1.9, HEIGHT / 2.4, plus_element_img, 0.5)
Minus1_button = button.Button(WIDTH / 2.1, HEIGHT / 2.4, minus_element_img, 1)
PLus2_button = button.Button(WIDTH / 1.9, HEIGHT / 2.15, plus_element_img, 0.5)
Minus2_button = button.Button(WIDTH / 2.1, HEIGHT / 2.15, minus_element_img, 1)
PLus3_button = button.Button(WIDTH / 1.9, HEIGHT / 1.95, plus_element_img, 0.5)
Minus3_button = button.Button(WIDTH / 2.1, HEIGHT / 1.95, minus_element_img, 1)
PLus4_button = button.Button(WIDTH / 1.9, HEIGHT / 1.75, plus_element_img, 0.5)
Minus4_button = button.Button(WIDTH / 2.1, HEIGHT / 1.75, minus_element_img, 1)
PLus5_button = button.Button(WIDTH / 1.9, HEIGHT / 1.6, plus_element_img, 0.5)
Minus5_button = button.Button(WIDTH / 2.1, HEIGHT / 1.6, minus_element_img, 1)
save_button = button.Button(525, HEIGHT / 1.2, save_img, 1)
createlocomotive_button = button.Button(WIDTH / 2.7, HEIGHT / 3, createlocomotive_img, 1)
createbrigad_button = button.Button(WIDTH / 2.5, HEIGHT / 3, createbrigad_img, 1)

pygame.display.update()


class Train(pygame.sprite.Sprite):

    def __init__(self, x, y, speed, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self, *args):
        self.rect.x += self.speed + args[0]
        if self.rect.left > WIDTH * 0.85:
            self.rect.right = WIDTH / 12 + 50

    def __del__(self):
        class_name = self.__class__.__name__
        print('{} уничтожен'.format(class_name))


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))


all_trains = pygame.sprite.Group()


def line_draw():
    height_for_line = HEIGHT / 3.64
    for i in range(0, 6):
        pygame.draw.line(window, BLACK, [WIDTH / 12, height_for_line], [WIDTH * 0.9, height_for_line], 3)
        height_for_line += 150
        i += 1


def station_maser():
    global height_for_train
    game_paused = True
    menu_state = "options"

    # Хранилище локомотивов и словарь с сохранением
    Locomotives = {}
    locomotive_count = 0

    # Ограничение количества выводимых локомотивов
    screen_limit = 0

    # Хранилище изображений локомотивов(TRAINS)
    Trains = {}
    trains_count = 0

    speed = 0

    run = True
    while run:
        clock.tick(FPS)

        # цикл обработки событий
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_paused = False
            if event.type == pygame.quit:
                main()
            pygame.display.update()

        window.fill(GRAY)

        # check if game is paused
        if game_paused == True:
            # check if the options menu is open

            if menu_state == "options":

                height_for_train = HEIGHT / 5
                width_for_train = WIDTH * 0.01

                line_draw()

                for key, train in Trains.items():
                    draw_text(f"ПУТЬ: {key} ", font_main, RED, width_for_train, height_for_train)

                    height_for_train += 150

                    all_trains.draw(window)
                    all_trains.update(speed)

                # Кнопки на экране
                if locomotive_button.draw(window):
                    menu_state = "Locomotive"
                if Brigads_button.draw(window):
                    menu_state = "Brigads"
                if Settings_button.draw(window):
                    menu_state = "settings"
                if back_button.draw(window):
                    main()
                if PLus_button.draw(window):
                    speed += 1

            if menu_state == "Locomotive":

                # все что будет находиться а экране
                pygame.draw.rect(window, WHITE, creating_screen)
                draw_text("Локомотивы", font, RED, WIDTH / 4.8, HEIGHT / 3.75)

                height_for_alltrains = HEIGHT / 3.9

                height_for_loco = HEIGHT / 2.7
                width_for_loco = WIDTH / 4.8
                height_for_button = HEIGHT / 3

                for key, loco in Locomotives.items():
                    if loco.parovoz == 0 and loco.electrovoz == 0 and loco.teplovoz == 0:
                        draw_text(f"Локомотив: {key}, ОШИБКА: Состав не может быть без ведущего вагона",
                                  font_class_OUTPUT, RED,
                                  width_for_loco, height_for_loco)


                    elif loco.parovoz > loco.teplovoz and loco.parovoz > loco.electrovoz and loco.parovoz <= 1:

                        if loco.gruzovoy_vagon == 0 and loco.special_vagon != 0 and loco.passazhirzskiy_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Паровоз: {loco.parovoz}. Специальных вагонов: {loco.special_vagon}. Пассажирских вагонов: {loco.passazhirzskiy_vagon}',
                                font_class_OUTPUT, RED,
                                width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 4.1, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/special_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/passanger_vagon1.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/passanger_vagon2.png'))

                        elif loco.special_vagon == 0 and loco.gruzovoy_vagon != 0 and loco.passazhirzskiy_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Паровоз: {loco.parovoz}. Грузовых вагонов: {loco.gruzovoy_vagon}. Пассажирских вагонов: {loco.passazhirzskiy_vagon}',
                                font_class_OUTPUT, RED,
                                width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 3.456, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 4.1, height_for_alltrains, 0, 'images/gruz_vagon.png'),
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/close_gruz_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/passanger_vagon1.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/passanger_vagon2.png'))

                        elif loco.passazhirzskiy_vagon == 0 and loco.special_vagon != 0 and loco.gruzovoy_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Паровоз: {loco.parovoz}. Специальных вагонов: {loco.special_vagon}. Грузовых вагонов: {loco.gruzovoy_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 4.1, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/gruz_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/close_gruz_vagon.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/special_vagon.png'))

                        elif loco.gruzovoy_vagon != 0 and loco.special_vagon != 0 and loco.passazhirzskiy_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Паровоз: {loco.parovoz}. Специальных вагонов: {loco.special_vagon}. Пассажирских вагонов: {loco.passazhirzskiy_vagon}. Грузовых вагонов: {loco.gruzovoy_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 2.98, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 3.456, height_for_alltrains, 0, 'images/gruz_vagon.png'),
                                Train(WIDTH / 4.1, height_for_alltrains, 0, 'images/close_gruz_vagon.png'),
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/special_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/passanger_vagon1.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/passanger_vagon2.png'))

                        elif loco.gruzovoy_vagon == 0 and loco.passazhirzskiy_vagon == 0 and loco.special_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Паровоз: {loco.parovoz}. Специальных вагонов: {loco.special_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/special_vagon.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/passanger_vagon1.png'))

                        elif loco.gruzovoy_vagon == 0 and loco.special_vagon == 0 and loco.passazhirzskiy_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Паровоз: {loco.parovoz}. Пассажирских вагонов: {loco.passazhirzskiy_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/passanger_vagon1.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/passanger_vagon2.png'))

                        elif loco.special_vagon == 0 and loco.passazhirzskiy_vagon == 0 and loco.gruzovoy_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Паровоз {loco.parovoz}. Грузовых вагонов: {loco.gruzovoy_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/gruz_vagon.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/close_gruz_vagon.png'))

                        elif loco.special_vagon == 0 and loco.passazhirzskiy_vagon == 0 and loco.gruzovoy_vagon == 0:
                            draw_text(f'Локомотив: {key}. Ведущий вагон Паровоз: {loco.parovoz}', font_class_OUTPUT,
                                      RED, width_for_loco,
                                      height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/main_vagon.png'))

                    elif loco.teplovoz > loco.parovoz and loco.teplovoz > loco.electrovoz and loco.teplovoz <= 1:

                        if loco.gruzovoy_vagon == 0 and loco.special_vagon != 0 and loco.passazhirzskiy_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Тепловоз: {loco.teplovoz}. Специальных вагонов: {loco.special_vagon}. Пассажирских вагонов: {loco.passazhirzskiy_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 4.1, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/special_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/passanger_vagon1.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/passanger_vagon2.png'))

                        elif loco.special_vagon == 0 and loco.gruzovoy_vagon != 0 and loco.passazhirzskiy_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Тепловоз: {loco.teplovoz}. Грузовых вагонов: {loco.gruzovoy_vagon}. Пассажирских вагонов: {loco.passazhirzskiy_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 3.456, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 4.1, height_for_alltrains, 0, 'images/gruz_vagon.png'),
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/close_gruz_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/passanger_vagon1.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/passanger_vagon2.png'))

                        elif loco.passazhirzskiy_vagon == 0 and loco.gruzovoy_vagon != 0 and loco.special_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Тепловоз: {loco.teplovoz}. Специальных вагонов: {loco.special_vagon}. Грузовых вагонов: {loco.gruzovoy_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 4.1, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/gruz_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/close_gruz_vagon.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/special_vagon.png'))

                        elif loco.gruzovoy_vagon != 0 and loco.special_vagon != 0 and loco.passazhirzskiy_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Тепловоз: {loco.teplovoz}. Специальных вагонов: {loco.special_vagon}. Пассажирских вагонов: {loco.passazhirzskiy_vagon}. Грузовых вагонов: {loco.gruzovoy_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 2.98, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 3.456, height_for_alltrains, 0, 'images/gruz_vagon.png'),
                                Train(WIDTH / 4.1, height_for_alltrains, 0, 'images/close_gruz_vagon.png'),
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/special_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/passanger_vagon1.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/passanger_vagon2.png'))

                        elif loco.gruzovoy_vagon == 0 and loco.passazhirzskiy_vagon == 0 and loco.special_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Тепловоз: {loco.teplovoz}. Специальных вагонов: {loco.special_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/special_vagon.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/passanger_vagon1.png'))

                        elif loco.gruzovoy_vagon == 0 and loco.special_vagon == 0 and loco.passazhirzskiy_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Тепловоз: {loco.teplovoz}. Пассажирских вагонов: {loco.passazhirzskiy_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/passanger_vagon1.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/passanger_vagon2.png'))

                        elif loco.special_vagon == 0 and loco.passazhirzskiy_vagon == 0 and loco.gruzovoy_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Тепловоз: {loco.teplovoz}. Грузовых вагонов: {loco.gruzovoy_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/gruz_vagon.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/close_gruz_vagon.png'))

                        elif loco.special_vagon == 0 and loco.passazhirzskiy_vagon == 0 and loco.gruzovoy_vagon == 0:
                            draw_text(f'Локомотив: {key}. Ведущий вагон Тепловоз: {loco.teplovoz}', font_class_OUTPUT,
                                      RED,
                                      width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/main_vagon.png'))

                    elif loco.electrovoz > loco.parovoz and loco.electrovoz > loco.teplovoz and loco.electrovoz <= 1:

                        if loco.gruzovoy_vagon == 0 and loco.special_vagon != 0 and loco.passazhirzskiy_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Электровоз: {loco.electrovoz}. Специальных вагонов: {loco.special_vagon}. Пассажирских вагонов: {loco.passazhirzskiy_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 4.1, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/special_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/passanger_vagon1.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/passanger_vagon2.png'))

                        elif loco.special_vagon == 0 and loco.gruzovoy_vagon != 0 and loco.passazhirzskiy_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Электровоз: {loco.electrovoz}. Грузовых вагонов: {loco.gruzovoy_vagon}. Пассажирских вагонов: {loco.passazhirzskiy_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 3.456, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 4.1, height_for_alltrains, 0, 'images/gruz_vagon.png'),
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/close_gruz_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/passanger_vagon1.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/passanger_vagon2.png'))

                        elif loco.passazhirzskiy_vagon == 0 and loco.gruzovoy_vagon != 0 and loco.special_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Электровоз: {loco.electrovoz}. Специальных вагонов: {loco.special_vagon}. Грузовых вагонов: {loco.gruzovoy_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 4.1, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/gruz_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/close_gruz_vagon.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/special_vagon.png'))

                        elif loco.gruzovoy_vagon != 0 and loco.special_vagon != 0 and loco.passazhirzskiy_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Электровоз: {loco.electrovoz}. Специальных вагонов: {loco.special_vagon}. Пассажирских вагонов: {loco.passazhirzskiy_vagon}. Грузовых вагонов: {loco.gruzovoy_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 2.98, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 3.456, height_for_alltrains, 0, 'images/gruz_vagon.png'),
                                Train(WIDTH / 4.1, height_for_alltrains, 0, 'images/close_gruz_vagon.png'),
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/special_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/passanger_vagon1.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/passanger_vagon2.png'))

                        elif loco.gruzovoy_vagon == 0 and loco.passazhirzskiy_vagon == 0 and loco.special_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Электровоз: {loco.electrovoz}. Специальных вагонов: {loco.special_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 12 + 297, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/special_vagon.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/passanger_vagon1.png'))

                        elif loco.gruzovoy_vagon == 0 and loco.special_vagon == 0 and loco.passazhirzskiy_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Электровоз: {loco.electrovoz}. Пассажирских вагонов: {loco.passazhirzskiy_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/passanger_vagon1.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/passanger_vagon2.png'))

                        elif loco.special_vagon == 0 and loco.passazhirzskiy_vagon == 0 and loco.gruzovoy_vagon != 0:
                            draw_text(
                                f'Локомотив: {key}. Ведущий вагон Электровоз: {loco.electrovoz}. Грузовых вагонов: {loco.gruzovoy_vagon}',
                                font_class_OUTPUT, RED, width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 12 + 295, height_for_alltrains, 0, 'images/main_vagon.png'),
                                Train(WIDTH / 12 + 177, height_for_alltrains, 0, 'images/gruz_vagon.png'),
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/close_gruz_vagon.png'))

                        elif loco.special_vagon == 0 and loco.passazhirzskiy_vagon == 0 and loco.gruzovoy_vagon == 0:
                            draw_text(f'Локомотив: {key}. Ведущий вагон Электровоз: {loco.electrovoz}',
                                      font_class_OUTPUT, RED,
                                      width_for_loco, height_for_loco)

                            Trains[trains_count] = all_trains.add(
                                Train(WIDTH / 12 + 50, height_for_alltrains, 0, 'images/main_vagon.png'))

                    else:
                        draw_text(f"Локомтоив: {key}. ОШИБКА: Неверно заданы параметры локомотива", font_class_OUTPUT,
                                  RED, width_for_loco, height_for_loco)

                    height_for_loco += 100
                    height_for_button += 110

                    height_for_alltrains += 150

                createlocomotive_button = button.Button(WIDTH / 2.3, height_for_button, createlocomotive_img, 1)

                # Кнопки на экране
                if locomotive_button.draw(window):
                    menu_state = "Locomotive"
                if Brigads_button.draw(window):
                    menu_state = "Brigads"
                if Settings_button.draw(window):
                    menu_state = "settings"
                if back_button.draw(window):
                    menu_state = "options"

                if screen_limit < 6:
                    if createlocomotive_button.draw(window):
                        menu_state = "create_locomotive"

                        trains_count += 1

                        locomotive_count += 1
                        Locomotives[locomotive_count] = locomotive.Locomotive(0, 0, 0, 0, 0, 0)

                        screen_limit += 1

            if menu_state == "create_locomotive":

                # все что будет находиться а экране
                pygame.draw.rect(window, WHITE, creating_screen)
                draw_text("Создание локомотива", font, RED, WIDTH / 4.8, HEIGHT / 3.75)

                creating_locomotive = Locomotives[locomotive_count]

                # Изменение параметров локомотива
                draw_text('Паровоз:                                                            {}'.format(
                    creating_locomotive.parovoz),
                          font_class, RED, WIDTH / 4.8,
                          HEIGHT / 2.7)

                draw_text('Электровоз:                                                       {}'.format(
                    creating_locomotive.electrovoz),
                          font_class, RED, WIDTH / 4.8,
                          HEIGHT / 2.4)

                draw_text('Теплоовоз:                                                         {}'.format(
                    creating_locomotive.teplovoz),
                          font_class, RED, WIDTH / 4.8,
                          HEIGHT / 2.15)

                draw_text('Грузовые вагоны:                                              {}'.format(
                    creating_locomotive.gruzovoy_vagon),
                          font_class, RED, WIDTH / 4.8,
                          HEIGHT / 1.95)

                draw_text('Специальные вагоны:                                       {}'.format(
                    creating_locomotive.special_vagon),
                          font_class, RED, WIDTH / 4.8,
                          HEIGHT / 1.75)

                draw_text('Пассажирские вагоны:                                     {}'.format(
                    creating_locomotive.passazhirzskiy_vagon),
                          font_class, RED, WIDTH / 4.8,
                          HEIGHT / 1.6)

                draw_text(creating_locomotive.errors_and_complte_of_a_locomotive(), font_class_OUTPUT, RED,
                          WIDTH / 4.8,
                          HEIGHT / 1.4)

                # Кнопки на экране
                if PLus_button.draw(window):
                    if creating_locomotive.parovoz <= 1:
                        creating_locomotive.parovoz += 1
                if Minus_button.draw(window):
                    if creating_locomotive.parovoz > 0:
                        creating_locomotive.parovoz -= 1

                if PLus1_button.draw(window):
                    if creating_locomotive.electrovoz <= 1:
                        creating_locomotive.electrovoz += 1
                if Minus1_button.draw(window):
                    if creating_locomotive.electrovoz > 0:
                        creating_locomotive.electrovoz -= 1

                if PLus2_button.draw(window):
                    if creating_locomotive.teplovoz <= 1:
                        creating_locomotive.teplovoz += 1
                if Minus2_button.draw(window):
                    if creating_locomotive.teplovoz > 0:
                        creating_locomotive.teplovoz -= 1

                if PLus3_button.draw(window):
                    if creating_locomotive.gruzovoy_vagon <= 20:
                        creating_locomotive.gruzovoy_vagon += 1
                if Minus3_button.draw(window):
                    if creating_locomotive.gruzovoy_vagon > 0:
                        creating_locomotive.gruzovoy_vagon -= 1

                if PLus4_button.draw(window):
                    if creating_locomotive.special_vagon <= 20:
                        creating_locomotive.special_vagon += 1
                if Minus4_button.draw(window):
                    if creating_locomotive.special_vagon > 0:
                        creating_locomotive.special_vagon -= 1

                if PLus5_button.draw(window):
                    if creating_locomotive.passazhirzskiy_vagon <= 20:
                        creating_locomotive.passazhirzskiy_vagon += 1
                if Minus5_button.draw(window):
                    if creating_locomotive.passazhirzskiy_vagon > 0:
                        creating_locomotive.passazhirzskiy_vagon -= 1

                if save_button.draw(window):
                    Locomotives[locomotive_count] = creating_locomotive
                    menu_state = "Locomotive"

            if menu_state == "Brigads":

                # все что будет находиться а экране
                pygame.draw.rect(window, WHITE, creating_screen)
                draw_text("Бригады", font, RED, WIDTH / 4.8, HEIGHT / 3.75)

                # Кнопки на экране
                if locomotive_button.draw(window):
                    menu_state = "Locomotive"
                if Brigads_button.draw(window):
                    menu_state = "Brigads"
                if Settings_button.draw(window):
                    menu_state = "settings"
                if back_button.draw(window):
                    menu_state = "options"

                if createbrigad_button.draw(window):
                    menu_state = "create_brigad"

            if menu_state == "create_brigad":

                # все что будет находиться а экране
                pygame.draw.rect(window, WHITE, creating_screen)

                draw_text("Состав бригады", font, RED, WIDTH / 4.8, HEIGHT / 3.75)
                draw_text('Всего локомотивов: %d' % locomotive.Locomotive.locomotive_count, font_class, RED,
                          WIDTH / 4.8, HEIGHT / 2)
                draw_text(locomotive.Locomotive1.errors_and_complte_of_a_locomotive(), font_class, RED, WIDTH / 4.8,
                          HEIGHT / 1.5)

                # Кнопки на экране
                if back_button.draw(window):
                    menu_state = "Brigads"

            if menu_state == "settings":

                # все что будет находиться а экране
                pygame.draw.rect(window, WHITE, creating_screen)
                draw_text("Настройки", font, RED, WIDTH / 4.8, HEIGHT / 3.75)

                # Кнопки на экране
                if locomotive_button.draw(window):
                    menu_state = "Locomotive"
                if Brigads_button.draw(window):
                    menu_state = "Brigads"
                if Settings_button.draw(window):
                    menu_state = "settings"
                if back_button.draw(window):
                    menu_state = "options"

        pygame.display.update()
    pygame.quit()


def main():
    # Creating the main menu
    mainMenu = pm.Menu(title="Главное меню",
                       width=WIDTH,
                       height=HEIGHT,
                       theme=pm.themes.THEME_DEFAULT)

    # Adjusting the default values
    mainMenu._theme.widget_alignment = pm.locals.ALIGN_CENTER

    mainMenu.add.label(title="Выберите роль для данной обучающей сессии", font_size=50)

    mainMenu.add.label(title="")

    # Кнопка Настройки, которая запускает окно настроек
    mainMenu.add.button(title="Начальник станции", action=station_maser,
                        font_color=WHITE, background_color=RED)

    # Пустая строка для разделения кнопок
    mainMenu.add.label(title="")

    mainMenu.add.button(title="Специалист локомотивной бригады", action=None,
                        font_color=WHITE, background_color=RED)

    # Пустая строка для разделения кнопок
    mainMenu.add.label(title="")

    # Кнопка выход, которая завершит выполнение программы
    mainMenu.add.button(title="ВЫХОД", action=pm.events.EXIT,
                        font_color=WHITE, background_color=RED)

    # вывод главного меню на экран
    mainMenu.mainloop(window)


if __name__ == "__main__":
    main()
