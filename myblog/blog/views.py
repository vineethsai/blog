from django.shortcuts import render, HttpResponse, render_to_response, HttpResponseRedirect
from .models import Post, Category
from .forms import PostForm


def home(request):
    if request.method == "GET":
        return render(request, 'index.html',
                      {
                          'posts': Post.objects.all()
                      })
    else:
        return HttpResponse("method not allowed", status=405)


def posts(request):
    if request.method == "GET":
        post_form = PostForm()
        return render(request, "newpost.html", {'form': post_form}, status=200)
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.update_or_create(
                title=form.cleaned_data["title"],
                is_published=form.cleaned_data["is_published"],
                text=form.cleaned_data["text"]
            )
            return HttpResponseRedirect('/blog/')
        else:
            return HttpResponse("invalid post", status=201)
    else:
        return HttpResponse("method not allowed", status=405)

