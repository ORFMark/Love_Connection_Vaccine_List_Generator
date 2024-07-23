from LCDR.UI.Colors import RGBColors
from LCDR.UI.Graphical.ScreenObjects.ScreenObject import ScreenObject


class TextDisplay(ScreenObject):

    def __init__(self, pygame, x,y, text=''):
        super().__init__()
        self.x = x;
        self.y = y;
        self.pygame = pygame
        self.FONT = pygame.font.Font(None, 32)
        self.text = self.FONT.render(text, True, RGBColors.BLACK.value)

    def handle_event(self, event):
        return
    def draw(self, screen):
        screen.blit(self.text, [self.x, self.y])