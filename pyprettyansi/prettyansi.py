class AnsiColors(object):
    color_prefix = '\033[%dm'
    colors = {
        'fg': {
            'blue': 34,
            'yellow': 33,
        },
        'bg': {
            'blue': 44,
            'yellow': 43,
        },
    }

    def __init__(self, mode='fg'):
        self.mode = mode

    def set_color(self, color):
        print self.color_prefix % self.colors[self.mode][color],

    @property
    def end(self):
        print self.color_prefix % 0,

class AnsiPrettyPrint(object):

    def __init__(self, color):
        self.color = color
        self.ansi = AnsiColors()

    def __call__(self, f):

        def wrapped_f(*args):
            self.ansi.set_color(self.color)
            f(*args)
            self.ansi.end

        return wrapped_f
