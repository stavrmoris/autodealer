from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.shortcuts import render
from .forms import FeedbackForm

def feedback1(request):
    return feedback_form_view(request, 'feedback/feedback_form1.html')


def feedback2(request):
    return feedback_form_view(request, 'feedback/feedback_form2.html')


def feedback_form_view(request, html):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, html)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Проверка AJAX-запроса
                return JsonResponse({'success': True, 'message': 'Спасибо за ваше обращение!'})
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = FeedbackForm()

    return render(request, html, {'form': form})
