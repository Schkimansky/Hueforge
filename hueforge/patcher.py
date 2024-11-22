
def rangify(component: int) -> int: return max(0, min(255, component))

def percentage_to_factor(percentage: int | float) -> float:
    factor = (percentage + 100) / 100

    # if percentage < 0:
    #     factor = -factor

    return factor

def unfloatify(component: float) -> int: return int(component)

def patch(c: int | float) -> int | float:
    return unfloatify(rangify(c))

def patch_channels(*args):
    return tuple( unfloatify(rangify(arg)) for arg in args )  # noqa

def patch_color(c):
    cls = type(c)
    r, g, b, a = c.rgba()
    return cls((r, g, b, a))
