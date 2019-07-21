import functools


def my_decorator(func):
	@functools.wraps(func)
	def function_that_runs_fun():
		print("in the decorator")
		func()
		print("after the decorator")

	return function_that_runs_fun


@my_decorator
def my_function():
	print("I'm the function")


# my_function()


##

def decorator_with_arguments(number):
	def decc(func):
		@functools.wraps(func)
		def function_that_runs_func(*args, **kwargs):
			print("In the decorator")
			if number == 56:
				print("not running function")
			else:
				func(*args, **kwargs)
			print("after")

		return function_that_runs_func

	return decc


@decorator_with_arguments(57)
def my_function_too(x, y):
	print(x + y)


my_function_too(57, 57)
