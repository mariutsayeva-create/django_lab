from django.views.generic import TemplateView, ListView, DateDetailView
from .models import Article, Category


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['articles'] = Article.objects.filter(
            main_page=True
        ).order_by('-pub_date')[:5]
        return context


class ArticleDetail(DateDetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'item'
    date_field = 'pub_date'
    month_format = '%m'
    allow_future = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = context['item'].images.all()
        return context


class ArticleList(ListView):
    model = Article
    template_name = 'articles_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Article.objects.all().order_by('-pub_date')


class ArticleCategoryList(ArticleList):
    def get_queryset(self):
        return Article.objects.filter(
            category__slug=self.kwargs['slug']
        ).order_by('-pub_date').distinct()