# https://www.youtube.com/watch?v=mUu_4k6a5-I&t=5984s
# https://github.com/ramalho/pyob


import sys
from pprint import pprint

pprint(sys.version)

#
# class Coordinate:
#     '''Coordinate on Earth'''
#
#     lat = 0.0
#     long = 0.0
#
#     def __repr__(self):
#         return f'Coordinate({self.lat}, {self.long})'
#
#     def __str__(self):
#         ns = 'NS'[self.lat < 0]
#         we = 'EW'[self.long < 0]
#         return f'{abs(self.lat):.1f}°{ns}, {abs(self.long):.1f}°{we}'
#
# pprint(f'{Coordinate.__dict__ = }')
#
# cle = Coordinate()
# cle.lat = 41.4
# cle.long = -81.8
# print(cle)
#
# pprint(f'{cle.__dict__ = }')
# print(cle.__repr__())
# print(cle.__repr__)
# print(repr(cle))
# print()
#
# # print(dir(cle))
# # print(cle.__dict__)
# # print(cle.__doc__)
# # print(cle.lat)
# # print(cle.__repr__)
#
# gulf_of_guinea = Coordinate()
# try:
#     print(gulf_of_guinea)
# except AttributeError as e:
#     print(e)
#
# pprint(f'{gulf_of_guinea.__dict__ = }')
# pprint(gulf_of_guinea.lat)


class Pizza:

    diameter = 40  # cm
    slices = 8

    def __init__(self, flavor='Cheese', flavor2=None):
        self.flavor = flavor
        self.flavor2 = flavor2

    def __repr__(self):
        return f'Pizza({self.diameter}, {self.slices}, {self.flavor}, {self.flavor2})'

    def __str__(self):
        return f'Pizza: diameter={self.diameter}, slices={self.slices}, add1={self.flavor}, add2={self.flavor2}'

# p1 = Pizza()
# pprint(p1)
# print(p1)

# import geohash


class Coordinate:
    '''Coordinate on Earth'''

    reference_system = 'WGS84'
    common = 55

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def __repr__(self):
        return f'Coordinate({self.lat}, {self.long})'

    def __str__(self):
        ns = 'NS'[self.lat < 0]
        we = 'WE'[self.long < 0]
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.long):.1f}°{we}'

    # def geohash(self):
    #     return geohash.encode(self.lat, self.long)


# cle = Coordinate(41.5, -81.7)
# mle = Coordinate(22.2, -33.3)
# print(cle)
# print(mle)
# Coordinate.common = 333
# print(cle)
# # mle.common=9
# print(cle)
# print(mle)

london = Coordinate(51.5, -0.1)
print(f"London: {london}")
