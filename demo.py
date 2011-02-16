from pyprettyansi.prettyansi import AnsiPrettyPrint, AnsiColors

@AnsiPrettyPrint('blue')
def printstuff():
    print "hey there"

@AnsiPrettyPrint('yellow')
def morethings():
    print "i should be yellow"

printstuff()
morethings()
print "I come after"