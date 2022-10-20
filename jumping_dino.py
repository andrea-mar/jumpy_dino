import sys
import pygame


def main():
    # initializes available pygame modules
    pygame.init()
    pygame.font.init()

    size = width, height = 600, 240
    speed_cactus = [-2, 0]  # [x, y]

    blue = 0, 0, 225
    green = 0, 255, 0
    white = 255, 255, 255
    points = 0
    v = 6
    m = 2
    is_jump = True

    # create a graphical window with a given width and height
    screen = pygame.display.set_mode(size)

    # create display for points
    points_font = pygame.font.SysFont("Comic Sans MS", 30)
    points_surface = points_font.render(f"Points: {points}", False, white)

    # create display for game over message
    message_font = pygame.font.SysFont("Comic Sans", 30)
    message_surface = message_font.render("", False, white)

    # cactus initial position
    cactus = pygame.image.load("cactus.png")
    cactus = pygame.transform.scale(cactus, (50, 70))
    cactusrect = cactus.get_rect(topleft=(width, height - 80))

    # dino initial position
    dino = pygame.image.load("dino.png")
    dino = pygame.transform.scale(dino, (100, 100))
    dinorect = dino.get_rect(top=height - 110)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # move cactus from rigth to left
        cactusrect = cactusrect.move(speed_cactus)
        if cactusrect.left < 0:
            cactusrect.right = width
            points = points + 1
            points_surface = points_font.render(f"Points: {points}", False, white)

        # stop the game if dino touches the cactus
        if pygame.Rect.colliderect(cactusrect, dinorect) == True:
            speed_cactus = [0, 0]
            message_surface = message_font.render("Game Over", False, white)

        # move dino up and down using the space bar
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            is_jump, v, m, dinorect.y = jump(is_jump, v, m, dinorect.y)
    
        #     dinorect.y -= 4  # dinorect.move(speed_dino_up)
        # if dinorect.top < height - 110:
        #     dinorect.y += 2  # dinorect.move(speed_dino_down)
        # if dinorect.top < 0:
        #     dinorect.y += 110  # prevents dino from going off screen

        screen.fill(blue)
        pygame.draw.rect(screen, green, pygame.Rect(0, height - 15, width, 15))
        screen.blit(points_surface, (5, 0))
        screen.blit(message_surface, (width / 2 - 70, height / 2 - 30))
        screen.blit(cactus, cactusrect)
        screen.blit(dino, dinorect)
        pygame.display.flip()


def jump(bool, v, m, y):
    if bool == True:
        if v > 0:
            F = 10 #0.5 * m * (v*v)
        else:
            F = -10#(0.5 * m * (v*v))
        y = y - F
        v = v - 1
        if y >= 130:
            y = 130
            bool = False
            v = 8
    else:
        bool = True
    return (bool, v, m, y)
        
        

if __name__ == "__main__":
    main()
