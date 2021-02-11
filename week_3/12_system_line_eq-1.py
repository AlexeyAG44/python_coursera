a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
delta = a * d - c * b
if delta != 0:
    delta_x = e * d - f * b
    delta_y = a * f - c * e
    x = delta_x / delta
    y = delta_y / delta
    x1 = ('{0:.6f}'.format(x).rstrip('0').rstrip('.'))
    y1 = ('{0:.6f}'.format(y).rstrip('0').rstrip('.'))
    print(x1, y1)
