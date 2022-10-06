class MiniCalculator:

    def sum(self, a, b):
        return a+b

    def diff(self, a, b):
        return a-b

    def produs(self, a, b):
        return a*b

    def impartire(self, a, b):
        error_message = "Nu se poate imparti la 0"
        if b == 0:
            return error_message
        else:
            return a/b

