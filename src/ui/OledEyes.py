import os

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame
from PIL import Image
import board
import busio
import adafruit_ssd1306

from src.ui.RoboEyesLibrary import (
    RoboEyes,
    DEFAULT,
    HAPPY,
    TIRED,
    ANGRY,
)  # <- your class


class OledEyes:
    def __init__(self, width=128, height=64, addr=0x3C, fps=30):
        self.width = width
        self.height = height

        pygame.init()
        self.surface = pygame.Surface((width, height))

        self.eyes = RoboEyes(self.surface, width=width, height=height, frame_rate=fps)
        self.eyes.begin()

        self.eyes.setWidth(48, 48)
        self.eyes.setHeight(32, 32)
        self.eyes.setSpacebetween(10)
        self.eyes.setBorderradius(10, 10)

        self.eyes.setMood(DEFAULT)
        self.eyes.setAutoblinker(True, interval=2, variation=3)

        self.eyes.setIdleMode(True, interval=5, variation=5)

        self.eyes.setHFlicker(False)
        self.eyes.setVFlicker(False)

        i2c = busio.I2C(board.SCL, board.SDA)
        self.display = adafruit_ssd1306.SSD1306_I2C(width, height, i2c, addr=addr)
        self.display.fill(0)
        self.display.show()

    def tick(self):
        # update eyes into pygame surface (may or may not redraw depending on fps_timer)
        self.eyes.update()

        # push latest surface to OLED
        rgb = pygame.image.tostring(self.surface, "RGB")
        img = Image.frombytes("RGB", (self.width, self.height), rgb).convert("1")
        self.display.image(img)
        self.display.show()

    # convenience methods to drive expressions
    def set_happy(self):
        self.eyes.setMood(HAPPY)

    def set_tired(self):
        self.eyes.setMood(TIRED)

    def set_angry(self):
        self.eyes.setMood(ANGRY)

    def set_default(self):
        self.eyes.setMood(DEFAULT)

    def blink(self):
        self.eyes.blink()
