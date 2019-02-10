class Matrix:
  def __init__(self, *args, **kwargs):
    if len(args) > 0:
      if isinstance(args[0], Matrix):
        m = args[0].copy()
    else:
      m = {'vals': [], 'w': 0, 'h': 0}

    self.vals = m.vals
    self.w = m.w
    self.h = m.h

  def copy(self):
    new_m = Matrix()
    for i in self.vals:
      new_m.vals.append(i)
    new_m.w = self.w
    new_m.h = self.h
    return new_m


  @property
  def width(self):
    return self.w


  @property
  def height(self):
    return self.h


  def value_at(self, row, col):
    return self.vals[row*self.w + col]


  def at(self, row, col):
    return self.value_at(row, col)


  def row(self, pos):
    return [self.vals[pos*self.w + i] for i in range(self.w)]


  @property
  def rows(self):
    return [self.row(i) for i in range(self.h)]
  

  def col(self, pos):
    return [self.vals[i*self.w + pos] for i in range(self.h)]


  @property
  def cols(self):
    return [self.col(i) for i in range(self.w)]
  

  @staticmethod
  def _isnumeric(i):
    return isinstance(i, float) or isinstance(i, int)


  def _add(self, r, p, q, *args):
    r = len(args) if r <= 0 else r
    for i in range(r):
      try:
        if self._isnumeric(args[i]):
          self.vals.insert(i*(p + 1) + self.w*q, args[i])
      except IndexError:
        self.vals.insert(i*(p + 1) + self.w*q, 0)
    return r


  def addrow(self, *args):
    self.w = self._add(self.w, 0, self.h, *args)
    self.h += 1


  def addcol(self, *args):
    self.h = self._add(self.h, self.w, 1, *args)
    self.w += 1
  

  def _fill(self, val, pos, r, lt, p, q, addfunc):
    if self._isnumeric(val):
      if pos < lt:
        for i in range(self.w):
          self.vals[pos*p + i*q] = val
      else:
        addfunc(*[val for _ in range(r)])


  def rowfill(self, val, pos):
    self._fill(val, pos, self.w, self.h, self.w, 1, self.addrow)


  def colfill(self, val, pos):
    self._fill(val, pos, self.h, self.w, 1, self.w, self.addcol)


  def removerow(self, pos):
    if self.h > 0 and pos < self.h:
      for _ in range(self.w):
        self.vals.pop(self.w*pos)
      self.h -= 1

    if self.h == 0:
      self.w = 0


  def removecol(self, pos):
    if self.w > 0 and pos < self.w:
      pos %= self.w
      for i in range(self.h):
        self.vals.pop(i*(self.w-1) + pos)
      self.w -= 1

    if self.w == 0:
      self.h = 0


  def __add__(self, other):
    new_m = Matrix()


  def __mul__(self, other):
    new_m = Matrix()
    for col in other.cols:
      s = [sum([self.at(l, i)*c for i, c in enumerate(col)]) for l in range(self.h)]
      print(s)
      #new_m.addcol()
    return new_m


  @property
  def det(self):
    if self.w * self.h == 1:
      return self.vals[0]

    if (self.w, self.h) == (2,2):
      return self.at(0, 0)*self.at(1, 1) - self.at(0, 1)*self.at(1, 0)

    d = 0
    for i in range(self.h):
      for j in range(self.w):
        b = [[y for y in (x[:j] + x[j+1:])] for x in self.cols[:i] + self.cols[i+1:]]
        d += det(val) if (i+j)%2 == 0 else -det(val)
    return d


  def __len__(self):
    return self.w * self.h


  def __repr__(self):
    if (self.w, self.h) == (0, 0):
      return "()"
    res = ""
    for i, val in enumerate(self.vals):
      end = "\n" if (i+1)%self.w == 0 else "\t"
      res += f"{val}{end}"
    return res

  def __str__(self):
    return self.__repr__()