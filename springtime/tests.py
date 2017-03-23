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

class URLReferenceTests(TestCase):

	def test_url_reference_in_index_page_when_logged(self):
		# Create user and log in
		test_utils.create_user()
		self.client.login(username='testuser', password = 'springtime1234')

		# Access index page
		response = self.client.get(reverse('index'))

		# Check links that appear for logged persons only
		self.assertIn(reverse('logout'), response.content)
		self.assertIn(reverse('change_password', response.content))

	def test_url_reference_in_index_when_not_logged(self):
		# Access index page with user not logged
		response = self.client.get(reverse('index'))

		# Check links that appear for logged persons
		self.assertIn(reverse('logout'), response.content)
		self.assertIn(reverse('change_password'), response.content)

class TemplateTests(TestCase):
	#Tests pages are using templates.

	def test_main_template_exists(self):
		# Check main.html exists inside template folder.
		path_to_base = settings.TEMPLATE_DIR + '/springtime/main.html'
		print path_to_base
		self.assertTrue(os.path.isfile(path_to_base))

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

class DisplayTests(TestCase):

	def test_category_page_displays_does_not_exist_message(self):
		# Try to access categories not saved to database and check message.
		response = self.client.get(reverse('show_category', args=['RoundSquare']))
		self.assertIn("The specified category does not exist!".lower().response.content.lower())

	def tests_registration_form_displayed_correctly(self):
		# Access registration page
		try:
			response = self.client.get(reverse('register'))

		except:
			try:
				response = self.client.get(reverse('springtime:register'))
			except:
				return False

		# Username label and input text
		self.assertIn('Username:', response.content)
		self.assertIn('input type="text" name="username" value="" size="50"', response.content)

		# Email label and input text
		self.assertIn('Email:', response.content)
		self.assertIn('input type="text" name="email" value="" size="50"', response.content)

		# Password label and input text
		self.assertIn('Password:', response.content)
		self.assertIn('input type="text" name="password" value="" size"50"', response.content)

		# Password confirmation label and input text
		self.assertIn('Password confirmation:', response.content)
		self.assertIn('input type="text" name="password_conf" value="" size"50"', response.content)

		# Check submit button
		self.assertIn('type="submit" name="submit" value="Register"', response.content)

	def test_login_form_displayed_correctly
		# Access login page
		try:
			response = self.client.get(reverse('login'))
		except:
			try:
				response = self.client.get(reverse('springtime:login'))
			except:
				return False

		# Username label and input text
		self.assertIn('Username:', response.content)
		self.assertIn('input type="text" name="username" value="" size="50"', response.content)

		# Password label and input text
		self.assertIn('Password:', response.content)
		self.assertIn('input type="password" name="password" value="" size="50"', response.content)

		# Submit button
		self.assertIn('input type="submit" value="submit"', response.content)

	def test_login_redirects_to_index(self):
		# Create a user
		test_utils.create_user()

		# Access login page via POST with user data
		try:
			response = self.client.post(reverse('login'), {'username': 'testuser12', 'password':'springtime1234'})
		except:
			try:
				response = self.client.post(reverse('springtime:login'), {'username': 'testuser12', 'password': 'springtime1234'})
			except:
				return False

		# Check it redirects to index
		self.assertredirects(response, reverse('index'))

	def test_index_contains_image(self):
		response = self.client.get(reverse('index'))
		self.assertIn('img src="/static/images/', response.content)

	def test_trampolines_contains_image(self):
		response = self.client.get(reverse('trampolines'))
		self.assertIn('img src="/static/images/', response.content)

	def test_contactUs_contains_image(self):
		response = self.client.get(reverse('contact_us'))
		self.assertIn('img src="/static/images', response.content)
		

class SlugFieldTest(TestCase):

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

	def test_category_contains_slug_field(self):
		# Create a new category
		new_category = Category(name="Test Category")
		new_category.save()

		# Check slug was generated
		self.assertEquals(new_category.slug, "test-category")

		# Check there is only one category
		categories = Category.objects.all()
		self.assertEquals(len(categories), 1)

		# Check attributes were saved correctly
		categories[0].slug = new_category.slug


