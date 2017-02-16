from inherit import Parent, Parent2

# add method
class Child1(Parent):
    def yow(self):
        print('Child1.yow')

# override method
class Child2(Parent):
    def spam(self):
        print('Child2.spam', self.value)

# override method but call parent method as well
class Child3(Parent):
    def spam(self):
        print('Child2.spam', self.value)
        super().spam()

# override constructor (calling super() is a must)
class Child4(Parent):
    def __init__(self, value, extra):
        self.extra = extra
        super().__init__(value)


class Child5(Parent, Parent2):
    pass
