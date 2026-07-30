from django.shortcuts import render
from .models import Comment

def home(request):

    if request.method == "POST":
        text = request.POST.get("text")
        Comment.objects.create(text=text)

    comments = Comment.objects.all()

    return render(
        request,
        "home.html",
        {"comments": comments}
    )