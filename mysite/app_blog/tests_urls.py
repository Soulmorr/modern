# Create your tests here.
from django.test import TestCase
from django.urls import reverse ,resolve

from .views import HomePageView, ArticleDetail, ArticleList, ArticleCategoryList


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, HomePageView)

    def test_category_view_status_code(self):
        url = reverse('articles-category-list',args=('name',))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_articles_list_url_resolves(self):
        url = reverse('articles-list')
        self.assertEquals(resolve(url).func.view_class, ArticleList)

    def test_articles_category_list_url_resolves(self):
        url = reverse('articles-category-list', kwargs={'slug': 'maximux'})
        self.assertEquals(resolve(url).func.view_class, ArticleCategoryList)

    def test_news_detail_url_resolves(self):
        url = reverse('news-detail', kwargs={'year': '2024', 'month': '04', 'day': '27', 'slug': 'maximux'})
        self.assertEquals(resolve(url).func.view_class, ArticleDetail)