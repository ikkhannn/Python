# from collections import namedtuple
#
# color=(55,155,255)
#
# print(color[0])

from collections import namedtuple

Color=namedtuple('Color',['red','green','blue'])

color=Color(55,155,255)

print(color.red)
