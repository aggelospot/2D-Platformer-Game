import pygame

import constants

from objects import MovingPlatform
from sprites import Sprites



class Player(pygame.sprite.Sprite):
    GREEN = (0, 255, 0)
    change_x = 0
    change_y = 0
    score = 0
    lost = False

    def play_coin_sound(self):
        coinz = pygame.mixer.Sound("coin_sound.wav")
        coinz.set_volume(0.1)
        coinz.play()

    def set_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def player_death(self):
        self.lost = True

    def get_status(self):
        return self.lost


    # Pinakes eikonwn
    walking_frames_l = []
    walking_frames_r = []

    direction = "R"

    level = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        sprites = Sprites("E:\Programming\Python\mygame\Xeonsheet.bmp")

        #Right side sprites
        image = sprites.get_image(17, 5, 45, 71)
        color_switch = image.get_at((0, 0))
        image.set_colorkey(color_switch)
        self.walking_frames_r.append(image)


        image = sprites.get_image(25, 170, 45, 71) #59,66
        color_switch = image.get_at((2, 2))
        image.set_colorkey(color_switch)
        self.walking_frames_r.append(image)

        image = sprites.get_image(103, 170, 45, 72)  #59,66
        color_switch = image.get_at((2, 2))
        image.set_colorkey(color_switch)
        self.walking_frames_r.append(image)


        # Left side sprites
        image = sprites.get_image(17, 5, 45, 72)
        image.set_colorkey(color_switch)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprites.get_image(25, 170, 55, 71)  # 59,66
        color_switch = image.get_at((2, 2))
        image.set_colorkey(color_switch)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprites.get_image(103, 170, 55, 72)  # 59,66
        color_switch = image.get_at((2, 2))
        image.set_colorkey(color_switch)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        # Arxiko sprite

        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()




    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()


        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift

        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]


        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        coin_hit_list = pygame.sprite.spritecollide(self, self.level.coin_list, True)
        enemy_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)

        if enemy_hit_list:
            self.player_death()


        if coin_hit_list:
            self.set_score()
            self.play_coin_sound()



        for block in block_hit_list:

            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom


            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35


        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
            self.image = self.walking_frames_r[0]

    def jump(self):

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10
            self.walking_frames_r[0]

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.image = self.walking_frames_r[0]
        self.change_x = 0


