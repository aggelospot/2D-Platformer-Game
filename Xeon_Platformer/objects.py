"""
Module for managing platforms.
"""
import pygame

from sprites import Sprites


STONE_PLATFORM_1 = (863, 383, 257, 33)
STONE_PLATFORM_2 = (800, 608, 320, 33)
DOUBLE_BOX = (1, 63, 63, 128)
MINI_BOX = (66, 160, 61, 32)
BUILDING1 = (0, 193, 234, 224)
BOX_STRIPPED = (575, 255, 96, 96)
OBSTACLE = (0, 192, 33, 223)
COIN_SILVER = (100, 0, 23, 19)
SPIKES_HORIZONTAL = (0, 84, 129, 84)
SPIKES_VERTICAL = (436, 0, 26, 129)
SCIBOX=(0,64,63,65)
COIN_SILVER = (100, 0, 23, 19)
HUGE_PLAT=(737,160,383,193)
LADDER=(234,189,40,216)
LAMP=(305,33,93,89)
TOWER=(736,3,288,349)
SPIKE=(1,331,28,38)
SPIKES_H=(0,95,129,16)
SPIKES_V=(438,161,9,125)

class Harmful(pygame.sprite.Sprite):

    def __init__(self, enemies):
        pygame.sprite.Sprite.__init__(self)
        enemy_list = Sprites("spikez.png")

        image = enemy_list.get_image(0, 0, 1, 1)
        color_switch = image.get_at((0, 0))

        self.image = enemy_list.get_image(enemies[0], enemies[1], enemies[2], enemies[3])
        self.image.set_colorkey(color_switch)

        self.rect = self.image.get_rect()

class Currency(pygame.sprite.Sprite):

    def __init__(self, coins):
        pygame.sprite.Sprite.__init__(self)
        coin_list = Sprites("coin_silver.png")

        image = coin_list.get_image(0, 0, 1, 1)
        color_switch = image.get_at((0, 0))

        self.image = coin_list.get_image(coins[0], coins[1], coins[2], coins[3])
        self.image.set_colorkey(color_switch)

        self.rect = self.image.get_rect()



class Platform(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = Sprites("scifi_platformTiles_32x32.png")

        self.image = sprite_sheet.get_image(sprite_sheet_data[0], sprite_sheet_data[1], sprite_sheet_data[2], sprite_sheet_data[3])

        self.rect = self.image.get_rect()


class MovingPlatform(Platform):
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way.  """

        self.rect.x += self.change_x

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:

            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right

        self.rect.y += self.change_y


        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:

            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom


        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
