from abc import ABC, abstractmethod

gone_to_town = False

class Quest(ABC):
    def __init__(self, image, description, t):
        self.image = image
        self.description = description
        self.type = t
        self.state = None

    @abstractmethod
    def updateState(self):
        pass

class MainQuest(Quest):
    def updateState(self):
        if self.state == None:
            self.state = "welcome"
        if self.state == "welcome":
            if gone_to_town:
                self.state = "talk to jack"