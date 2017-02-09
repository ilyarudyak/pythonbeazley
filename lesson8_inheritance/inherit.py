class Parent(object):
    def __init__(self, value):
        self.value = value

    def spam(self):
        print('Parent.spam', self.value)

    def grok(self):
        print('parent.grok')
        self.spam()


class Parent2(object):
    def yow(self):
        print('Parent2.yow')
