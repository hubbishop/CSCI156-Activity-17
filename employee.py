__author__ = 'Dark-Knight'
from SS import *


class Employee:
    def __init__(self, last=None, first=None, start=None, pay_rate=None, social=None):
        if (last is None) and (first is None) and (start is None) and (pay_rate is None) and (social is None):
            self.last = input("Input last name:").capitalize()
            self.first = input("Input first name:").capitalize()
            self.start = input("Input start year:")
            self.pay_rate = float(input("Input pay_rate:"))
            self.social = SS()
        else:
            self.last = last.capitalize()
            self.first = first.capitalize()
            self.start = start
            self.pay_rate = pay_rate
            self.social = social

    def __str__(self):
        return 'Employee' + ' ' + self.last + ' ' + self.first + ' ' + ' began working in the year' + ' ' + self.start + ' '+ 'makes' + ' ' + str(self.pay_rate) + ' '+ 'an hour' +\
        ' ' + ' and the social security number is' + ' ' + str(self.social)
