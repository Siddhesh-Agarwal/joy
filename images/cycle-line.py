from joy import Line, Repeat, Rotate
from _img import render

shape = Line() | Repeat(18, Rotate(10))
render(shape)
