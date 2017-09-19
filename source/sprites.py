import pygame

class Alien:
    def __init__(self, starting_position_x, starting_position_y, file_location):
        self.__x_position = starting_position_x
        self.__y_position = starting_position_y
        self.__x_change = 0
        self.__y_change = 0
        self.__character = pygame.image.load(file_location)

    def draw(self, game_display):
        self.__x_position += self.__x_change
        self.__y_position += self.__y_change
        game_display.blit(self.__character,
            (self.__x_position, self.__y_position)
        )

    def get_x_position(self):
        return self.__x_position

    def get_y_position(self):
        return self.__y_position

    def set_x_position(self, x):
        self.__x_position = x

    def set_y_position(self, y):
        self.__y_position = y

    def set_x_change(self, change):
        self.__x_change = change

    def set_y_change(self, change):
        self.__y_change = change


class Laser:
    def __init__(self, starting_position_x, starting_position_y, file_location):
        self.__x_position = starting_position_x
        self.__y_position = starting_position_y
        self.__x_change = 0
        self.__laser = pygame.image.load(file_location)

    def draw(self, game_display):
        self.__x_position += self.__x_change
        game_display.blit(self.__laser, 
            (self.__x_position, self.__y_position)    
        )


    def set_x_change(self, change):
        self.__x_change = change

    def set_x_position(self, x):
        self.__x_position = x

    def set_y_position(self, y):
        self.__y_position = y


