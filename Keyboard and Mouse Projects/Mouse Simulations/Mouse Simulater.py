"""
from pynput.mouse import Button, Controller
mouse = Controller()
mouse.position = (750, 750)
mouse.move(100, -100)
mouse.click(Button.left, 10000)
print (f"The current mouse position is at {mouse.position}")
mouse.click(Button.left, 10)
"""
import numpy as np

a = np.array([1, 2, 3])
print(a)
print(type(a))
c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]], dtype=float)
print(c)
print(type(c))
