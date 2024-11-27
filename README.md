# HueForge
## A python library to handle everything color related.

This is a python library that handles everything color related. It includes a color class. 
Valid ways to initialize an object:

```python
from hueforge import Color

# Valid ways to initialize:
example_color = Color("#FF0000")        # Hex color format                       
example_color = Color("#FF0000FF")      # Hexa color format                      
example_color = Color("Orange red")     # Direct color format                    
example_color = Color((255, 0, 0))      # RGB color format                       
example_color = Color((255, 0, 0, 255)) # RGBA color format                      
example_color = Color((0, 0))           # Invalid color format; Raises exception 
```

Get a color in a specific format from a Color() instance:
```python
from hueforge import Color

example_color = Color("#FF0000")

print(example_color.hex())     # Outputs: "#FF0000"
print(example_color.hexa())    # Outputs: "#FF0000FF"
print(example_color.rgb())     # Outputs: (255, 0, 0)
print(example_color.rgba())    # Outputs: (255, 0, 0, 255)
print(example_color.direct())  # Outputs: "red"

# Note: example_color.direct() will raise a exception if the color
# is too unique and doesn't have a set name.
```

Adjust brightness, contrast, hue and saturation.
```python
from hueforge import Color

example_color = Color("#99ABD3")

# Note: These methods don't modify the color in 
# place, They return a new color instead.

print(example_color.increase_brightness(40))   # Increase brightness by 40%
print(example_color.increase_contrast(70))     # Increase contrast by 70%
print(example_color.increase_hue(180))         # Increase hue by 180 degrees (0 - 360)
print(example_color.increase_saturation(100))  # Increase Saturation by 100%

# You can also use decrease_brightness, decrease_contrast etc.
```

Simulate colorblindness and help colorblindness.
```python
from hueforge import Color

example_color = Color("#FF0000")
colorblindness = "protanopia"  # Type of colorblindness. Possible values: deuteranopia, deuteranomaly, protanopia, protanomaly, tritanopia, tritanomaly, all, d, t, p, d1, t1, p1, d2, t2, p2, a (all)

print(f"A colorblind person would see this as: {example_color.simulate_colorblindness(colorblindness)}")
print(f"Adjusted color so the colorblind person can see the color properly: {example_color.help_colorblindness(colorblindness)}")
```

Generate a smooth color gradient starting from one color, Ending with the other:
```python
from hueforge import Color

starting_color = Color("#FF0000")
ending_color = Color("#0000FF")

gradient = starting_color.gradient(ending_color, steps=3)
print(gradient)  # Outputs: [Color(#FF0000), Color(#7F007F), Color(#0000FF)]

# Increase steps for a higher quality gradient, It's recommended to keep it under 255.
# By higher quality, I mean that there are more unique colors leading to a smoother gradient. For example, a 2 step gradient would just be [starting_color, end_color]. Such a gradient is useless because of the low quality. 
high_quality_gradient = starting_color.gradient(ending_color, steps=5)
print(high_quality_gradient)  # Outputs: [Color(#FF0000), Color(#BF003F), Color(#7F007F), Color(#3F00BF), Color(#0000FF)]
```

Color Harmonies:
```python
from hueforge import Color

example_color = Color("#FF0000")
print(example_color.get_complementary_color())
print(example_color.get_split_complementary_colors())
print(example_color.get_analogous_colors())
print(example_color.get_triadic_colors())
print(example_color.get_tetradic_colors())
print(example_color.get_square_colors())

# Hover over these functions (in an IDE) to see their return order.
```

Blending colors
```python
from hueforge import Color

color1 = Color("#FF0000")
color2 = Color("#FFFF00")
print(color1.blend(color2))  # Gives a 50/50 mix of color1 and color2
print(color1.blend(color2, delta=0))  # Gives color1
print(color1.blend(color2, delta=70))  # Gives a 70/30 mix of color1 and color2
print(color1.blend(color2, delta=100))  # Gives color2
```

Inverting colors
```python
from hueforge import Color

example_color = Color("#FF0000")
print(example_color.invert())
```

Temperature control
```python
from hueforge import Color

example_color = Color("#FF0000")
print(example_color.temperature(100))  # 100 = extremely hot temperature, 0 = extremely cold temperature
```

That's almost everything that's included in this library. Thanks for using HueForge!
