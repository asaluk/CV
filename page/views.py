from django.shortcuts import render
from django.views import View
from .models import Comment
from .forms import CommentForm
from django.shortcuts import redirect
# Create your views here.


class Index(View):
    def get(self, request):
        comments = Comment.objects.all().order_by('-id')[:2]
        context = {
            'data' : comments,
            'comment_form' : CommentForm(),
        }
        
        return render(request, "index.html", context)
    
    def post(self, request):
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.save()
            return redirect('index')
        
        context = {
            "comment_form" : comment_form,
        }
        return render(request, "index2.html", context)
        


