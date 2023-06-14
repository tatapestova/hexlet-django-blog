from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView


class IndexView(TemplateView):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        # return redirect(reverse('article', kwargs={'article_id': 42, 'tags': 'python'}))
        return render(
        request,
        'index.html',
        context={'who': 'Tata'},
    )

def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'about.html',
        context={'tags': tags},
    )
