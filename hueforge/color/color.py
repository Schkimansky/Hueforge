from typing import Union, Literal
from hueforge.color.convertor import Convertor
from hueforge.algorithms.propertycontrol import increase_contrast, increase_brightness, increase_saturation, increase_hue


channels_to_index: dict[str, int] = {'r': 0, 'g': 1, 'b': 2, 'a': 3}


class Color:
    def __init__(
            self,
            value: Union[str, tuple[int, int, int], tuple[int, int, int, int]],
            of_type: Literal['hex', 'hexa', 'rgb', 'rgba', 'direct'] | None = None
    ):
        """
        Initializes a Color instance.

        :param value: The color value. Can be either:
            - A string representing the color (e.g., "red").
            - A string representing the hex value (e.g., "#FFAA00").
            - A string representing the hexa value (e.g., "#FFAA00FF").
            - A tuple of three integers representing RGB values (e.g., (255, 0, 0)).
            - A tuple of four integers representing RGBA values (e.g., (255, 0, 0, 255)).
        """
        self.convertor = Convertor()

        if of_type is None:
            self.value: tuple[int, int, int, int] = self.convertor.convert_auto(value, 'rgba')
        else:
            self.value: tuple[int, int, int, int] = self.convertor.convert(value, of_type, 'rgba')

    def convert(self, to_type: Literal['hex', 'hexa', 'rgb', 'rgba', 'direct']) -> Union[str, tuple[int, int, int], tuple[int, int, int, int]]:
        """ Converts the color to the desired color format. """
        return self.convertor.convert(self.value, 'rgba', to_type)

    def hex(self):    return self.convert('hex')
    def hexa(self):   return self.convert('hexa')
    def rgb(self):    return self.convert('rgb')
    def rgba(self):   return self.convert('rgba')
    def direct(self): return self.convert('direct')

    def increase_brightness(self, percentage: int | float): return Color(increase_brightness(self.rgba(), percentage), 'rgba')
    def increase_saturation(self, percentage: int | float): return Color(increase_saturation(self.rgba(), percentage), 'rgba')
    def increase_contrast(self, percentage: int | float):   return Color(increase_contrast(self.rgba(), percentage), 'rgba')
    def increase_hue(self, degrees: int | float):           return Color(increase_hue(self.rgba(), degrees), 'rgba')

    def decrease_brightness(self, percentage: int | float): return self.increase_brightness(-percentage)
    def decrease_saturation(self, percentage: int | float): return self.increase_saturation(-percentage)
    def decrease_contrast(self, percentage: int | float):   return self.increase_contrast(-percentage)
    def decrease_hue(self, degrees: int | float):           return self.increase_hue(-degrees)

    def process(self, query):
        identifier_to_function_name: dict[str, str] = {'c': 'increase_contrast', 's': 'increase_saturation', 'b': 'increase_brightness', 'h': 'increase_hue'}
        query = query.replace(' ', '')
        tasks = query.split('||')
        result = self

        for task in tasks:
            identifier, value = task.split(':')[0], float(task.split(':')[1])
            function_name = identifier_to_function_name[identifier]
            function = getattr(result, function_name)
            result = function(value)

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
            i = channels_to_index[channel]
            rgba[i] = eval(expression, {}, {'n1': rgba[i], 'n2': operand})

        return Color(rgba)


if __name__ == '__main__':
    # I warn you, Don't look below this.
    import trilent as t

    alignments = ['start', 'center', 'end']

    wwindow = t.Window()

    wcolor = Color('#ff00ff')
    wwidget = t.Widget(wwindow, 100, 100, widget_color=wcolor.hex())
    wwidget.place(20, 20)

    whue = 0
    wbrightness = 0
    wcontrast = 0
    wsaturation = 0

    def wincrease_hue(v): global whue; whue = v
    def wincrease_saturation(v): global wsaturation; wsaturation = v
    def wincrease_brightness(v): global wbrightness; wbrightness = v
    def wincrease_contrast(v): global wcontrast; wcontrast = v

    whue_slider = t.Slider(wwindow, quality=1, command=lambda v: wincrease_hue(v / 1000))
    whue_slider.place(140, 20)
    t.Text(wwindow, "Hue", text_size=20).place(170 + 150, 30)

    wbrightness_slider = t.Slider(wwindow, quality=1, command=lambda v: wincrease_brightness(v))
    wbrightness_slider.place(140, 20 + (26 * 1))
    t.Text(wwindow, "Brightness", text_size=20).place(170 + 150, 30 + (26 * 1))

    wcontrast_slider = t.Slider(wwindow, quality=1, command=lambda v: wincrease_contrast(v))
    wcontrast_slider.place(140, 20 + (26 * 2))
    t.Text(wwindow, "Contrast", text_size=20).place(170 + 150, 30 + (26 * 2))

    wsaturation_slider = t.Slider(wwindow, quality=1, command=lambda v: wincrease_saturation(v))
    wsaturation_slider.place(140, 20 + (26 * 3))
    t.Text(wwindow, "Saturation", text_size=20).place(170 + 150, 30 + (26 * 3))

    def update():
        wwidget.change(
            widget_color=wcolor
            .increase_hue(whue)
            .decrease_contrast(wcontrast)
            .decrease_saturation(wsaturation)
            .decrease_brightness(wbrightness)
            .hex()
        )

    wwindow.run(update=update)
