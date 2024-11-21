from hueforge.patcher import percentage_to_factor, rangify, unfloatify


def increase_brightness(rgba: tuple[int, int, int, int], percentage: int | float) -> tuple[int, int, int, int]:
    factor = percentage_to_factor(percentage)
    r, g, b, a = rgba
    f = lambda channel: rangify(unfloatify(channel * factor))  # noqa

    return f(r), f(g), f(b), a


def increase_contrast(rgba: tuple[int, int, int, int], percentage: int | float) -> tuple[int, int, int, int]:
    factor = percentage_to_factor(percentage)
    r, g, b, a = rgba
    f = lambda channel: rangify(unfloatify(128 + (channel - 128) * factor))  # noqa

    return f(r), f(g), f(b), a


def increase_saturation(rgba: tuple[int, int, int, int], percentage: int | float) -> tuple[int, int, int, int]:
    factor = percentage_to_factor(percentage)
    r, g, b, a = rgba
    grayscale = (r + g + b) / 3
    f = lambda channel: rangify(unfloatify(grayscale + (channel - grayscale) * factor))  # noqa

    return f(r), f(g), f(b), a
