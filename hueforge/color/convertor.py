from typing import Literal, Union
from hueforge.color.detection import Detection
from hueforge.utility import patch_rgba

COLOR_NAMES = {'aliceblue': '#F0F8FF', 'antiquewhite': '#FAEBD7', 'aqua': '#00FFFF', 'aquamarine': '#7FFFD4', 'azure': '#F0FFFF', 'beige': '#F5F5DC', 'bisque': '#FFE4C4', 'black': '#000000', 'blanchedalmond': '#FFEBCD', 'blue': '#0000FF', 'blueviolet': '#8A2BE2', 'brown': '#A52A2A', 'burlywood': '#DEB887', 'cadetblue': '#5F9EA0', 'chartreuse': '#7FFF00', 'chocolate': '#D2691E', 'coral': '#FF7F50', 'cornflowerblue': '#6495ED', 'cornsilk': '#FFF8DC', 'crimson': '#DC143C', 'litecrimson': '#F21642', 'delightcrimson': '#D11339', 'cyan': '#00FFFF', 'darkblue': '#00008B', 'darkcyan': '#008B8B', 'darkgoldenrod': '#B8860B', 'darkgray': '#A9A9A9', 'darkgreen': '#006400', 'darkgrey': '#A9A9A9', 'darkkhaki': '#BDB76B', 'darkmagenta': '#8B008B', 'darkolivegreen': '#556B2F', 'darkorange': '#FF8C00', 'darkorchid': '#9932CC', 'darkred': '#8B0000', 'darksalmon': '#E9967A', 'darkseagreen': '#8FBC8F', 'darkslateblue': '#483D8B', 'darkslategray': '#2F4F4F', 'darkslategrey': '#2F4F4F', 'darkturquoise': '#00CED1', 'darkviolet': '#9400D3', 'deeppink': '#FF1493', 'deepskyblue': '#00BFFF', 'dimgray': '#696969', 'dimgrey': '#696969', 'dodgerblue': '#1E90FF', 'firebrick': '#B22222', 'floralwhite': '#FFFAF0', 'forestgreen': '#228B22', 'fuchsia': '#FF00FF', 'gainsboro': '#DCDCDC', 'ghostwhite': '#F8F8FF', 'gold': '#FFD700', 'goldenrod': '#DAA520', 'gray': '#808080', 'green': '#008000', 'greenyellow': '#ADFF2F', 'grey': '#808080', 'honeydew': '#F0FFF0', 'hotpink': '#FF69B4', 'indianred': '#CD5C5C', 'indigo': '#4B0082', 'ivory': '#FFFFF0', 'khaki': '#F0E68C', 'lavender': '#E6E6FA', 'lavenderblush': '#FFF0F5', 'lawngreen': '#7CFC00', 'lemonchiffon': '#FFFACD', 'lightblue': '#ADD8E6', 'lightcoral': '#F08080', 'lightcyan': '#E0FFFF', 'lightgoldenrodyellow': '#FAFAD2', 'lightgray': '#D3D3D3', 'lightgreen': '#90EE90', 'lightgrey': '#D3D3D3', 'lightpink': '#FFB6C1', 'lightsalmon': '#FFA07A', 'lightseagreen': '#20B2AA', 'lightskyblue': '#87CEFA', 'lightslategray': '#778899', 'lightslategrey': '#778899', 'lightsteelblue': '#B0C4DE', 'lightyellow': '#FFFFE0', 'lime': '#00FF00', 'limegreen': '#32CD32', 'linen': '#FAF0E6', 'magenta': '#FF00FF', 'maroon': '#800000', 'mediumaquamarine': '#66CDAA', 'mediumblue': '#0000CD', 'mediumorchid': '#BA55D3', 'mediumpurple': '#9370DB', 'mediumseagreen': '#3CB371', 'mediumslateblue': '#7B68EE', 'mediumspringgreen': '#00FA9A', 'mediumturquoise': '#48D1CC', 'mediumvioletred': '#C71585', 'midnightblue': '#191970', 'mintcream': '#F5FFFA', 'mistyrose': '#FFE4E1', 'moccasin': '#FFE4B5', 'navajowhite': '#FFDEAD', 'navy': '#000080', 'oldlace': '#FDF5E6', 'olive': '#808000', 'olivedrab': '#6B8E23', 'orange': '#FFA500', 'orangered': '#FF4500', 'orchid': '#DA70D6', 'palegoldenrod': '#EEE8AA', 'palegreen': '#98FB98', 'paleturquoise': '#AFEEEE', 'palevioletred': '#DB7093', 'papayawhip': '#FFEFD5', 'peachpuff': '#FFDAB9', 'peru': '#CD853F', 'pink': '#FFC0CB', 'plum': '#DDA0DD', 'powderblue': '#B0E0E6', 'purple': '#800080', 'red': '#FF0000', 'rosybrown': '#BC8F8F', 'royalblue': '#4169E1', 'saddlebrown': '#8B4513', 'salmon': '#FA8072', 'sandybrown': '#F4A460', 'seagreen': '#2E8B57', 'seashell': '#FFF5EE', 'sienna': '#A0522D', 'silver': '#C0C0C0', 'skyblue': '#87CEEB', 'slateblue': '#6A5ACD', 'slategray': '#708090', 'slategrey': '#708090', 'snow': '#FFFAFA', 'springgreen': '#00FF7F', 'steelblue': '#4682B4', 'tan': '#D2B48C', 'teal': '#008080', 'thistle': '#D8BFD8', 'tomato': '#FF6347', 'turquoise': '#40E0D0', 'violet': '#EE82EE', 'wheat': '#F5DEB3', 'white': '#FFFFFF', 'whitesmoke': '#F5F5F5', 'yellow': '#FFFF00', 'yellowgreen': '#9ACD32', 'xylon': '#0074D9'}

