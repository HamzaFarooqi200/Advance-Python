#example no.1:
#********************************************************
from functools import partial


def power(a, b):
	return a**b


# partial functions
pow2 = partial(power, b=45)
pow4 = partial(power, b=2)
power_of_5 = partial(power, 4)

print(power(2, 3))
print(pow2(4))
print(pow4(3))
print(power_of_5(2))

#********************************************************
#example no.2:
from functools import partialmethod

class Dummy:
	def __init__(self):
		self.color = 'black'

	def _color(self, type):
		self.color = type

	set_red = partialmethod(_color, type='red')
	set_blue = partialmethod(_color, type='blue')
	set_green = partialmethod(_color, type='green')


obj = Dummy()
print(obj.color)
obj.set_blue()
print(obj.color)

#********************************************************
#example no.3:
from functools import wraps

def decorator(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		"""Decorator's docstring"""
		return f(*args, **kwargs)

	print('Documentation of decorated :', decorated.__doc__)
	return decorated

@decorator
def f(x):
	"""f's Docstring"""
	return x

print('f name :', f.__name__)
print('Documentation of f :', f.__doc__)
