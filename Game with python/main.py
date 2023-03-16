import pygame
import time 
import random
pygame.font.init()


Width, Heigth = 1000, 800
WIN = pygame.display.set_mode((Width,Heigth))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("milk.jpg"),(Width,Heigth))

Player_Width = 40
Player_height = 60

Player_vel = 5

Font = pygame.font.SysFont("comicsans",30)

Star_width = 10
Star_height = 20
Star_vel = 3

def draw(player,elapsed_time,stars):
    WIN.blit(BG,(0,0))

    time_text = Font.render(f"Time: {round(elapsed_time)}s",1,"white")
    WIN.blit(time_text,(10,10))

    pygame.draw.rect(WIN,(255,0,0),player)

    for star in stars:
        pygame.draw.rect(WIN,"white",star)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200,Heigth - Player_height,Player_Width,Player_height)

    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)

        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0,Width - Star_width)
                star = pygame.Rect(star_x, -Star_height,Star_width,Star_height)
                stars.append(star)
            star_add_increment = max(200,star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - Player_vel >= 0:
            player.x -= Player_vel
        if keys[pygame.K_RIGHT] and player.x + Player_vel + Player_Width <= Width:
            player.x += Player_vel

        for star in stars[:]:
            star.y += Star_vel
            if star.y > Heigth:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = Font.render("You Lost!",1,"white")
            WIN.blit(lost_text, (Width/2 - lost_text.get_width()/2 , Heigth/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)

    pygame.quit()

if __name__ == "__main__":
    main()