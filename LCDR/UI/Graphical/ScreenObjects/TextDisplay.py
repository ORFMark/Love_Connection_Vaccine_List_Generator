from LCDR.UI.Colors import RGBColors
from LCDR.UI.Graphical.ScreenObjects.ScreenObject import ScreenObject


class TextDisplay(ScreenObject):

    def __init__(self, pygame, x,y, text=''):
        super().__init__()
        self.x = x;
        self.y = y;
        self.pygame = pygame
        self.FONT = pygame.font.Font(None, 32)
        self.text = text

    def handle_event(self, event):
        return
    def draw(self, screen):
        draw = self.FONT.render(self.text, True, RGBColors.BLACK.value)
        screen.blit(draw, [self.x, self.y])