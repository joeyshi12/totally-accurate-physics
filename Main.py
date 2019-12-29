from PendulumMass import *
import pygame

pygame.init()

clock = pygame.time.Clock()
display_width = 800
display_height = 500
display = pygame.display.set_mode((display_width, display_height))


m1 = PendulumMass(1, 0, (int(display_width / 2), int(display_height / 2)), 100)
m2 = PendulumMass(1, 0, m1.get_pos(), 100)
dt = 0.02
g = 10


def draw_mass(m: PendulumMass):
    pygame.draw.line(display, (0, 0, 0), m.origin, m.get_pos())
    pygame.draw.circle(display, (255, 0, 0), m.get_pos(), 10)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.fill((255, 255, 255))
        alpha1 = (-3 * g * sin(m1.theta) - g * sin(m1.theta - 2 * m2.theta) - 2 * sin(m1.theta - m2.theta) * (m2.omega ** 2 * m2.length - m1.omega ** 2 * m1.length * cos(m1.theta - m2.theta))) \
                 / (m1.length * (3 - cos(2 * m1.theta - 2 * m2.theta)))
        m1.update(dt, alpha1)
        alpha2 = (2 * sin(m1.theta - m2.theta) * (m1.omega ** 2 * m1.length * 2 + g * 2 * cos(m1.theta) + m2.omega ** 2 * m2.length * cos(m1.theta - m2.theta))) \
                 / (m2.length * (3 - cos(2 * m1.theta - 2 * m2.theta)))
        m2.update(dt, alpha2)
        draw_mass(m1)
        draw_mass(m2)
        m2.origin = m1.get_pos()
        pygame.display.update()
        clock.tick(1000)


if __name__ == '__main__':
    main()
