from django.shortcuts import render


def index(request):
    name = 'Статьи'
    return render(
        request,
        'articles/index.html',
        context={'name': name},
    )
