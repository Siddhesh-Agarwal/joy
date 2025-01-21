from joy import Rectangle, Repeat, Rotate
from _img import render

shape = Rectangle(width=200, height=100) | Repeat(18, Rotate(10))
render(shape)
