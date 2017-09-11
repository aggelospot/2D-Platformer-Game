import pygame
import constants
import levels

from PlayerCharacter import Player

def playsoundtrack():
    soundtrack = pygame.mixer.Sound("Deus_ex.wav")
    soundtrack.set_volume(0.1)
    soundtrack.play()


def main():
    pygame.init()

    playsoundtrack()
    size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Xeon Platformer")

    pc = Player()

    level_list = []
    level_list.append(levels.Level_01(pc))
    level_list.append(levels.Level_02(pc))

    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()

    pc.level = current_level

    pc.rect.x = 340
    pc.rect.y = constants.SCREEN_HEIGHT - pc.rect.height

    active_sprite_list.add(pc)

    end = False
    won = False

    font = pygame.font.Font(None, 40)
    textlost = font.render("YOU LOST", 1, (255, 255, 255))
    textwon = font.render("YOU WIN!", 1, (255, 255, 255))
    textwon2 = font.render("All coins collected!", 1, (255, 255, 255))

    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN and end == False:
                if event.key == pygame.K_LEFT:
                    pc.go_left()
                if event.key == pygame.K_RIGHT:
                    pc.go_right()
                if event.key == pygame.K_UP:
                    pc.jump()
                if event.key == pygame.K_F1:
                    end = True
                    won = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and pc.change_x < 0:
                    pc.stop()
                if event.key == pygame.K_RIGHT and pc.change_x > 0:
                    pc.stop()

        active_sprite_list.update()

        current_level.update()

        if pc.rect.x >= 500:
            diff = pc.rect.x - 500
            pc.rect.x = 500
            current_level.shift_world(-diff)

        if pc.rect.x <= 120:
            diff = 120 - pc.rect.x
            pc.rect.x = 120
            current_level.shift_world(diff)

        current_position = pc.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            if current_level_no < len(level_list)-1:
                pc.rect.x = 120
                current_level_no += 1
                current_level = level_list[current_level_no]
                pc.level = current_level
            elif current_level_no == 1:
                won = True



        # Draw
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        score = pc.get_score()
        score_conv = str(score)
        score_text = font.render(score_conv, 1, (255,255,255))



        if pc.get_status() == False:
            if won == False:
                screen.blit(score_text, (750, 550))
            else:
                if pc.get_score() == 13:
                    screen.blit(textwon2, (300, 300))
                screen.blit(textwon, (360, 250))
                screen.blit(score_text, (420, 350))
                end = True

        else:
            end = True
            screen.blit(score_text, (380, 300))
            screen.blit(textlost, (300, 250))


        clock.tick(60)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
