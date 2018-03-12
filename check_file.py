import matplotlib
from matplotlib.patches import Circle, Wedge, Polygon, Arrow
import matplotlib.lines as mlines
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import  numpy as np
def sortByRad(inputSet):
    return inputSet[1]

wells_coord = [(2,3), (8,7), (4,5), (1,1), (5,5), (6,5), (1,8)]
wells_coord.sort(key=sortByRad)

r_list = [1,2,3,4,5]


delta_r = 0.01
delta_r_fine = 0.005
R_for_fine = 0.02
R = 0.215
r_well = 0.0075
N_r_fine = int(R_for_fine/delta_r_fine)
N_r = int((R-r_well-R_for_fine)/delta_r)
delta_r_list = [delta_r_fine]*N_r_fine + [delta_r]*N_r
print(delta_r_list)

fig, ax = plt.subplots()

patches = []

# circle = Wedge((1.5, 1.5), 0.1, 0, 360, width=0.001)
# patches.append(circle)


for i in range(len(delta_r_list)):
    circle = Wedge((0.5, 0.5), sum(delta_r_list[0:i]), 0, 360, width=0.001)
    patches.append(circle)

arrow = Arrow(x=0.5, y=0.5, dx=0.2, dy=0.2, width=0.005)
patches.append(arrow)
p = PatchCollection(patches)

x, y = np.array([[0.0, 0.1, 0.2], [0.05, 0.2, 0.3]])
line = mlines.Line2D(x, y, lw=0.5)

ax.add_collection(p)
ax.add_line(line)
plt.show()

