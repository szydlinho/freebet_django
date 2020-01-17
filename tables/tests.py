from django.urls import reverse
from django.test import TestCase
from django.urls import resolve
from .views import matches_list_view_base

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, matches_list_view_base)



class TableTabTest(TestCase):
    def test_league_tab_view_not_found_status_code(self):
        url = reverse('league_tab', kwargs={'abb': 'E2'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_league_tab_view_success_status_code(self):
        url = reverse('league_tab', kwargs={'abb': 'E0'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)