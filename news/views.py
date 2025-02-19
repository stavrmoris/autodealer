from django.shortcuts import render, get_object_or_404

from feedback.forms import FeedbackForm
from .models import News

def news_list(request):
    form = FeedbackForm()
    news = News.objects.all().order_by('-date')
    return render(request, 'news/news_full_list.html', {'news': news, 'form': form})

def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news_item': news_item})