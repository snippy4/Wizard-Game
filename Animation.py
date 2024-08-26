class Animation:
    def __init__(self, images, img_dur=5, loop=True):
        self.images = images
        self.duration = img_dur
        self.loop = loop
        self.done = False
        self.frame = 0

    def copy(self):
        return Animation(self.images, self.duration, self.loop)
    
    def img(self):
        return self.images[int(self.frame / self.duration)]
    
    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (len(self.images) * self.duration)
        else:
            self.frame = min(self.frame + 1, len(self.images) * self.duration - 1)
            if self.frame >= self.duration * len(self.images) - 1:
                self.don = True
