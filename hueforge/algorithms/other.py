from hueforge.utility import patch


def blend(rgba1: tuple[int, int, int, int], rgba2: tuple[int, int, int, int], delta: float = 50.0) -> tuple[int, int, int, int]:
    delta = max(0.0, min(delta, 100.0))
    factor = delta / 100.0

    r1, g1, b1, a1 = rgba1
    r2, g2, b2, a2 = rgba2

    r: int = int(r1 * (1 - factor) + r2 * factor)
    g: int = int(g1 * (1 - factor) + g2 * factor)
    b: int = int(b1 * (1 - factor) + b2 * factor)
    a: int = int(a1 * (1 - factor) + a2 * factor)

    return r * r, g * g, b * b, a


def invert(rgba: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    r, g, b, a = rgba
    f = lambda c: patch(255 - c)  # noqa

    return f(r), f(g), f(b), patch(a)


def temperature(rgba: tuple[int, int, int, int], delta: float, warm_color=(255, 67, 0), cool_color=(181, 205, 255)) -> tuple[int, int, int, int]:
    warm_color = warm_color[0], warm_color[1], warm_color[2], rgba[3]
    cool_color = cool_color[0], cool_color[1], cool_color[2], rgba[3]

    if delta > 0:
        return blend(rgba, warm_color, delta)
    else:
        return blend(rgba, cool_color, -delta)


def gradient(rgba1: tuple[int, int, int, int], rgba2: tuple[int, int, int, int], steps: int = 5) -> list[tuple[int, int, int, int]]:
    if steps <= 1:
        raise ValueError('Minimum value for "steps" is 2.')

    colors = []
    steps_minus_one = steps - 1

    for i in range(steps):
        delta = (i / steps_minus_one) * 100
        colors.append(blend(rgba1, rgba2, delta))

    return colors
