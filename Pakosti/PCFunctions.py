from random import choice, randint
from pyautogui import *
import pygame
from os import system, path


class Pakosti:
    def __init__(self):
        self.list_pakosti = ['backspace', 'звук', 'картинка', 'статья', 'клавиши']
        self.words = ['Write!', 'Work!', 'You are BUSY?!', 'AAAAAAAAAAAAAAAAAAAAA!', 'Write! Write! write!']
        self.screen_size = size()
        pygame.mixer.init()

    def create_pacost(self, selected_pakosti=['backspace', 'звук', 'картинка', 'статья', 'клавиши']):
        pakost = choice(selected_pakosti)
        if pakost == 'backspace':
            press('backspace', presses=randint(1, 3), interval=0.5)
        elif pakost == 'кликает':
            x = randint(0, self.screen_size.width)
            y = randint(0, self.screen_size.height)
            click(x, y)
        elif pakost == 'звук':
            sound_id = str(randint(1, 3))
            print(sound_id)
            pygame.mixer.music.load(path.abspath(path.abspath(f'Pakosti\\sounds\\{sound_id}.mp3')))
            pygame.mixer.music.play()
        elif pakost == 'картинка':
            picture_id = str(randint(1, 4))
            system(path.abspath('start ' + path.abspath(f'Pakosti\\images//{picture_id}.jpg')))
        elif pakost == 'статья':
            system(path.abspath('start ' + path.abspath('Pakosti\\document.txt')))
        elif pakost == 'клавиши':
            print('text')
            write(choice(self.words), interval=0.1)
