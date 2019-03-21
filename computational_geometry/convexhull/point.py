class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __getitem__(self, i):
        return {0: self.x, 1: self.y}.get(i, None)

    @staticmethod
    def from_iter(tpl):
        return tpl if type(tpl) == Point else Point(tpl[0], tpl[1])
