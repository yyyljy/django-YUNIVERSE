from django.shortcuts import render, redirect
from articles.models import Article

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def board_write(request):
    return render(request, 'articles/write.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    Article.objects.create(title=title, content=content)

    # context = {
    #     'title': title,
    #     'content': content
    # }
    #return render(request, 'articles/create.html', context)
    return redirect('articles:index')