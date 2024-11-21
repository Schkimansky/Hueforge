from typing import Union, Literal
from hueforge.color.convertor import Convertor
from hueforge.manipulation.manipulation import increase_contrast, increase_brightness, increase_saturation


class Color:
    def __init__(self, value: Union[str, tuple[int, int, int], tuple[int, int, int, int]],
                 of_type: Literal['hex', 'hexa', 'rgb', 'rgba', 'direct'] | None = None):
        """
        Initializes a Color instance.

        :param value: The color value. Can be either:
            - A string representing the color (e.g., "red").
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

    def hex(self):      return self.convert('hex')
    def hexa(self):     return self.convert('hexa')
    def rgb(self):      return self.convert('rgb')
    def rgba(self):     return self.convert('rgba')
    def direct(self):   return self.convert('direct')

    def __str__(self):  return f'Color({self.hex()})'
    def __repr__(self): return self.__str__()

    def increase_brightness(self, percentage: int | float): return Color(increase_brightness(self.rgba(), percentage), 'rgba')
    def increase_saturation(self, percentage: int | float): return Color(increase_saturation(self.rgba(), percentage), 'rgba')
    def increase_contrast(self, percentage: int | float):   return Color(increase_contrast(self.rgba(), percentage), 'rgba')

    def decrease_brightness(self, percentage: int | float): return self.increase_brightness(-percentage)
    def decrease_saturation(self, percentage: int | float): return self.increase_saturation(-percentage)
    def decrease_contrast(self, percentage: int | float):   return self.increase_contrast(-percentage)

    def process(self, query):
        identifier_to_function_name: dict[str, str] = {'c': 'increase_contrast', 's': 'increase_saturation', 'b': 'increase_brightness'}
        query = query.replace(' ', '')
        tasks = query.split('||')
        result = self

        for task in tasks:
            identifier, percentage = task.split(':')
            function_name = identifier_to_function_name[identifier]
            function = getattr(result, function_name)

            result = function()

        return result


if __name__ == '__main__':
    # print(Color('#3ea94f'))
    # 'c:10', 'b:10'
    # 'c: 10 || b: 10'

    color = Color('orange red')
    print(color)
