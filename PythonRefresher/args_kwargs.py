def my_method(arg1, arg2):
	return arg1 + arg2


my_method(5, 6)


def my_list_addition(list_arg):
	return sum(list_arg)


def addition_simplified(*args):
	return sum(args)


suum = addition_simplified(3, 5, 7, 12, 14, 15)
print(suum)


##


def what_are_kwargs(name, location):
	print(name)
	print(location)


what_are_kwargs(name="jose", location="UK")
