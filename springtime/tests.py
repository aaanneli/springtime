from django.test import TestCase
from rango.models import Category

class LinkTests(TestCase):
	# Test links are functioning.

	def test_index_has_contactUs_link(self):
		# Check to make usre link to Contact Us page is displayed.
		response = self.client.get(reverse('index'))
		self.assertContains(response, '<a href="%s%>Contact Us</a>' % reverse("index"), html = True)

	def test_index_has_trampolines_link(self):
		# Check to make sure link to Trampolines is displayed.
		response = self.client.get(reverse('index'))
		self.assertContains(response, '<a href="%s>Our Trampolines</a>' % reverse("trampolines"), html = True)

	def test_index_has_bookings_link(self):
		# Check to make sure link to bookings is displayed.
		response = self.client.get(reverse('index'))
		self.assertContains(response, '<a href="%s>Bookings</a>' % reverse ("bookings"), html = True)

	def test_contains_link_to_bookings(self):
		# Check My Account contains a link to Bookings.
		response = self.client.get(reverse('my_account'))
		self.assertContains(response, '<a href="%s>My Bookings</a>' % reverse("bookings"), html = True)

	def test_contains_link_to_logout(self):
		# Check My Account contains a link to log out.
		response = self.client.get(reverse('my_account'))
		self.assertContains(response, '<a href="%s>Log out</a>' % reverse("auth_logout"), html = True)

class templateTests(TestCase):
	#Tests pages are using templates.

	def test_bookings_using_template(self):
		# Check My Account page is using a template.
		response = self.client.get(reverse('my_account'))
		self.assertTemplateUsed(response, 'springtime/bookings.html')

	def test_trampolines_using_template(self):
		# Check Trampolines page is using a template.
		response = self.client.get(reverse('trampolines'))
		self.assertTemplateUsed(response, 'springtime/trampolines.html')

	def test_index_using_template(self):
		#Check to make sure index is using a template.
		response = self.client.get(reverse('index'))
		self.assertTemplateUsed(response, 'springtime/index.html')

	def test_contactUs_using_template(self):
		# Check to make sure Contact Us is using a template.
		response = self.client.get(reverse('contact_us'))
		self.assertTemplateUsed(response, 'springtime/contact_us.html')

	def test_reviews_using_template(self):
		# Check to make sure reviews using template.
		response = self.client.get(reverse('add_review'))
		self.assertTemplateUsed(response, 'springtime/add_review.html')

class FormTests(TestCase):

	def 

class ImageTests(TestCase):

	def test_index_contains_image(self):
		response = self.client.get(reverse('index'))
		self.assertIn('img src="/static/images/', response.content)

	def test_trampolines_contains_image(self):
		response = self.client.get(reverse('trampolines'))
		self.assertIn('img src="/static/images/', response.content)

	def test_contactUs_contains_image(self):
		response = self.client.get(reverse('contact_us'))
		self.assertIn('img src="/static/images', response.content)


class ModelTests(TestCase):

	def setUp(self):
		from populate_springtime import populate
		populate()
	except ImportError:
		print('The module populate_springtime does not exist.')
	except NameError:
		print('The function populate() does not exist or is not correct')
	except:
		print('Something went wrong in the populate() function :(')

	def get_category(self, name):
		from springtime.models import Category
		try:
			cat = Category.objects.get(name=name)
		except Category.DoesNotExist:
			cat = None
		return cat

class slugFieldTest(TestCase):

	def setUp(self):
		try:
			from populate_springtime import populate
			populate()
		except ImportError:
			print('The  module populate_springtime does not exist.')
		except NameError:
			print('The function populaate() does not exist or is incorrect.')
		except:
			print('Something went wrong in the populate() function :(')

	def test_does_slug_field_work(self):
		# Checks slug field works.
		from springtime.models import Category
		cat = Category(name='how do I create a slug in Django')
		cat.save()
		self.assertEqual(cat.slug, 'how-do-i-create-a-slug-in-django')




