__author__ = 'xinli'

from poplib import POP3

p = POP3('pop.python.is.cool')
p.user("techNstuff4U")
p.pass_("youllNeverGuess")
p.stat()


