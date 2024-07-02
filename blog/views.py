from django.shortcuts import render, redirect

from .models import Post
from .forms import CommentForm

# Create your views here.
def front_page(request):
	posts = Post.objects.all()
	context = {"posts": posts}
	return render(request, "blog/frontpage.html", context)

def post_detail(request, slug):
	post = Post.objects.get(slug=slug)
	context = {"post": post}

	if request.method == "POST":
		form = CommentForm(request.POST)
		
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()

			return redirect("post_detail", slug=post.slug)
	else:
		form = CommentForm()

	context["form"] = form
	return render(request, "blog/postdetail.html", context)
