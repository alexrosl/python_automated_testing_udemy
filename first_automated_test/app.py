blogs = dict()


def menu():
	# show available blogs
	# make choice
	# do something

	print_blogs()


def print_blogs():
	for key, blog in blogs.items():
		print('- {}'.format(blog))
