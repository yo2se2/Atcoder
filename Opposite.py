#アフィン変換

import numpy as np

N = int(input())

x0, y0 = map(int,input().split())
xh, yh = map(int,input().split())

#角度
deg = np.deg2rad(360/N)
cos = np.cos(deg)
sin = np.sin(deg)

xo, yo = (xh+x0)/2, (yh+y0)/2

rot_x = ((x0-xo)*cos) - ((y0-yo)*sin)
rot_y = ((x0-xo)*sin) + ((y0-yo)*cos)
rot_x += xo
rot_y += yo
print(rot_x,rot_y)