class AnsiColors(object):
    color_prefix = '\033[%dm'
    colors = {
        'fg': {
            'blue': 34,
            'yellow': 33,
        },
        'bg': {
            'blue': 44,
            'blue': 43,
        },
    }

    def __getattr__(self, attr):
        print colors % (gettattr(self, attr))


class AnsiPrettyPrint(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print AnsiColors.colors['bg']['blue']
        self.f()
