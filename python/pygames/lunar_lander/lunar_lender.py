import pygame, sys

pygame.init()

screen = pygame.display.set_mode([430, 720])
screen.fill([0, 0, 0])
ship = pygame.image.load('lunarlander.png')
moon = pygame.image.load('moonsurface.png')
ground = 660
start = 90

# Music
pygame.mixer.init()
pygame.mixer.music.load("lander.mp3")
pygame.mixer.music.set_volume(0.88)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

ship_mass = 5000.0
fuel = 5000.0
velocity = -100.0
gravity = 10
height = 2000
thrust = 0
delta_v = 0
y_pos = 90
held_down = False



class ThrottleClass(pygame.sprite.Sprite):
    def __init__(self, location = [0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([30, 10])
        image_surface.fill([128, 128, 128])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.centery = location


def calculate_velocity():
    global thrust, fuel, velocity, delta_v, height, y_pos, fps
    delta_t = 1 / fps
    thrust = (500 - myThrottle.rect.centery) * 5.0
    fuel -= thrust / (10 * fps)
    if fuel < 0:
        fuel = 0.0
    if fuel < 0.1:
        thrust = 0.0
    delta_v = delta_t * (-gravity + 200 * thrust / (ship_mass + fuel))
    velocity = velocity + delta_v
    delta_h = velocity * delta_t
    height = height + delta_h
    y_pos = ground - (height * (ground - start) / 2000) - 90


def display_stats():
    v_str = "velocity: %i m/s" % velocity
    h_str = "height: %.1f" % height
    t_str = "thrust: %i" % thrust
    a_str = "acceleration: %.1f" % (delta_v * fps)
    f_str = "fuel: %i" % fuel

    v_font = pygame.font.Font(None, 26)
    v_surf = v_font.render(v_str, 1, (255, 255, 255))
    screen.blit(v_surf, [10, 50])
    h_font = pygame.font.Font(None, 26)
    h_surf = h_font.render(h_str, 1, (255, 255, 255))
    screen.blit(h_surf, [10, 120])
    t_font = pygame.font.Font(None, 26)
    t_surf = t_font.render(t_str, 1, (255, 255, 255))
    screen.blit(t_surf, [10, 180])
    a_font = pygame.font.Font(None, 26)
    a_surf = a_font.render(a_str, 1, (255, 255, 255))
    screen.blit(a_surf, [10, 250])
    f_font = pygame.font.Font(None, 26)
    f_surf = f_font.render(f_str, 1, (255, 255, 255))
    screen.blit(f_surf, [60, 375])


def display_flames():
    flame_size = thrust / 15
    for i in range(2):
        startx = 252 - 10 + i * 19
        starty = y_pos + 83
        pygame.draw.polygon(screen, [255, 109, 14], [(startx, starty),
            (startx + 4, starty + flame_size),
            (startx + 8, starty)], 0)

def display_final():
    final1 = "Game is Finished!"
    final2 = "Speed of landing %.1f m/s" % velocity
    if velocity > -5:
        final3 = "Great Landing!"
        final4 = "I've heard NASA looking for a new talents!"
    if velocity > -15:
        final3 = "Tuff touching. But we've survived. This is good."
        final4 = "Next time you'll be better, i believe!"
    else:
        final3 = "God Damn! You smashed the 30-million $ Ship."
        final4 = "And.. How do you like to fly home?"
    pygame.draw.rect(screen, [0, 0, 0], [5, 5, 350, 280], 0)

    f1_font = pygame.font.Font(None, 70)
    f1_surf = f1_font.render(final1, 1, (255, 255, 255))
    screen.blit(f1_surf, [20, 50])
    f2_font = pygame.font.Font(None, 40)
    f2_surf = f2_font.render(final2, 1, (255, 255, 255))
    screen.blit(f2_surf, [20, 140])
    f3_font = pygame.font.Font(None, 26)
    f3_surf = f3_font.render(final3, 1, (255, 255, 255))
    screen.blit(f3_surf, [20, 200])
    f4_font = pygame.font.Font(None, 26)
    f4_surf = f4_font.render(final4, 1, (255, 255, 255))
    screen.blit(f4_surf, [20, 250])
    pygame.display.flip()


myThrottle = ThrottleClass([15, 500])
running  = True

while running:
    clock.tick(30)
    fps = clock.get_fps()
    if fps < 1:
        fps = 30
    if height > 0.01:
        calculate_velocity()
        screen.fill([0, 0, 0])
        display_stats()
        pygame.draw.rect(screen, [0, 0, 255], [80, 420, 24, 100], 2)
        fuelbar = 96 * fuel / 5000
        pygame.draw.rect(screen, [0, 255, 0], [84, 538-fuelbar, 18, fuelbar], 0)
        pygame.draw.rect(screen, [255, 0, 0], [25, 360, 10, 200], 0)
        screen.blit(moon, [0, 600, 400, 100])
        pygame.draw.rect(screen, [60, 60, 60], [220, 645, 70, 5], 0)
        screen.blit(myThrottle.image, myThrottle.rect)
        display_flames()
        screen.blit(ship, [230, y_pos, 50, 90])
        instruct1 = "Landing carefully, don't run out of fuel!"
        instruct2 = "Tip: < 15 m/s - good landing; < 5 m/s - great landing!"
        inst1_font = pygame.font.Font(None, 24)
        inst1_surf = inst1_font.render(instruct1, 1, (255, 255, 255))
        screen.blit(inst1_surf, [50, 660])
        inst2_font = pygame.font.Font(None, 24)
        inst2_surf = inst2_font.render(instruct2, 1, (255, 255, 255))
        screen.blit(inst2_surf, [50, 695])
        pygame.display.flip()

    else:
        display_final()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            held_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            held_down = False
        elif event.type == pygame.MOUSEMOTION:
            if held_down:
                myThrottle.rect.centery = event.pos[1]
                if myThrottle.rect.centery < 300:
                    myThrottle.rect.centery = 300
                if myThrottle.rect.centery > 500:
                    myThrottle.rect.centery = 500

pygame.quit()
