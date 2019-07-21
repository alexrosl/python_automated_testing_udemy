from first_automated_test.blog import Blog

MENU_PROMPT = "Enter 'c' to create a blog, " \
              "l list blogs" \
              "'r' read one, " \
              "'p' create post, " \
              "'q' quit"
POST_TEMPLATE = '''
---- {} ----

{}

'''

blogs = dict()


def menu():
	# show available blogs
	# make choice
	# do something

	print_blogs()
	selection = input(MENU_PROMPT)
	while selection != 'q':
		if selection == 'c':
			ask_create_blog()
		elif selection == 'l':
			print_blogs()
		elif selection == 'r':
			ask_read_blog()
		elif selection == 'p':
			ask_create_post()
		selection = input(MENU_PROMPT)


def print_blogs():
	for key, blog in blogs.items():
		print('- {}'.format(blog))


def ask_create_blog():
	title = input("Enter your blog title: ")
	author = input('Enter your name: ')

	blogs[title] = Blog(title, author)


def ask_read_blog():
	title = input('Enter the blog title')
	print_post(blogs[title])


def print_posts(blog):
	for post in blog.posts:
		print_post(post)


def print_post(post):
	print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
	blog_name = input('Enter blog title: ')
	title = input('Enter your post title: ')
	content = input('Enter your post content')

	blogs[blog_name].create_post(title, content)
