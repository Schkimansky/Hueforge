from colorsys import rgb_to_hsv, hsv_to_rgb
from hueforge.utility import percentage_to_factor, patch


def increase_brightness(rgba, percentage: int | float):
    factor = percentage_to_factor(percentage)
    r, g, b, a = rgba
    f = lambda channel: patch(channel * factor)  # noqa

    return f(r), f(g), f(b), patch(a)


def increase_contrast(rgba, percentage: int | float):
    factor = percentage_to_factor(percentage)
    r, g, b, a = rgba
    f = lambda channel: patch(128 + (channel - 128) * factor)  # noqa

    return f(r), f(g), f(b), patch(a)


def increase_saturation(rgba, percentage: int | float):
    factor = percentage_to_factor(percentage)
    r, g, b, a = rgba
    grayscale = (r + g + b) / 3
    f = lambda channel: patch(grayscale + (channel - grayscale) * factor)  # noqa

    return f(r), f(g), f(b), patch(a)


def increase_hue(rgba, percentage: int | float):
    factor = percentage_to_factor(percentage) * 360
    r, g, b, a = rgba

    h, s, v = rgb_to_hsv(r, g, b)   # Convert to hsv (hue, saturation, value/lightness)
    h = (h + factor) % 360          # Increase hue channel
    r, g, b = hsv_to_rgb(h, s, v)   # Convert to rgb

    return patch(r), patch(g), patch(b), patch(a)
