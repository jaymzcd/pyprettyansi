class AnsiColors(object):
    """ Defines the standard term codes for various colors and a number of
        methods to activate colors either via the class itself or an instance
        of it which is slightly configurable """

    color_prefix = '\033[%dm' # standard term code to open color sequence

    # Following dict holds the color codes for fb/bg and effects
    colors = {
        'fg': {
            'blue': 34,
            'yellow': 33,
            'red': 31,
            'green': 32,
            'cyan': 36,
            'white': 37,
        },
        'bg': {
            'blue': 44,
            'yellow': 43,
            'red': 41,
            'green': 42,
            'cyan': 46,
            'white': 47,
        },
    }

    def __init__(self, mode='fg'):
        self.mode = mode

    def set_color(self, color):
        return self.activate_color(color, self.mode)

    @staticmethod
    def activate_color(color, mode='fg'):
        """ You can use this method straight from the class rather than using
            an existing AnsiColors instance """
        print AnsiColors.color_prefix % (AnsiColors.colors[mode][color])

    @property
    def end(self):
        """ Terminate a given ansi color string sequence """
        print AnsiColors.color_prefix % 0,

    @staticmethod
    def reset():
        """ Helper method to terminate when colors set via activate_color """
        print AnsiColors.color_prefix % 0,

class AnsiPrettyPrint(object):
    """ A decorator that sets the given ansi terminal color for a passed
        functions output which is printed """

    def __init__(self, color, mode='fg'):
        self.color = color
        self.ansi = AnsiColors(mode=mode)

    def __call__(self, f):

        def wrapped_f(*args):
            self.ansi.set_color(self.color)
            f(*args)
            self.ansi.end

        return wrapped_f
