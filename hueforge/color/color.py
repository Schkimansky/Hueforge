from typing import Union  # Literal not needed as it's imported by "*" the line below this line.
from hueforge.algorithms.colorblindness import *
from hueforge.algorithms.other import gradient, temperature, invert, blend
from hueforge.color.convertor import Convertor
from hueforge.algorithms.property_adjustment import increase_contrast, increase_brightness, increase_saturation, increase_hue


CHANNELS_TO_INDEX: dict[str, int] = {'r': 0, 'g': 1, 'b': 2, 'a': 3}


class Color:
    def __init__(
            self,
            value: Union[str, tuple[int, int, int], tuple[int, int, int, int]],
            of_type: Literal['hex', 'hexa', 'rgb', 'rgba', 'direct'] | None = None
    ):
        """
        :param value: The color value. Can be either:
            - A string representing the color (e.g., "red").
            - A string representing the hex value (e.g., "#FFAA00").
            - A string representing the hexa value (e.g., "#FFAA00FF").
            - A tuple of three integers representing RGB values (e.g., (255, 0, 0)).
            - A tuple of four integers representing RGBA values (e.g., (255, 0, 0, 255)).

        :param of_type:
            Optional.
            This specifies the color format of the value parameter.
            If not given, The format is automatically detected.
        """
        self.convertor = Convertor()

        if of_type is None:
            self.value: tuple[int, int, int, int] = self.convertor.convert_auto(value, 'rgba')
        else:
            self.value: tuple[int, int, int, int] = self.convertor.convert(value, of_type, 'rgba')

    def hex(self):    return self._convert('hex')
    def hexa(self):   return self._convert('hexa')
    def rgb(self):    return self._convert('rgb')
    def rgba(self):   return self._convert('rgba')
    def direct(self): return self._convert('direct')

    # Colorblindness functions
    def simulate_colorblindness(self, colorblindness: COLORBLINDNESSES = 'd'):
        """ Adjusts the color as if it was looked at by a colorblinded person. """
        return simulate_colorblindness(self.rgba(), colorblindness)

    def help_colorblindness(self, colorblindness: COLORBLINDNESSES = 'd'):
        """ Adjusts the color so a colorblind person can properly see it. """
        return help_colorblindness(self.rgba(), colorblindness)

    # Color harmonies
    def get_complementary_color(self):
        return self.increase_hue(180)

    def get_split_complementary_colors(self, offset=30):
        return [
            self,
            self.increase_hue(180 - offset),
            self.increase_hue(180 + offset)
        ]

    def get_analogous_colors(self, offset=30):
        return [
            self.increase_hue(-offset),
            self,
            self.increase_hue(offset)
        ]

    def get_triadic_colors(self):
        return [
            self,
            self.increase_hue(120),
            self.increase_hue(240)
        ]

    def get_tetradic_colors(self):
        return [
            self,
            self.increase_hue(90),
            self.increase_hue(180),
            self.increase_hue(270)
        ]

    def get_square_colors(self):
        return self.get_tetradic_colors()

    # Some functions to adjust color properties, Eg contrast, saturation and brightness
    def increase_brightness(self, percentage: int | float): return Color(increase_brightness(self.rgba(), percentage), 'rgba')
    def increase_saturation(self, percentage: int | float): return Color(increase_saturation(self.rgba(), percentage), 'rgba')
    def increase_contrast(self, percentage: int | float):   return Color(increase_contrast(self.rgba(), percentage), 'rgba')
    def increase_hue(self, degrees: int | float):           return Color(increase_hue(self.rgba(), degrees), 'rgba')

    def decrease_brightness(self, percentage: int | float): return self.increase_brightness(-percentage)
    def decrease_saturation(self, percentage: int | float): return self.increase_saturation(-percentage)
    def decrease_contrast(self, percentage: int | float):   return self.increase_contrast(-percentage)
    def decrease_hue(self, degrees: int | float):           return self.increase_hue(-degrees)

    # Ease of use methods
    def __str__(self):  return f'Color({self.hex()})'
    def __repr__(self): return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.rgba() == other.rgba()

        return super().__eq__(other)

    # Operator methods
    def add(self, by, channels=None): return self._base_op('n1 + n2', by, channels)
    def subtract(self, by, channels=None): return self._base_op('n1 - n2', by, channels)
    def multiply(self, by, channels=None): return self._base_op('n1 * n2', by, channels)
    def divide(self, by, channels=None): return self._base_op('n1 / n2', by, channels)

    def __add__(self, other): return self.add(other)
    def __mul__(self, other): return self.multiply(other)
    def __truediv__(self, other): return self.divide(other)
    def __sub__(self, other): return self.subtract(other)

    def _base_op(self, expression: str, operand: int | float, channels: list[str] = None):
        if channels is None:
            channels = ['r', 'g', 'b']

        rgba = self.rgba()

        for channel in channels:
            i = CHANNELS_TO_INDEX[channel]
            rgba[i] = eval(expression, {}, {'n1': rgba[i], 'n2': operand})

        return Color(rgba)

    # Other
    def gradient(self, to, steps: int = 5) -> list:
        """ Returns a list of some colors that form a smooth gradient from 1 color to the other """
        return [Color(rgba, 'rgba') for rgba in gradient(self.rgba(), to.rgba(), steps)]

    def _convert(self, to_type: Literal['hex', 'hexa', 'rgb', 'rgba', 'direct']) -> Union[str, tuple[int, int, int], tuple[int, int, int, int]]:
        return self.convertor.convert(self.value, 'rgba', to_type)

    def blend(self, other_color, delta: float = 50.0):
        return Color(blend(self.rgba(), other_color.rgba(), delta))

    def invert(self):
        return Color(invert(self.rgba()))

    def temperature(self, temp: float, warm_color=(255, 67, 0), cool_color=(181, 205, 255)):
        return Color(temperature(self.rgba(), temp, warm_color, cool_color))
