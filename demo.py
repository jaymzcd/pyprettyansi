from pyprettyansi.prettyansi import AnsiPrettyPrint, AnsiColors

@AnsiPrettyPrint('blue', mode='bg')
def printstuff():
    print "hey there"

@AnsiPrettyPrint('yellow', bold=True)
def morethings():
    print "i should be yellow"
    x = range(1, 20)
    AnsiColors.activate_color('blue', mode='bg')
    for i in x:
        print i

printstuff()
morethings()

AnsiColors.activate_color('yellow', mode='bg')
AnsiColors.activate_color('red', mode='fg')
print "hey there"

AnsiColors.reset()


print "I come after"