import pygame

import constants
import objects

class Level():

    platform_list = None
    enemy_list = None
    coin_list = None

    background = None

    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.coin_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
        self.coin_list.update()

    def draw(self, screen):
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.coin_list.draw(screen)

    def shift_world(self, shift_x):

        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for coin in self.coin_list:
            coin.rect.x += shift_x

class Level_01(Level):


    def __init__(self, player):

        Level.__init__(self, player)

        self.background = pygame.image.load("background1-720.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1300

        level = [ [objects.BUILDING1, 0, 380],
            [objects.STONE_PLATFORM_2, 700, 280],
            [objects.STONE_PLATFORM_1, 210, 400],
            [objects.BOX_STRIPPED, 0, 285], [objects.BOX_STRIPPED, 0, 198], [objects.OBSTACLE, -35, 379],
            [objects.OBSTACLE, -35, 160], [objects.OBSTACLE, -35, 2],
            [objects.STONE_PLATFORM_1, 1000, 670],
            [objects.SCIBOX, 720, 214],
            [objects.HUGE_PLAT, 1000, 407],
            [objects.HUGE_PLAT, 1868, 407],
            [objects.SCIBOX, 750, 533],
            [objects.OBSTACLE, 2500, 379],
            [objects.OBSTACLE, 2500, 160], [objects.OBSTACLE, 2500, 2],
            [objects.LADDER, 2450, 400] ]


        enemies = [[objects.SPIKES_HORIZONTAL, 870, 580], [objects.SPIKES_HORIZONTAL, 820, 580],
                   [objects.SPIKES_HORIZONTAL, 1380, 580], [objects.SPIKES_HORIZONTAL, 1500, 580],
                   [objects.SPIKES_HORIZONTAL, 1620, 580], [objects.SPIKES_HORIZONTAL, 1740, 580]]

        level_coin = [[objects.COIN_SILVER, 120, 140], [objects.COIN_SILVER, 120, 160], [objects.COIN_SILVER, 720, 100],
                      [objects.COIN_SILVER, 700, 550], [objects.COIN_SILVER, 900, 450],
                      [objects.COIN_SILVER, 1600, 150], [objects.COIN_SILVER, 1700, 150],
                      [objects.COIN_SILVER, 1800, 150]]

        for enemy in enemies:
            block = objects.Harmful(enemy[0])
            block.rect.x = enemy[1]
            block.rect.y = enemy[2]
            block.player = self.player
            self.enemy_list.add(block)


        for platform in level:
            block = objects.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for coin in level_coin:
            block = objects.Currency(coin[0])
            block.rect.x = coin[1]
            block.rect.y = coin[2]
            block.player = self.player
            self.coin_list.add(block)

        block = objects.MovingPlatform(objects.STONE_PLATFORM_1)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


class Level_02(Level):

    def __init__(self, player):

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background3-720.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1200

        # Array with type of platform, and x, y location of the platform.
        level = [ [objects.BUILDING1, -200, 380],[objects.OBSTACLE, -210, 379],
            [objects.OBSTACLE, -110, 160], [objects.OBSTACLE, -110, 2],
                   [objects.OBSTACLE, 100, 2],
                  [objects.STONE_PLATFORM_1, 230, 450],
                  [objects.DOUBLE_BOX, 391, 322],
                  [objects.TOWER,548,250],
                  [objects.BOX_STRIPPED,690,153],
                  [objects.STONE_PLATFORM_2,540,-23],
                  [objects.STONE_PLATFORM_1, 1030, 340],

                  [objects.STONE_PLATFORM_2, 940, -23],
                  [objects.SCIBOX,1130,277],

                  [objects.STONE_PLATFORM_2, 1440, 0],

                  [objects.HUGE_PLAT,1850,6],
                  [objects.TOWER, 1850, 350],
                  [objects.HUGE_PLAT, 2232, 6],[objects.HUGE_PLAT, 2614, 6],
                  [objects.TOWER, 2138, 350],[objects.TOWER, 2426, 350]


                  ]


        enemies = [[objects.SPIKES_H, 699, 9],[objects.SPIKES_H, 659,9]
            ,[objects.SPIKES_H, 539, 9],[objects.SPIKE, 870, 580],[objects.SPIKES_V, 538, 500], [objects.SPIKES_H, -30, 180]
            ,[objects.SPIKES_V, 538, 380],[objects.SPIKES_V, 538, 250],[objects.LAMP,1060,12],
                   [objects.SPIKES_H, 1862, 198],[objects.SPIKES_H, 1440, 33],[objects.SPIKE, 1570, 30],
                   [objects.SPIKE, 1598, 30],[objects.SPIKES_H, 1625, 33],
                   [objects.SPIKES_HORIZONTAL, 1380, 585], [objects.SPIKES_HORIZONTAL, 1500, 585],
                   [objects.SPIKES_HORIZONTAL, 1620, 585], [objects.SPIKES_HORIZONTAL, 1730, 585], [objects.SPIKES_HORIZONTAL, 920, 585],
                   [objects.SPIKES_HORIZONTAL, 1160, 585]
                   ]


        level_coin = [ [objects.COIN_SILVER,70,20],[objects.COIN_SILVER,70,40],[objects.COIN_SILVER,70,60],[objects.COIN_SILVER,70,80],
        [objects.COIN_SILVER, 70, 100], [objects.COIN_SILVER, 70, 120], [objects.COIN_SILVER, 70, 140],[objects.COIN_SILVER, 70, 160],

                       [objects.COIN_SILVER, 30, 20], [objects.COIN_SILVER, 30, 40], [objects.COIN_SILVER, 30, 60],
                       [objects.COIN_SILVER, 30, 80],
                       [objects.COIN_SILVER, 30, 100], [objects.COIN_SILVER, 30, 120], [objects.COIN_SILVER, 30, 140],
                       [objects.COIN_SILVER, 30, 160],

                       [objects.COIN_SILVER, 1000,40],[objects.COIN_SILVER, 1180,40],[objects.COIN_SILVER, 1587,74],
                       [objects.COIN_SILVER, 1325, 470],[objects.COIN_SILVER, 1120, 470]
                       ]

        for enemy in enemies:
            block = objects.Harmful(enemy[0])
            block.rect.x = enemy[1]
            block.rect.y = enemy[2]
            block.player = self.player
            self.enemy_list.add(block)

        for platform in level:
            block = objects.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for coin in level_coin:
            block = objects.Currency(coin[0])
            block.rect.x = coin[1]
            block.rect.y = coin[2]
            block.player = self.player
            self.coin_list.add(block)

        # Add a custom moving platform
        block = objects.MovingPlatform(objects.STONE_PLATFORM_1)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