# "COLOR_NAMES" but reversed since key: value is reversed to value: key
SEMAN_ROLOC = {v: k for k, v in COLOR_NAMES.items()}

COLOR_TYPES = [
    'hex',    # #FF0033
    'hexa',   # #FF0033AA
    'rgb',    # (255, 255, 255)
    'rgba',   # (255, 255, 255, 255)
    'direct'  # red | orangered | lime | green
]


class Convertor(Detection):
    def convert(self,
                value: Union[str, tuple[int, int, int], tuple[int, int, int, int]],
                from_type: Literal['hex', 'hexa', 'rgb', 'rgba', 'direct'],
                to_type: Literal['hex', 'hexa', 'rgb', 'rgba', 'direct']) -> Union[str, tuple[int, int, int], tuple[int, int, int, int]]:  # noqa
        """ Converts a color from one format to another. """
        if from_type == to_type:
            return value

        # Convert from current format to RGBA first.
        if from_type == 'hex':
            rgba = self.hex_to_rgba(value)
        elif from_type == 'hexa':
            rgba = self.hexa_to_rgba(value)
        elif from_type == 'rgb':
            rgba = self.rgb_to_rgba(value)
        elif from_type == 'rgba':
            rgba = value
        elif from_type == 'direct':
            rgba = self.direct_to_rgba(value)
        else:
            raise Exception(f"Invalid from_type: {to_type}. Possible from_type's: {COLOR_TYPES} ")

        # Then convert it to the desired color format.
        if to_type == 'hex':
            desired_color = self.rgba_to_hex(rgba)
        elif to_type == 'hexa':
            desired_color = self.rgba_to_hexa(rgba)
        elif to_type == 'rgb':
            desired_color = self.rgba_to_rgb(rgba)
        elif to_type == 'rgba':
            desired_color = rgba
        elif to_type == 'direct':
            desired_color = self.rgba_to_direct(value)
        else:
            raise Exception(f"Invalid to_type: {to_type}. Possible to_type's: {COLOR_TYPES} ")

        return desired_color

    def convert_auto(self, value: Union[str, tuple[int, int, int], tuple[int, int, int, int]], to_type: Literal['hex', 'hexa', 'rgb', 'rgba', 'direct']) -> Union[str, tuple[int, int, int], tuple[int, int, int, int]]:  # noqa
        """ The same as self.convert() but automatically detects the from_type based on the value """
        return self.convert(value, self.detect(value), to_type)

    @staticmethod
    def hex_to_rgba(hex: str) -> tuple[int, int, int, int]:  # noqa
        hexa = hex + 'FF'
        hexa = hexa.removeprefix('#')
        rgba: tuple[int, int, int, int] = tuple(int(hexa[i:i + 2], 16) for i in (0, 2, 4, 6))  # noqa

        return rgba

    @staticmethod
    def rgba_to_hex(rgba: tuple[int, int, int, int]) -> str:  # noqa
        rgba = patch_rgba(rgba)
        return '#%02X%02X%02X' % rgba[0:3]

    @staticmethod
    def hexa_to_rgba(hexa: str) -> tuple[int, int, int, int]:
        hexa = hexa.removeprefix('#')
        if len(hexa) == 6:
            hexa += 'FF'  # Add 'FF' if no alpha is provided

        rgba: tuple[int, int, int, int] = tuple(int(hexa[i:i + 2], 16) for i in (0, 2, 4, 6))  # noqa

        return rgba

    @staticmethod
    def rgba_to_hexa(rgba: tuple[int, int, int, int]) -> str:
        rgba = patch_rgba(rgba)
        return '#%02X%02X%02X%02X' % rgba

    @staticmethod
    def rgb_to_rgba(rgb: tuple[int, int, int]) -> tuple[int, int, int, int]:
        return rgb[0], rgb[1], rgb[2], 255

    @staticmethod
    def rgba_to_rgb(rgba: tuple[int, int, int, int]) -> tuple[int, int, int]:
        return rgba[0], rgba[1], rgba[2]

    def direct_to_rgba(self, direct: str) -> tuple[int, int, int]:
        direct = direct.replace(' ', '').lower()

        if direct not in COLOR_NAMES:
            raise ValueError(f'Unknown color name: {direct}')

        hex = COLOR_NAMES[direct]  # noqa

        return self.convert(hex, 'hex', 'rgba')

    def rgba_to_direct(self, rgba: tuple[int, int, int, int]) -> str:
        hex = self.convert(rgba, 'rgba', 'hex')  # noqa

        if hex not in SEMAN_ROLOC:
            raise ValueError("Cannot convert color to 'direct' format, No known direct color names match.")

        return SEMAN_ROLOC[hex]

    # No need for rgba_to_rgba and vice versa function
