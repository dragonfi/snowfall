import math

def to_polar(x, y):
    r = math.hypot(x, y)
    theta = math.atan2(y, x)
    return r, theta

def to_cartesian(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y


