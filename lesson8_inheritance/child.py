from inherit import Parent, Parent2


class Child1(Parent):
    def yow(self):
        print('Child1.yow')


class Child2(Parent):
    def spam(self):
        print('Child2.spam', self.value)


class Child3(Parent):
    def spam(self):
        print('Child2.spam', self.value)
        super().spam()


class Child4(Parent):
    def __init__(self, value, extra):
        self.extra = extra
        super().__init__(value)


class Child5(Parent, Parent2):
    pass
