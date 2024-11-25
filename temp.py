from hueforge.color.color import Color

red = Color((255, 0, 0))
green = Color((0, 255, 0))

print(red.blend(green, 50))
