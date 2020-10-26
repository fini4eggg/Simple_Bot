class SimpleRobot:
    
    def __init__(self):
        self.name = 'str'
        self.command = 'str'

    def get_name(self):
        return self.name

    def get_command(self):
        return self.command


class InfoBot(SimpleRobot):
    def __init__(self, name, command):
        super().__init__()
        self.name = name
        self.command = command

class FuckOffBot(SimpleRobot):
    def __init__(self, name, command):
        super().__init__()
        self.name = name
        self.command = command