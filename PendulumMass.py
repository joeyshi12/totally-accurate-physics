from math import *


class PendulumMass:
    theta: float
    omega: float
    origin: tuple
    length: float
    pos: tuple

    def __init__(self, theta, omega, origin, length):
        self.theta = theta
        self.omega = omega
        self.origin = origin
        self.length = length

    def update(self, dt, alpha):
        self.theta += self.omega * dt
        self.omega += alpha * dt

    def get_pos(self):
        x = self.length * sin(self.theta) + self.origin[0]
        y = self.length * cos(self.theta) + self.origin[1]
        return int(x), int(y)
