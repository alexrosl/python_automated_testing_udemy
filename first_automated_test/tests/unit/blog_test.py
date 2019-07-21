from unittest import TestCase

from first_automated_test.blog import Blog


class BlogTest(TestCase):
	def test_create_blog(self):
		b = Blog('Test', 'Test Author')

		self.assertEqual('Test', b.title)
		self.assertEqual('Test Author', b.author)
		self.assertListEqual([], b.posts)

	def test_repr(self):
		b = Blog('Test', 'Test Author')

		self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')

	def test_rep_multiple_posts(self):
		b = Blog('Test', 'Test Author')
		b.posts = ['test']
		b2 = Blog('Test', 'Test Author')
		b2.posts = ['test', 'another']

		self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
		self.assertEqual(b2.__repr__(), 'Test by Test Author (2 posts)')
