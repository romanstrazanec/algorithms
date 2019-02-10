from point import Point


def convexhull(points):
  def rightturn(last3ps):
    def der(p1, p2):
      from sys import float_info
      dy = p2.y - p1.y
      dx = p2.x - p1.x
      if dx == 0:
        dx = float_info.epsilon
      return dy/dx
    return der(last3ps[0], last3ps[1]) > der(last3ps[0], last3ps[2])

  ps = points.copy()
  ps.sort(key=lambda p: p.x)
  Lupper = [ps[0], ps[1]]

  for i in range(2, len(ps)):
    Lupper.append(ps[i])
    while len(Lupper) > 2 and not rightturn(Lupper[-3:]):
      Lupper.pop(-2)

  Llower = [ps[-1], ps[-2]]
  for i in range(len(ps)-3, -1, -1):
    Llower.append(ps[i])
    while len(Llower) > 2 and not rightturn(Llower[-3:]):
      Llower.pop(-2)

  Llower.pop(0)
  
  Lupper.extend(Llower)
  return Lupper
