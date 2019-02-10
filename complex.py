class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        x = Complex(0, 0)
        x.r = self.r + other.r
        x.i = self.i + other.i
        return x

    def __sub__(self, other):
        x = Complex(0, 0)
        x.r = self.r - other.r
        x.i = self.i - other.i
        return x

    def __mul__(self, other):
        x = Complex(0, 0)
        x.r = self.r * other.r - (self.i * other.i)
        x.i = self.r * other.i + self.i * other.r
        return x

    def __truediv__(self, other):
        x = self * other.conjugate()
        d = float(other * other.conjugate())
        x.r /= d
        x.i /= d
        return x

    def reverse(self):
        return Complex(-self.r, -self.i)

    def conjugate(self):
        return Complex(self.r, -self.i)

    def size(self):
        return abs(self)

    def __abs__(self):
        return (self.r**2 + self.i**2)**(0.5)

    def __eq__(self, other):
        return self.r == other.r and self.i == other.i

    def __int__(self):
        return int(self.r)

    def __float__(self):
        return float(self.r)

    def __repr__(self):
        return f"C({self.r},{self.i})"

x = Complex(1,-2) 
y = Complex(3,7)
