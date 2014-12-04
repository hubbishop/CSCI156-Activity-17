__author__ = 'Dark-Knight'


class SS():
    class InvalidSocial(ValueError):
        pass

    def __init__(self):
        self.getsocial()

    def __str__(self):
        return self.ss

    def validatess(self):
        try:
            aaa, gg, ssss = self.ss.split('-')
        except ValueError:
            raise self.InvalidSocial
        if aaa == '078' and gg == '05' and ssss == '1120':
            raise self.InvalidSocial
        if len(aaa) != 3 or len(gg) != 2 or len(ssss) != 4:
            raise self.InvalidSocial
        if str(aaa) == '000' or str(gg) == '00' or str(ssss) == '0000':
            raise self.InvalidSocial
        try:
            aaa = int(aaa)
            gg = int(gg)
            ssss = int(ssss)
        except ValueError:
            raise self.InvalidSocial
        if 900 <= int(aaa) <= 999:
            raise self.InvalidSocial
        elif int(aaa) == 666:
            raise self.InvalidSocial
        else:
            return aaa, gg, ssss

    def getsocial(self):
        self.ss = input("aaa, gg, ssss: ")
        print(self.ss)
        try:
            self.validatess()
        except self.InvalidSocial:
            print("Invalid SS, please try again\n")
            self.getsocial()




