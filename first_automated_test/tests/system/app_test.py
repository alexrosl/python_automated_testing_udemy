from unittest import TestCase
from unittest.mock import patch

import first_automated_test.app as app
from first_automated_test.blog import Blog
from first_automated_test.post import Post


class AppTest(TestCase):
	def setUp(self):
		blog = Blog('Test', 'Test Author')
		app.blogs = {'Test': blog}

	def test_menu_calls_create_blog(self):
		with patch('builtins.input') as mocked_input:
			with patch('first_automated_test.app.ask_create_blog') as mocked_ask_create_blog:
				mocked_input.side_effect = ('c', 'q')

				app.menu()

				mocked_ask_create_blog.assert_called()

	def test_menu_print_prompt(self):
		with patch('builtins.input', return_value='q') as mocked_input:
			app.menu()
			mocked_input.assert_called_with(app.MENU_PROMPT)

	def test_menu_calls_print_blogs(self):
		with patch('first_automated_test.app.print_blogs') as mocked_pring_blogs:
			with patch('builtins.input', return_value='q'):
				app.menu()
				mocked_pring_blogs.assert_called()

	def test_print_blogs(self):
		with patch('builtins.print') as mocked_print:
			app.print_blogs()
			mocked_print.assert_called_with('- Test by Test Author (0 posts)')

	def test_ask_create_blog(self):
		with patch('builtins.input') as mocked_input:
			mocked_input.side_effect = ('Test', 'Test Author')
			app.ask_create_blog()

			self.assertIsNotNone(app.blogs.get('Test'))

	def test_ask_read_blog(self):
		blog = app.blogs['Test']
		with patch('builtins.input', return_value='Test'):
			with patch('first_automated_test.app.print_post') as mocked_print_posts:
				app.ask_read_blog()

			mocked_print_posts.assert_called_with(blog)

	def test_print_posts(self):
		blog = app.blogs['Test']
		blog.create_post('Test Post', 'Test Content')

		with patch('first_automated_test.app.print_post') as mocked_print_post:
			app.print_posts(blog)

			mocked_print_post.assert_called_with(blog.posts[0])

	def test_print_post(self):
		post = Post('Post title', 'Post content')
		expected_print = '''
---- Post title ----

Post content

'''
		with patch('builtins.print') as mocked_print:
			app.print_post(post)
			mocked_print.assert_called_with(expected_print)

	def test_ask_create_post(self):
		blog = app.blogs['Test']

		with patch('builtins.input') as mocked_input:
			mocked_input.side_effect = ('Test', 'Test Title', 'Test Content')

			app.ask_create_post()

			self.assertEqual(blog.posts[0].title, 'Test Title')
			self.assertEqual(blog.posts[0].content, 'Test Content')
