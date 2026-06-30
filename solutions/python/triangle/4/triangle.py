def equilateral(sides):
    sidea, sideb, sidec = sides
    return sidea + sideb > sidec and sidea + sidec > sideb and sideb + sidec > sidea and len(set(sides)) == 1


def isosceles(sides):
    sidea, sideb, sidec = sides
    return sidea + sideb > sidec and sidea + sidec > sideb and sideb + sidec > sidea and len(set(sides)) <= 2


def scalene(sides):
    sidea, sideb, sidec = sides
    return sidea + sideb > sidec and sidea + sidec > sideb and sideb + sidec > sidea and len(set(sides)) == 3
