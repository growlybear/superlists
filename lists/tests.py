from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)

        # HTML5 doctype
        self.assertTrue(response.content.strip().startswith('<!DOCTYPE html>'))

        # <title>
        self.assertIn('<title>To-Do lists</title>', response.content)

        # valid closing </html> element
        self.assertTrue(response.content.strip().endswith('</html>'))
