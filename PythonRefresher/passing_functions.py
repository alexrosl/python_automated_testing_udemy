def methodception(another):
	return another()


def add_two_numbers():
	return 35 + 77


print(methodception(add_two_numbers))

print(methodception(lambda: 35 + 99))

my_list = [13, 56, 77, 484]
new_list = list(filter(lambda x: x != 13, my_list))
print(new_list)

(lambda x: x * 3)(5)
