import src.myconstants as myconstants

class Background:
    def __init__(self, window_width, window_height):
        self.width = window_width
        self.height = window_height
        self.x = 0
        self.y = 0
        self.speed = myconstants.BACKGROUND_SPEED
        self.color = myconstants.WHITE

    def update(self):
        self.x -= self.speed
        if self.x <= -self.width:
            self.x = 0