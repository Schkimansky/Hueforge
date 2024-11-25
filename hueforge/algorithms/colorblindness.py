from typing import Literal

COLORBLINDNESSES = Literal['deuteranopia', 'deuteranomaly', 'protanopia', 'protanomaly', 'tritanopia', 'tritanomaly', 'all', 'd', 't', 'p', 'd1', 't1', 'p1', 'd2', 't2', 'p2', 'a']
COLORBLINDNESS_FACTORS = {
    'deuteranopia':  (1.0,  1.75, 1.25),
    'deuteranomaly': (1.0,  1.5,  1.25),
    'protanopia':    (1.0,  1.3,  1.0),
    'protanomaly':   (1.25, 1.25, 1.0),
    'tritanopia':    (1.0,  1.0,  1.0),
    'tritanomaly':   (1.0,  1.0,  1.5),
    'all':           (1.2,  1.3,  1.3),
}
NAME_SHORTCUTS = {
    'd': 'deuteranomaly',
    't': 'tritanomaly',
    'p': 'protanomaly',

    'd1': 'deuteranomaly',
    't1': 'tritanomaly',
    'p1': 'protanomaly',

    'd2': 'deuteranopia',
    't2': 'tritanopia',
    'p2': 'protanopia',

    'a': 'all',
}

def get_factors(colorblindness: COLORBLINDNESSES):
    return COLORBLINDNESS_FACTORS[NAME_SHORTCUTS.get(colorblindness, colorblindness)]

def simulate_colorblindness(rgba, colorblindness: COLORBLINDNESSES = 'd'):
    r, g, b, a = rgba

    helped = help_colorblindness(rgba, colorblindness)
    difference = r - helped[0], g - helped[1], b - helped[2], a - helped[3]

    return r + difference[0], g + difference[1], b + difference[2], a + difference[1]

def help_colorblindness(rgba, colorblindness: COLORBLINDNESSES = 'd'):
    r, g, b, a = rgba
    factors = get_factors(colorblindness)

    return (
        r * factors[0],
        g * factors[1],
        b * factors[2],
        a
    )
