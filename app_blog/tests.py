
from django.test import TestCase
from django.urls import reverse, resolve

from .views import (
    HomePageView,
    ArticleDetail,
    ArticleList,
    ArticleCategoryList,
)


class URLTests(TestCase):

    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(url, '/')
        self.assertEqual(resolve(url).func.view_class, HomePageView)

    def test_articles_list_url(self):
        url = reverse('articles-list')
        self.assertEqual(url, '/articles/')
        self.assertEqual(resolve(url).func.view_class, ArticleList)

    def test_category_url(self):
        url = reverse(
            'articles-category-list',
            kwargs={'slug': 'technology'}
        )
        self.assertEqual(
            url,
            '/articles/category/technology/'
        )
        self.assertEqual(
            resolve(url).func.view_class,
            ArticleCategoryList
        )

    def test_article_detail_url(self):
        url = reverse(
            'news-detail',
            kwargs={
                'year': 2024,
                'month': 5,
                'day': 10,
                'slug': 'test-article',
            }
        )
        self.assertEqual(
            resolve(url).func.view_class,
            ArticleDetail
        )

